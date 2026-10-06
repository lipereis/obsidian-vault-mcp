---
type: conceito
status: rascunho
tags: [agentes, arquitetura]
---
# Agents

## Em uma frase
LLM em **loop** usando ferramentas para atingir um objetivo, decidindo o próximo passo com base nos resultados.

## Workflow vs Agente
- **Workflow**: caminho de código predefinido, LLM em etapas (prompt chaining, routing, paralelização, orchestrator-workers, evaluator-optimizer).
- **Agente**: o LLM decide dinamicamente. Mais flexível, mais caro, menos previsível.
- Regra: use a solução **mais simples** que resolve; agente só quando o caminho é imprevisível.

## Componentes
Modelo · [[Function Calling e Tool Use|tools]] · memória/estado · [[Context Engineering]] · condição de parada · sandbox/permissões · [[Observabilidade de LLMs]].

## Padrões
ReAct (raciocinar+agir) · plan-and-execute · reflexão/auto-crítica · human-in-the-loop · sub-agentes ([[Multi-Agent Systems]]).

## Riscos
Loops infinitos, custo descontrolado, ações destrutivas, prompt injection via tools → [[Guardrails e Segurança]]. Limite passos/orçamento, logue tudo.

## Fontes
- Anthropic: "Building effective agents"
- Docs de Agent SDKs

## Relacionado
[[MCP - Model Context Protocol]] · [[Evals]]
