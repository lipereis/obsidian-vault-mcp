---
type: conceito
status: rascunho
tags: [infra, producao]
---
# Inference e Serving

## Conceitos
- **TTFT** (time to first token) vs **tokens/s**; prefill (compute-bound) vs decode (memory-bound).
- **KV cache**, batching contínuo, PagedAttention, speculative decoding.
- **Quantização** (INT8/4, GGUF/AWQ/GPTQ) reduz memória com pouca perda.
- **Streaming** (SSE) melhora UX percebida.

## Opções
| Opção | Quando |
|---|---|
| API gerenciada | padrão; zero ops |
| Gateway (roteamento/fallback) | multi-provedor, observabilidade, fallback |
| vLLM / TGI / SGLang | self-host open-weights em GPU |
| Ollama / llama.cpp | dev local, edge |

## Produção
Timeouts, retries com backoff, fallback de modelo, filas para batch, rate limiting, idempotência.

## Relacionado
[[Transformers]] · [[Caching e Custos]] · [[LLMs]]
