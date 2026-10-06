---
type: conceito
status: rascunho
tags: [seguranca, producao]
---
# Guardrails e Segurança

## Ameaças (OWASP LLM Top 10)
- **Prompt injection** (direta e **indireta** via docs/web/tool results).
- Vazamento de dados/system prompt; saída insegura (XSS, SQL) ; excesso de agência; alucinação; DoS de custo.

## Defesas em camadas
1. **Menor privilégio** nas tools; confirmação humana em ações sensíveis.
2. Separar instruções de dados não confiáveis; tratar saída de tool como não confiável.
3. Validação de entrada/saída (schemas, classificadores, regex, moderação).
4. Sandbox para execução de código.
5. Limites: passos, tokens, orçamento, rate limit por usuário.
6. Sem segredos no prompt; filtro de PII.
7. Red-teaming e [[Evals]] adversariais.

## Regra de ouro
Nunca confie em instruções vindas de conteúdo recuperado; assuma que o modelo **pode** ser enganado e limite o dano.

## Relacionado
[[Agents]] · [[MCP - Model Context Protocol]] · [[Observabilidade de LLMs]]
