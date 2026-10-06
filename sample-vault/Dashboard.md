---
tags: [dashboard]
---
# 🧠 Dashboard — Segundo Cérebro de AI Engineering

> Requer plugin **Dataview** (e opcionalmente **Tasks**). Veja [[Como usar este vault]].

## Navegação
- [[01-Roadmap/Roadmap AI Engineer|Roadmap]] · [[01-Roadmap/Plano 90 dias|Plano 90 dias]]
- [[02-Conceitos/MOC - AI Engineering|Conceitos]] · [[03-Projetos/MOC - Projetos|Projetos]]
- [[04-Recursos/MOC - Recursos|Recursos]] · [[06-Carreira/MOC - Carreira|Carreira]]

## 📥 Inbox (processar)
```dataview
LIST FROM "00-Inbox" SORT file.ctime DESC
```

## 🌱 Conceitos por maturidade
```dataview
TABLE status, file.mtime AS "Atualizado"
FROM "02-Conceitos"
WHERE type = "conceito"
SORT status ASC, file.name ASC
```

## 🚧 Projetos ativos
```dataview
TABLE stack, status
FROM "03-Projetos"
WHERE type = "projeto" AND status != "concluído"
```

## 📚 Fila de leitura / estudo
```dataview
TABLE tipo, prioridade, status
FROM "04-Recursos"
WHERE type = "recurso" AND status != "concluído"
SORT prioridade ASC
```

## 📝 Notas recentes
```dataview
TABLE file.mtime AS "Modificado"
FROM -"99-Templates" AND -"05-Diario"
SORT file.mtime DESC
LIMIT 10
```

## ✅ Tarefas abertas
```dataview
TASK
FROM -"99-Templates"
WHERE !completed
LIMIT 20
```

## 🔁 Conceitos para revisar (status = rascunho)
```dataview
LIST
FROM "02-Conceitos"
WHERE status = "rascunho"
```
