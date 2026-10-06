---
type: conceito
status: rascunho
tags: [retrieval, infra]
---
# Vector Databases

## Em uma frase
Armazenam [[Embeddings]] e fazem busca por vizinho mais próximo aproximada (ANN) com filtros por metadados.

## Índices
- **HNSW**: grafo, rápido e preciso, memória alta (padrão).
- **IVF / IVF-PQ**: clusters + quantização, menos memória.
- **Flat**: exato, só p/ bases pequenas.

## Opções
| Tipo | Exemplos | Quando |
|---|---|---|
| Extensão Postgres | pgvector | já tem Postgres; começo simples |
| Dedicado | Qdrant, Weaviate, Milvus, Pinecone | escala/recursos avançados |
| Embutido/local | Chroma, LanceDB, SQLite-vec | protótipo, local |

## Dicas
- Comece com **pgvector**; migre só se necessário.
- Guarde metadados (fonte, página, data, permissões) e filtre por eles.
- Combine com BM25 (hybrid) e **reranker**.
- Meça recall@k contra busca exata.

## Relacionado
[[RAG]] · [[Embeddings]]
