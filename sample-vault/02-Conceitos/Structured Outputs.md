---
type: conceito
status: rascunho
tags: [prompting, producao]
---
# Structured Outputs

## Em uma frase
Forçar o LLM a devolver JSON válido segundo um schema, para integrar com código.

## Abordagens (da mais frágil à mais robusta)
1. Pedir JSON no prompt + parse (frágil).
2. **Schema-constrained decoding** / modo JSON do provedor.
3. **Tool use** com `input_schema` (padrão confiável) → [[Function Calling e Tool Use]].
4. Validar com Pydantic + retry com mensagem de erro.

## Código
```python
from pydantic import BaseModel
class Pessoa(BaseModel):
    nome: str
    idade: int | None = None

# valide sempre, mesmo com schema no provedor
p = Pessoa.model_validate_json(resposta)
```

## Boas práticas
- Campos opcionais explícitos; enums para categorias.
- Descrição por campo ajuda o modelo.
- Sempre valide e trate falha (retry limitado).

## Relacionado
[[Prompt Engineering]] · [[Evals]]
