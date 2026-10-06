---
type: conceito
status: rascunho
tags: [producao, qualidade]
---
# Observabilidade de LLMs

## O que registrar
- **Traces** completos: prompt, versão, modelo, params, tool calls, resposta, erros.
- Tokens in/out/cache, **custo**, latência (TTFT, total), taxa de erro/retry.
- Feedback do usuário (👍/👎) e correções.
- IDs de sessão/usuário (com cuidado com PII).

## Uso
- Depurar falhas → transformar em casos de [[Evals]].
- Alertas de custo/latência/qualidade.
- A/B de prompts e modelos.

## Ferramentas
Langfuse · LangSmith · Helicone · Arize Phoenix · OpenTelemetry (GenAI semantic conventions).

## Relacionado
[[Caching e Custos]] · [[Guardrails e Segurança]]
