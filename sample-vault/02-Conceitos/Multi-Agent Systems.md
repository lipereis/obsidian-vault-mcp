---
type: conceito
status: rascunho
tags: [agentes, arquitetura]
---
# Multi-Agent Systems

## Em uma frase
Vários agentes especializados coordenados (orquestrador + workers) para paralelizar e isolar contexto.

## Quando vale
- Tarefas paralelizáveis (pesquisa ampla), contextos grandes que estouram um único agente, especialização clara.
- **Custo**: muito mais tokens; coordenação complexa. Não use por moda.

## Padrões
- **Orchestrator-workers**: líder planeja, sub-agentes executam e devolvem resumo.
- **Pipeline**: agente A → B → C.
- **Debate/revisão**: crítico revisa o gerador.

## Dicas
- Briefing completo a cada sub-agente (ele não vê seu contexto).
- Saída compacta e estruturada de volta.
- Estado compartilhado via arquivos/DB.
- Avalie vs. agente único — [[Evals]].

## Relacionado
[[Agents]] · [[Context Engineering]]
