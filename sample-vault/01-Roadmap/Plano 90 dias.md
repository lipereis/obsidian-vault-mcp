---
type: plano
tags: [roadmap, plano]
---
# Plano 90 dias

Ritmo: 1-2 h/dia úteis + 4 h fim de semana. Regra: **toda semana termina com algo rodando**.

## Mês 1 — Fundamentos + primeiro app
| Sem | Foco | Entregável |
|---|---|---|
| 1 | Python moderno, pydantic, async, API do LLM | script que chama LLM com streaming |
| 2 | [[Tokenização]], [[Prompt Engineering]], [[Structured Outputs]] | extrator JSON de textos |
| 3 | [[Embeddings]] + busca semântica | busca semântica em notas (este vault!) |
| 4 | FastAPI + front simples | chat web deployado |

## Mês 2 — RAG + Agentes
| Sem | Foco | Entregável |
|---|---|---|
| 5 | [[Vector Databases]], chunking | indexador de PDFs |
| 6 | [[RAG]] avançado: hybrid, rerank | RAG com citações |
| 7 | [[Function Calling e Tool Use]] | agente com 3 tools |
| 8 | [[MCP - Model Context Protocol]] | MCP server próprio |

## Mês 3 — Qualidade + produção + portfólio
| Sem | Foco | Entregável |
|---|---|---|
| 9 | [[Evals]] | dataset de 50 casos + runner |
| 10 | [[Observabilidade de LLMs]] (Langfuse/LangSmith) | tracing no projeto RAG |
| 11 | [[Guardrails e Segurança]], [[Caching e Custos]] | hardening + relatório de custo |
| 12 | Polimento | 2 projetos com README, demo e post |

## Rituais
- Diário: [[99-Templates/Diário|daily note]] (5 min)
- Semanal: [[99-Templates/Revisão Semanal|revisão]] (30 min, domingo)
- Mensal: reavaliar [[Roadmap AI Engineer]]
