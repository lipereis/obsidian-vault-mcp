---
type: conceito
status: rascunho
tags: [fundamentos, llm]
---
# LLMs

## Em uma frase
Modelos [[Transformers]] treinados para prever o próximo token em escala massiva, depois alinhados (SFT + RLHF/RLAIF) para seguir instruções.

## Ciclo de vida
1. **Pré-treino** (texto bruto) → conhecimento.
2. **Pós-treino**: instruction tuning, preferências, raciocínio (RL).
3. **Inferência**: amostragem com `temperature`, `top_p`, `max_tokens`.

## Escolhendo modelo (trade-offs)
| Eixo | Pergunta |
|---|---|
| Qualidade | passa nos meus [[Evals]]? |
| Latência | TTFT e tokens/s |
| Custo | $/M tokens in/out, cache |
| Contexto | tamanho útil real |
| Capacidades | tools, visão, JSON, raciocínio |
| Privacidade | dados saem da empresa? open-weights? |

Regra: comece com modelo forte, **meça**, depois desça para modelo menor/barato onde o eval permitir.

## Parâmetros
- `temperature` baixa → determinismo (extração); alta → criatividade.
- Modelos de raciocínio: orçamento de "thinking" aumenta qualidade/custo.

## Limitações
Alucinação, conhecimento com data de corte, não-determinismo, sensível a prompt.

## Relacionado
[[Prompt Engineering]] · [[RAG]] · [[Fine-tuning]] · [[Inference e Serving]]

## Fontes
- Docs dos provedores (Anthropic, OpenAI, Google), Hugging Face
- Karpathy: "Intro to LLMs"
