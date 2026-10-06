---
type: conceito
status: rascunho
tags: [fundamentos, arquitetura]
---
# Transformers

## Em uma frase
Arquitetura baseada em **self-attention**: cada token pondera todos os outros para construir representações contextuais, em paralelo.

## Como funciona
- Input: tokens → [[Embeddings]] + codificação posicional (ex.: RoPE).
- **Self-attention**: Q, K, V; `softmax(QKᵀ/√d)·V`.
- Multi-head → várias "visões" de relação.
- Blocos: attention + MLP + residual + layer norm, empilhados.
- LLMs modernos: **decoder-only**, geração autoregressiva (próximo token).
- **KV cache**: reaproveita K/V de tokens passados na inferência → ver [[Inference e Serving]].
- Custo de atenção cresce ~O(n²) com contexto.

## Por que importa p/ AI Eng
Explica limites de contexto, latência (prefill vs decode), custo e por que ordem/posição no prompt importa ("lost in the middle").

## Flashcards
Por que dividir por √d na atenção?::Estabiliza a variância dos produtos escalares, evitando softmax saturado.
Prefill vs decode?::Prefill processa o prompt em paralelo; decode gera 1 token por vez (bound por memória).

## Relacionado
[[LLMs]] · [[Tokenização]]

## Fontes
- "Attention Is All You Need" (Vaswani et al., 2017)
- Vídeos do Andrej Karpathy (Let's build GPT)
- The Illustrated Transformer (Jay Alammar)
