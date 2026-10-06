"""Testes rápidos das tools e das travas de segurança: python test_server.py"""
import os
import tempfile
from pathlib import Path

tmp = Path(tempfile.mkdtemp())
(tmp / "00-Inbox").mkdir()
(tmp / "02-Conceitos").mkdir()
(tmp / "02-Conceitos" / "RAG.md").write_text(
    "---\ntype: conceito\nstatus: rascunho\ntags: [retrieval]\n---\n# RAG\nBusca + [[Embeddings]]\n", encoding="utf-8")
(tmp / "02-Conceitos" / "Embeddings.md").write_text(
    "---\ntype: conceito\nstatus: maduro\n---\n# Embeddings\nvetores #ml\n", encoding="utf-8")
os.environ["VAULT_PATH"] = str(tmp)

import server as s  # noqa: E402


def test_all():
    assert "RAG.md" in s.listar_notas(tipo="conceito", status="rascunho")
    assert "Embeddings.md" not in s.listar_notas(status="rascunho")
    assert "02-Conceitos/RAG.md" in s.buscar_notas("busca embeddings")
    assert "vetores" in s.ler_nota("embeddings")
    links = s.listar_links("Embeddings")
    assert "02-Conceitos/RAG.md" in links
    assert "Embeddings" in s.listar_links("RAG")
    assert "criada" in s.criar_nota("Ideia: X/Y", "texto", ["t"])
    assert (tmp / "00-Inbox" / "Ideia XY.md").exists()
    try:
        s.criar_nota("Ideia XY", "x")
        raise AssertionError("deveria falhar")
    except FileExistsError:
        pass
    for bad in ("../fora", "..\\..\\x"):
        try:
            s.ler_nota(bad)
            raise AssertionError("path traversal")
        except (ValueError, FileNotFoundError):
            pass
    try:
        s.adicionar_ao_inbox("RAG", "x")
        raise AssertionError("escrita fora do inbox")
    except PermissionError:
        pass
    assert "retrieval" in s.listar_tags()


if __name__ == "__main__":
    test_all()
    print("ok")
