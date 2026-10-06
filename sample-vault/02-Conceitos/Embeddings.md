---
type: conceito
status: rascunho
tags: [retrieval, fundamentos]
---
# Embeddings

## Em uma frase
Vetores densos que codificam significado; textos semelhantes ficam próximos no espaço.

## Como usar
- Similaridade: **cosseno** (ou dot product se normalizados).
- Usos: busca semântica, [[RAG]], clustering, deduplicação, classificação, recomendação.
- Dimensão (384–3072) afeta custo/armazenamento; alguns modelos permitem truncar (Matryoshka).

## Código
```python
import numpy as np
def cos(a, b): return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
```

## Armadilhas
- Misturar modelos de embedding entre indexação e consulta.
- Não reindexar ao trocar de modelo.
- Embedding ≠ busca exata (IDs, siglas) → use **hybrid** (BM25 + vetor).
- Idioma: avalie modelos multilíngues em PT-BR.

## Flashcards
Por que normalizar vetores?::Cosseno vira dot product, mais rápido e consistente.

## Relacionado
[[Vector Databases]] · [[RAG]]
