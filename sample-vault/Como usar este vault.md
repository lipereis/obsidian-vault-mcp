---
tags: [meta]
---
# Como usar este vault

Segundo cérebro (PKM) focado em **AI Engineering**. Método: **PARA leve + Zettelkasten + MOCs**.

## Setup (5 min)
1. Obsidian → *Open folder as vault* → esta pasta (`ai-engineering`).
2. *Settings → Community plugins → Turn on* → instale: **Dataview**, **Templater**, **Tasks**, **Calendar**, **Spaced Repetition**.
3. Dataview: ative *Enable JavaScript Queries* e *Inline queries*.
4. Templater: *Template folder* = `99-Templates`, ligue *Trigger on new file creation*.
5. Abra [[Dashboard]].

## Estrutura
| Pasta | Função |
|---|---|
| `00-Inbox` | captura rápida, sem organizar |
| `01-Roadmap` | trilha de aprendizado e planos |
| `02-Conceitos` | notas atômicas (1 ideia = 1 nota) ligadas por MOC |
| `03-Projetos` | projetos práticos / portfólio |
| `04-Recursos` | livros, cursos, papers, ferramentas |
| `05-Diario` | daily notes (o que estudei/construí) |
| `06-Carreira` | portfólio, entrevistas, vagas, networking |
| `07-Anexos` | imagens e PDFs |
| `99-Templates` | templates Templater |

## Fluxo diário
1. **Capturar** → qualquer coisa vai pro Inbox.
2. **Estudar** → crie nota de Recurso (`99-Templates/Recurso`).
3. **Destilar** → escreva conceito com suas palavras (template `Conceito`), ligue com `[[links]]`.
4. **Aplicar** → registre experimento/projeto.
5. **Revisar** → Dashboard semanal + flashcards (`#flashcard`).

## Convenções
- Frontmatter: `type`, `status` (`rascunho` → `em-progresso` → `maduro`), `tags`.
- Toda nota de conceito termina com seções **Relacionado** e **Fontes**.
- Flashcards: `pergunta::resposta` (Spaced Repetition).
- Nome de notas: claro, singular, sem data (exceto diário).
