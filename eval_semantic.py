"""Eval de retrieval: recall@3 e MRR da busca semântica sobre o vault real.

Uso: python eval_semantic.py            (modelo padrão)
     VAULT_EMBED_MODEL=<modelo> python eval_semantic.py
Consultas são paráfrases sem as palavras-chave da nota esperada.
"""
import sys
import time

import server as s
import semantic

CASES = [
    ("como evitar que o modelo invente respostas", {"RAG", "Evals", "LLMs", "Entrevistas AI Engineer"}),
    ("gastar menos dinheiro com a API", {"Caching e Custos"}),
    ("como me preparar para conseguir emprego na área", {"Portfólio", "Entrevistas AI Engineer", "Roadmap AI Engineer"}),
    ("proteger o sistema contra ataques de usuários maliciosos", {"Guardrails e Segurança"}),
    ("como saber se meu sistema está funcionando bem", {"Evals", "Observabilidade de LLMs"}),
    ("dividir documentos em pedaços para indexar", {"RAG"}),
    ("deixar a resposta do modelo mais rápida", {"Inference e Serving", "Caching e Custos"}),
    ("fazer o modelo chamar funções do meu código", {"Function Calling e Tool Use"}),
    ("garantir que a resposta venha em JSON válido", {"Structured Outputs"}),
    ("onde guardar vetores para busca por similaridade", {"Vector Databases"}),
    ("treinar o modelo com meus próprios dados", {"Fine-tuning"}),
    ("vários agentes trabalhando juntos", {"Multi-Agent Systems"}),
    ("o que colocar na janela de contexto", {"Context Engineering"}),
    ("padrão para conectar ferramentas externas a assistentes", {"MCP - Model Context Protocol"}),
    ("o que estudar nos próximos três meses", {"Plano 90 dias", "Roadmap AI Engineer"}),
]

# termos exatos/siglas: onde a busca lexical deveria ajudar
EXACT = [
    ("HNSW", {"Vector Databases"}),
    ("LoRA QLoRA", {"Fine-tuning"}),
    ("KV cache", {"Transformers", "Inference e Serving"}),
    ("pgvector", {"Vector Databases", "RAG com Citações", "MOC - Recursos"}),
    ("OWASP", {"Guardrails e Segurança"}),
    ("TTFT", {"Inference e Serving", "Observabilidade de LLMs", "LLMs"}),
    ("FastMCP stdio", {"MCP - Model Context Protocol", "MCP Server do Vault"}),
    ("recall@k MRR nDCG", {"Métricas e Avaliação de ML"}),
    ("lost in the middle", {"RAG", "Transformers", "MOC - Recursos"}),
    ("STAR comportamental", {"Entrevistas AI Engineer"}),
]
POOL = int(next((a.split("=")[1] for a in sys.argv if a.startswith("--pool=")), 30))

MODES = {
    "densa": lambda q: semantic.search(q, s._semantic_notes(), s.VAULT, 3),
    "hibrida (RRF)": lambda q: semantic.hybrid_search(q, s._semantic_notes(), s.VAULT, 3, use_rerank=False),
    "hibrida + rerank": lambda q: semantic.hybrid_search(q, s._semantic_notes(), s.VAULT, 3, pool=POOL),
}
VERBOSE = "-v" in sys.argv
print(f"embeddings: {semantic.MODEL}")
print(f"reranker:   {semantic.RERANKER}\n")
for label, cases in (("PARAFRASES", CASES), ("TERMOS EXATOS", EXACT)):
    print(f"== {label} (n={len(cases)})")
    for name, fn in MODES.items():
        fn("aquecimento")
        hit = top1 = mrr = 0
        t0 = time.time()
        for q, expected in cases:
            stems = [c["path"].rsplit("/", 1)[-1][:-3] for _, c in fn(q)]
            rank = next((i + 1 for i, st in enumerate(stems) if st in expected), 0)
            hit += bool(rank)
            top1 += rank == 1
            mrr += 1 / rank if rank else 0
            if VERBOSE or not rank:
                print(f"  [{name}] {'OK ' if rank else 'MISS'} {q} -> {stems}")
        n = len(cases)
        print(f"{name:18} recall@3 {hit}/{n}  top1 {top1}/{n}  MRR {mrr / n:.2f}  {(time.time() - t0) / n * 1000:.0f} ms/consulta")
