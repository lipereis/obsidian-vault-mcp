---
type: conceito
status: rascunho
tags: [producao, custo]
---
# Caching e Custos

## Alavancas (maior → menor impacto típico)
1. **Prompt caching**: prefixo estável (system, tools, docs) reaproveitado → lê mais barato e rápido. Coloque conteúdo estável **antes** do variável.
2. **Modelo certo por tarefa**: roteamento (barato p/ classificar, forte p/ raciocinar).
3. **Reduzir tokens**: prompts enxutos, saída curta, `max_tokens`.
4. **Batch API** para trabalho assíncrono (desconto).
5. **Cache semântico/exato** de respostas repetidas.
6. Compactar histórico → [[Context Engineering]].

## Medir
Custo por requisição/usuário/feature em [[Observabilidade de LLMs]]; orçamento e alertas.

## Fórmula
`custo = tokens_in·p_in + tokens_cache_read·p_cache + tokens_out·p_out`

## Relacionado
[[Tokenização]] · [[Inference e Serving]]
