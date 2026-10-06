---
type: conceito
status: rascunho
tags: [agentes, protocolo]
---
# MCP — Model Context Protocol

## Em uma frase
Protocolo aberto (JSON-RPC) que padroniza como apps de IA se conectam a **tools, resources e prompts** externos — "USB-C" para integrações.

## Peças
- **Host/Client** (Claude Desktop, IDEs, seu agente) ↔ **Server** (expõe capacidades).
- Primitivos: **tools** (ações), **resources** (dados), **prompts** (templates).
- Transportes: stdio (local), HTTP streamable (remoto). Auth via OAuth em servers remotos.

## Exemplo mínimo (Python, FastMCP)
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("notas")

@mcp.tool()
def buscar_nota(termo: str) -> str:
    """Busca no vault Obsidian."""
    ...

if __name__ == "__main__":
    mcp.run()
```

## Ideia de projeto
MCP server que expõe **este vault** (buscar/criar notas) → [[03-Projetos/MCP Server do Vault]].

## Segurança
Confie só em servers conhecidos; tool descriptions podem conter injeção; princípio do menor privilégio → [[Guardrails e Segurança]].

## Relacionado
[[Function Calling e Tool Use]] · [[Agents]]
