---
type: conceito
status: rascunho
tags: [ml, fundamentos]
---
# Métricas e Avaliação de ML

## Em uma frase
Medir se um modelo generaliza: separe dados em treino/validação/teste e escolha métrica alinhada ao negócio.

## Essencial
- **Overfitting** vs **underfitting**; viés–variância.
- Classificação: precision, recall, F1, ROC-AUC. Desbalanceamento → accuracy engana.
- Regressão: MAE, RMSE, R².
- Ranking/retrieval: recall@k, MRR, nDCG (usado em [[RAG]]).
- **Data leakage**: info do teste vazando pro treino.

## Flashcards
Quando recall importa mais que precision?::Quando falso negativo é caro (ex.: detecção de fraude/doença).
O que é data leakage?::Informação do conjunto de teste influenciando o treino, inflando métricas.

## Relacionado
[[Evals]] · [[MOC - AI Engineering]]
