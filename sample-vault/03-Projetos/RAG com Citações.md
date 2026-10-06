---
type: projeto
status: ideia
stack: [python, pgvector, embeddings, reranker]
tags: [projeto, rag]
---
# RAG com Citações

## Objetivo
Perguntar sobre seus PDFs/notas e receber resposta com **citação de fonte/página**; recusar quando não houver evidência.

## Milestones
- [ ] Ingestão (parse + chunking + embeddings)
- [ ] Busca hybrid (vetor + BM25)
- [ ] Reranker
- [ ] Prompt com citações obrigatórias
- [ ] Dataset de 50 perguntas + métricas recall@k e fidelidade
- [ ] Tracing ([[Observabilidade de LLMs]])

## Conceitos
[[RAG]] · [[Embeddings]] · [[Vector Databases]] · [[Evals]] · [[Context Engineering]]
