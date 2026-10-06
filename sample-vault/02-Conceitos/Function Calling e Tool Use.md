---
type: conceito
status: rascunho
tags: [agentes]
---
# Function Calling e Tool Use

## Em uma frase
O modelo não executa nada: ele **pede** a chamada de uma função (nome + argumentos JSON); seu código executa e devolve o resultado.

## Loop
1. Envia `tools` (nome, descrição, schema) + mensagem.
2. Modelo responde com `tool_use` (stop_reason = tool_use).
3. Você executa, devolve `tool_result`.
4. Repete até resposta final.

## Código (esboço)
```python
import anthropic
client = anthropic.Anthropic()
tools = [{
  "name": "get_clima",
  "description": "Retorna clima atual de uma cidade",
  "input_schema": {"type": "object",
    "properties": {"cidade": {"type": "string"}}, "required": ["cidade"]},
}]
msgs = [{"role": "user", "content": "Clima em Recife?"}]
while True:
    r = client.messages.create(model="claude-sonnet-5-5", max_tokens=1024,
                               tools=tools, messages=msgs)
    if r.stop_reason != "tool_use":
        break
    msgs.append({"role": "assistant", "content": r.content})
    results = []
    for b in r.content:
        if b.type == "tool_use":
            results.append({"type": "tool_result", "tool_use_id": b.id,
                            "content": executar(b.name, b.input)})
    msgs.append({"role": "user", "content": results})
```

## Design de tools
- Poucas, claras, nomes e descrições como se explicasse a um júnior.
- Retorne o mínimo útil; erros legíveis que ajudem o modelo a corrigir.
- Idempotência e confirmação humana para ações destrutivas.

## Relacionado
[[Agents]] · [[MCP - Model Context Protocol]] · [[Structured Outputs]]
