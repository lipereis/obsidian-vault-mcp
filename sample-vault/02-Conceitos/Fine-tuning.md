---
type: conceito
status: rascunho
tags: [customizacao]
---
# Fine-tuning

## Em uma frase
Continuar treinando um modelo com seus dados para ajustar **comportamento/estilo/formato** (pouco para injetar conhecimento).

## Quando considerar
Só após esgotar [[Prompt Engineering]] e [[RAG]], com [[Evals]] mostrando gap. Motivos: reduzir custo/latência (modelo menor), formato rígido, tom de marca, tarefa de nicho.

## Técnicas
- **SFT** com pares instrução→resposta (qualidade > quantidade; centenas a milhares).
- **PEFT: LoRA / QLoRA** — treina poucos parâmetros; roda em GPU modesta.
- **Preference tuning** (DPO), RL com recompensas verificáveis.
- **Destilação**: modelo grande gera dados p/ treinar menor.

## Stack
Hugging Face (transformers, peft, trl) · Unsloth · Axolotl · serviços gerenciados de fine-tuning.

## Armadilhas
Dados ruins, vazamento de eval, esquecimento catastrófico, custo de manter modelo.

## Relacionado
[[LLMs]] · [[Inference e Serving]]
