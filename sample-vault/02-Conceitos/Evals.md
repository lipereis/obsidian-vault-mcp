---
type: conceito
status: rascunho
tags: [qualidade, producao]
---
# Evals

## Em uma frase
Testes automatizados para sistemas de LLM: dataset + execução + métricas. É o que separa demo de produto.

## Passos
1. **Dataset**: comece com 20–50 casos reais + casos-limite; cresça com falhas de produção.
2. **Graders**:
   - Código (exact match, regex, schema, testes unitários) — preferir.
   - **LLM-as-judge** com rubrica clara (calibrar com humanos, evitar viés de posição/verbosidade).
   - Humano para amostra.
3. **Métricas**: acurácia, fidelidade ao contexto, recall@k (RAG), taxa de recusa correta, custo, latência.
4. **Rodar no CI** e a cada mudança de prompt/modelo (regressão).
5. **Análise de erros**: leia os erros — maior ROI.

## Por tipo de sistema
- [[RAG]]: retrieval e geração separados.
- [[Agents]]: sucesso da tarefa, nº de passos, uso correto de tools, custo.
- Extração: precision/recall por campo.

## Ferramentas
Promptfoo · Braintrust · LangSmith · Langfuse · Inspect (UK AISI) · Ragas · DeepEval.

## Template
[[99-Templates/Experimento de Eval]]

## Relacionado
[[Observabilidade de LLMs]] · [[Métricas e Avaliação de ML]]
