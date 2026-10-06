---
type: conceito
status: rascunho
tags: [fundamentos, llm]
---
# Tokenização

## Em uma frase
Converte texto em IDs de sub-palavras (BPE/SentencePiece); o modelo só "vê" tokens, não caracteres.

## Por que importa
- **Custo e limite** são em tokens (≈ 0,75 palavra em inglês; português gasta mais).
- Explica falhas em contar letras, aritmética, idiomas raros.
- Janela de contexto = prompt + saída.

## Código
```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
print(len(enc.encode("Olá, mundo!")))
```
> Cada provedor tem seu tokenizer; para contagem exata use a API de token counting do provedor.

## Armadilhas
- Contar tokens com tokenizer errado.
- Espaços/maiúsculas mudam tokens.

## Relacionado
[[Transformers]] · [[LLMs]] · [[Caching e Custos]]
