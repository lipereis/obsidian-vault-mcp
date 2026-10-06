---
type: projeto
status: ideia
stack: [python, pytest, promptfoo]
tags: [projeto, eval]
---
# Pipeline de Evals

## Objetivo
Runner reutilizável: dataset (JSONL) → executa sistema → graders (código + LLM judge) → relatório e gate no CI.

## Milestones
- [ ] Formato de dataset
- [ ] Graders por código
- [ ] LLM-as-judge calibrado
- [ ] Relatório comparando versões
- [ ] GitHub Actions bloqueando regressão

## Conceitos
[[Evals]] · [[Observabilidade de LLMs]] · [[Métricas e Avaliação de ML]]
