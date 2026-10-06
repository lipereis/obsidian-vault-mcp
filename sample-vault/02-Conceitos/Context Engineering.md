---
type: conceito
status: rascunho
tags: [prompting, agentes]
---
# Context Engineering

## Em uma frase
Decidir **o que entra na janela de contexto** a cada passo: instruções, memória, resultados de tools, docs recuperados, histórico.

## Princípios
- Contexto é recurso finito e degrada com ruído ("context rot").
- Menor conjunto de tokens de alto sinal.
- **Just-in-time**: guardar referências (caminhos, IDs) e carregar sob demanda via tools.
- **Compactação**: resumir histórico longo; **notas externas** (arquivo/memória) para longo prazo.
- **Sub-agentes** com contexto limpo retornando só resumo → [[Multi-Agent Systems]].
- Ordene: estável no início (cache!), variável no fim → [[Caching e Custos]].

## Camadas
System prompt · ferramentas · exemplos · memória · retrieval ([[RAG]]) · histórico · estado da tarefa.

## Relacionado
[[Prompt Engineering]] · [[Agents]]
