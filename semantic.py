"""Busca semântica local: chunks por seção -> embeddings (fastembed/ONNX) -> cosseno.

Índice incremental em .cache/ (reembeda só notas cujo mtime mudou).
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import numpy as np

MODEL = os.environ.get("VAULT_EMBED_MODEL", "sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
CACHE = Path(os.environ.get("VAULT_CACHE_DIR") or Path(__file__).parent / ".cache")
META, VECS = CACHE / "index.json", CACHE / "vectors.npy"
MAX_CHARS = 1200
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n?", re.S)

_model = None


def _embed(texts: list[str], query: bool = False) -> np.ndarray:
    global _model
    if "e5" in MODEL:  # modelos E5 exigem prefixo por papel
        texts = [("query: " if query else "passage: ") + t for t in texts]
    if _model is None:
        from fastembed import TextEmbedding
        _model = TextEmbedding(MODEL)
    v = np.array(list(_model.embed(texts)), dtype=np.float32)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def chunk(title: str, text: str) -> list[dict]:
    """Divide por headings '## '; prefixa o título da nota em cada chunk (contexto)."""
    body = FRONTMATTER.sub("", text)
    out = []
    for sec in re.split(r"\n(?=#{1,3} )", body):
        sec = sec.strip()
        if len(sec) < 20:
            continue
        heading = sec.splitlines()[0].lstrip("# ").strip() if sec.startswith("#") else ""
        for i in range(0, len(sec), MAX_CHARS):
            piece = sec[i:i + MAX_CHARS]
            out.append({"heading": heading, "text": piece, "embed": f"{title} — {heading}\n{piece}"})
    return out


def build(notes: list[Path], vault: Path, force: bool = False) -> tuple[list[dict], np.ndarray, int]:
    """Retorna (chunks, vetores, n_notas_reembedadas), reaproveitando o cache."""
    old_meta, old_vecs = {"model": None, "files": {}}, None
    if not force and META.exists() and VECS.exists():
        old_meta = json.loads(META.read_text(encoding="utf-8"))
        old_vecs = np.load(VECS)
        if old_meta.get("model") != MODEL:
            old_meta, old_vecs = {"model": None, "files": {}}, None

    files, chunks, parts, pending = {}, [], [], []
    for p in sorted(notes):
        rel = p.relative_to(vault).as_posix()
        mtime = p.stat().st_mtime
        prev = old_meta["files"].get(rel)
        if prev and prev["mtime"] == mtime and old_vecs is not None:
            cs, vs = prev["chunks"], old_vecs[prev["start"]:prev["start"] + len(prev["chunks"])]
        else:
            cs = chunk(p.stem, p.read_text(encoding="utf-8"))
            vs = None
            pending.append((rel, cs))
        files[rel] = {"mtime": mtime, "chunks": [{"heading": c["heading"], "text": c["text"]} for c in cs]}
        parts.append((rel, vs))

    if pending:
        flat = [c["embed"] for _, cs in pending for c in cs]
        new = _embed(flat) if flat else np.zeros((0, 1), dtype=np.float32)
        fresh, i = {}, 0
        for rel, cs in pending:
            fresh[rel] = new[i:i + len(cs)]
            i += len(cs)
        parts = [(rel, fresh[rel] if vs is None else vs) for rel, vs in parts]

    start, mats = 0, []
    for rel, vs in parts:
        files[rel]["start"] = start
        start += len(files[rel]["chunks"])
        if len(vs):
            mats.append(vs)
        chunks += [{"path": rel, **c} for c in files[rel]["chunks"]]
    vecs = np.vstack(mats) if mats else np.zeros((0, 1), dtype=np.float32)

    if pending or set(files) != set(old_meta["files"]):
        CACHE.mkdir(exist_ok=True)
        META.write_text(json.dumps({"model": MODEL, "files": files}, ensure_ascii=False), encoding="utf-8")
        np.save(VECS, vecs)
    return chunks, vecs, len(pending)


def search(query: str, notes: list[Path], vault: Path, k: int = 8) -> list[tuple[float, dict]]:
    chunks, vecs, _ = build(notes, vault)
    if not chunks:
        return []
    scores = vecs @ _embed([query], query=True)[0]
    best: dict[str, tuple[float, dict]] = {}  # melhor chunk por nota
    for i in np.argsort(-scores):
        c = chunks[int(i)]
        if c["path"] not in best:
            best[c["path"]] = (float(scores[i]), c)
        if len(best) >= k:
            break
    return list(best.values())


# ---------- híbrida: BM25 + denso -> RRF -> reranker (cross-encoder) ----------

RERANKER = os.environ.get("VAULT_RERANK_MODEL", "jinaai/jina-reranker-v2-base-multilingual")
STOP = set("a o e de do da dos das em no na nos nas um uma para por com que se os as ao como mais meu minha "
           "the of to and in for is on with".split())
_reranker = None


def _tokens(text: str) -> list[str]:
    import unicodedata
    text = unicodedata.normalize("NFKD", text.lower()).encode("ascii", "ignore").decode()
    return [t for t in re.findall(r"[a-z0-9]+", text) if t not in STOP and len(t) > 1]


def bm25(query: str, docs: list[str], k1: float = 1.5, b: float = 0.75) -> np.ndarray:
    toks = [_tokens(d) for d in docs]
    avg = sum(map(len, toks)) / max(1, len(toks))
    df: dict[str, int] = {}
    for t in toks:
        for w in set(t):
            df[w] = df.get(w, 0) + 1
    scores = np.zeros(len(docs), dtype=np.float32)
    for q in set(_tokens(query)):
        if q not in df:
            continue
        idf = np.log(1 + (len(docs) - df[q] + 0.5) / (df[q] + 0.5))
        for i, t in enumerate(toks):
            tf = t.count(q)
            if tf:
                scores[i] += idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * len(t) / avg))
    return scores


def rerank(query: str, texts: list[str], batch_size: int = 4) -> np.ndarray:
    """Cross-encoder. Ordena por tamanho e usa lotes pequenos: cada lote é
    preenchido (padding) até o maior texto, então misturar curtos e longos
    desperdiça computação. Resultado é devolvido na ordem original."""
    global _reranker
    if _reranker is None:
        from fastembed.rerank.cross_encoder import TextCrossEncoder
        _reranker = TextCrossEncoder(RERANKER)
    order = sorted(range(len(texts)), key=lambda i: len(texts[i]))
    if batch_size <= 0:  # comportamento antigo (lote único, sem ordenar)
        return np.array(list(_reranker.rerank(query, texts)), dtype=np.float32)
    scores = np.zeros(len(texts), dtype=np.float32)
    ranked = list(_reranker.rerank(query, [texts[i] for i in order], batch_size=batch_size))
    scores[order] = ranked
    return scores


def hybrid_search(query: str, notes: list[Path], vault: Path, k: int = 8,
                  use_rerank: bool = True, pool: int = 30, rrf_k: int = 60,
                  batch_size: int = 4) -> list[tuple[float, dict]]:
    """Funde ranking lexical (BM25) e denso por RRF; opcionalmente reordena o
    top `pool` com cross-encoder. Retorna melhor chunk por nota."""
    chunks, vecs, _ = build(notes, vault)
    if not chunks:
        return []
    docs = [f"{Path(c['path']).stem} {c['heading']}\n{c['text']}" for c in chunks]
    dense = vecs @ _embed([query], query=True)[0]
    lex = bm25(query, docs)
    fused = np.zeros(len(chunks), dtype=np.float32)
    for scores in (dense, lex):
        order = np.argsort(-scores)
        for rank, i in enumerate(order):
            if scores[i] > 0:
                fused[i] += 1.0 / (rrf_k + rank + 1)
    top = [int(i) for i in np.argsort(-fused)[:pool]]
    if use_rerank:
        rs = rerank(query, [docs[i] for i in top], batch_size)
        ranked = sorted(zip(rs.tolist(), top), reverse=True)
    else:
        ranked = [(float(fused[i]), i) for i in top]
    best: dict[str, tuple[float, dict]] = {}
    for s, i in ranked:
        c = chunks[i]
        if c["path"] not in best:
            best[c["path"]] = (s, c)
        if len(best) >= k:
            break
    return list(best.values())
