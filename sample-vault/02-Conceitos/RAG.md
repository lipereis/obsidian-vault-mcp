---
type: conceito
status: rascunho
tags: [retrieval, arquitetura]
---
# RAG (Retrieval-Augmented Generation)

## Em uma frase
Buscar trechos relevantes numa base externa e injetá-los no prompt para o LLM responder com fundamento e citação.

## Pipeline
1. **Ingestão**: parse (PDF/HTML) → limpeza → **chunking** → [[Embeddings]] → [[Vector Databases]].
2. **Consulta**: reescrever pergunta → buscar (vetor + BM25) → **rerank** → montar contexto.
3. **Geração**: prompt com contexto + instrução de citar e de recusar se faltar evidência.
4. **Avaliação**: retrieval (recall@k) e geração (fidelidade, relevância) → [[Evals]].

## Chunking
- 200–800 tokens, overlap 10–20%, respeitar estrutura (títulos, parágrafos).
- Anexar contexto ao chunk (título do doc/seção) — "contextual retrieval".

## Melhorias
Hybrid search · reranker (cross-encoder) · query rewriting/HyDE · multi-query · parent-document retrieval · filtros por metadado · GraphRAG para relações.

## RAG vs Fine-tuning vs contexto longo
- Conhecimento mutável/privado/citável → **RAG**.
- Estilo/formato/comportamento → [[Fine-tuning]].
- Base pequena → às vezes basta colocar tudo no contexto + [[Caching e Custos|prompt caching]].

## Falhas comuns
Chunk ruim · busca traz lixo · contexto demais ("lost in the middle") · sem fallback "não sei" · sem eval.

## Relacionado
[[Context Engineering]] · [[Agents]] (agentic RAG)
