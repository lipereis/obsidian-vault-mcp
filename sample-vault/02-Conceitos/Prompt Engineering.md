---
type: conceito
status: rascunho
tags: [prompting]
---
# Prompt Engineering

## Em uma frase
Projetar instruções + contexto + exemplos para obter saída confiável do modelo. Hoje é parte de [[Context Engineering]].

## Técnicas que funcionam
1. **Seja específico**: papel, tarefa, formato, restrições, público.
2. **Few-shot**: 2–5 exemplos diversos, incluindo casos-limite.
3. **Delimitadores** (XML/markdown) para separar instruções de dados.
4. **Raciocínio**: peça passos/uso de thinking para tarefas difíceis.
5. **Dê saída de escape**: "se não souber, diga que não sabe".
6. **Saída estruturada** → [[Structured Outputs]].
7. **Iterar com [[Evals]]**, não por intuição.

## Anti-padrões
- Prompt gigante sem estrutura; instruções contraditórias.
- Mudar prompt sem versionar nem medir.
- Colocar dados não confiáveis como instrução → [[Guardrails e Segurança]].

## Template
```
<papel>Você é ...</papel>
<tarefa>...</tarefa>
<regras>- ...</regras>
<exemplos>...</exemplos>
<entrada>{{dados}}</entrada>
<formato_saida>...</formato_saida>
```

## Relacionado
[[LLMs]] · [[Evals]]
