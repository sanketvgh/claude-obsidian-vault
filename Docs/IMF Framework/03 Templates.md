Part of the IMF Framework spec: [[00 Overview]] · [[01 Principles & Concepts]] · [[02 Implementation]] · **03 Templates** · [[04 Reference]]

# IMF Framework — Templates

## 15. Templates

Directly-usable Obsidian Markdown templates for the justified note types. Use the core Templates plugin, or Templater for `{{date}}` variables and prompts. Stored in `Extras/Templates`.

### 15.1 Concept Note

```markdown
---
type: concept
created: {{date:YYYY-MM-DD}}
tags: []
aliases: []
up: 
related: 
---
# {{title}}

> One-sentence claim (the atomic idea in your own words).

## Elaboration
- 

## Connections
- Relates to [[ ]] because …
- Contrasts with [[ ]] because …

## Sources
- [[ ]]
```

### 15.2 Source Note

```markdown
---
type: source
created: {{date:YYYY-MM-DD}}
author: 
title: 
year: 
url: 
status: Todo
tags: []
---
# {{title}}

## Summary (in my own words)

## Key points
- 

## Notes → concepts to extract
- [ ] Create/append [[ ]]
```

### 15.3 MOC

```markdown
---
type: moc
created: {{date:YYYY-MM-DD}}
tags: [moc]
aliases: []
---
# {{title}} MOC

> What this map is about / the question it explores.

## Core concepts
- [[ ]]
- [[ ]]

## Open questions
- 

## Related maps
- [[ ]]
```

### 15.4 Home Note

```markdown
---
type: home
created: {{date:YYYY-MM-DD}}
---
# Home

## Main Maps
- [[ ]] 
- [[ ]]

## Currently active
- [[ ]]

## Entry points
- Inbox: [[+ Inbox]]
```

### 15.5 Project/Effort Note (optional)

```markdown
---
type: project
created: {{date:YYYY-MM-DD}}
status: Todo
due: 
tags: []
---
# {{title}}

## Outcome / definition of done

## Tasks
- [ ] 

## Relevant notes
- [[ ]]
```

---

Next: [[04 Reference]]
