---
type: carreira
tags: [carreira, entrevista]
---
# Entrevistas AI Engineer

## Perguntas típicas
- RAG vs fine-tuning: quando usar cada um? → [[RAG]], [[Fine-tuning]]
- Como avaliar um sistema de LLM sem ground truth? → [[Evals]]
- Como reduzir alucinação? → RAG, citações, "não sei", verificação, evals
- Projete um chatbot de suporte com RAG: ingestão, retrieval, fallback, métricas, custo
- Como proteger um agente contra prompt injection? → [[Guardrails e Segurança]]
- Como reduzir custo/latência? → [[Caching e Custos]], [[Inference e Serving]]
- Workflow vs agente? → [[Agents]]
- Explique atenção e KV cache → [[Transformers]]
- Chunking: trade-offs de tamanho/overlap?

## System design (roteiro)
Requisitos → dados → arquitetura → modelo → avaliação → falhas/segurança → custo/escala → monitoramento.

## Coding
Python async, FastAPI, pydantic, SQL, estruturas de dados básicas, implementar cosine similarity / top-k / chunker.

## Comportamental
Histórias STAR: impacto, trade-off, falha e aprendizado.
