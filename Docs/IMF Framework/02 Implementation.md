Part of the IMF Framework spec: [[00 Overview]] · [[01 Principles & Concepts]] · **02 Implementation** · [[03 Templates]] · [[04 Reference]]

# IMF Framework — Implementation

## Workflow

A 5-stage loop. Most captures only need stages 1–4; a map (stage 5) gets built only once a topic earns one.

| Stage          | Action                                                                                   | Where                               | Example                                  |
| -------------- | ---------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------- |
| **1. Capture** | Dump the raw idea, unorganized                                                           | New note in `+ Inbox`               | Clip "spacing effect improves retention" |
| **2. Process** | If it's from a source, summarize it in your own words + citation                         | `Source Note` template in `Sources` | Summarize a book chapter                 |
| **3. Distill** | Extract one idea into its own note                                                       | `Concept Note` template in `Atlas`  | Create `Spacing effect.md`               |
| **4. Connect** | Link it to related concept notes, with a note on *why*                                   | Wikilinks + backlinks pane          | Link spacing effect ↔ active recall      |
| **5. Map**     | Once a topic's notes cluster and get hard to hold in your head, build a map linking them | `MOC` template in `Atlas`           | Build `Learning MOC.md`                  |

## Folders

- `+ Inbox` — capture staging (temporary)
- `Atlas` — concept notes + MOCs (the core of the vault)
- `Sources` — source notes
- `Calendar` — daily/periodic notes (optional)
- `Efforts` — active projects (optional)
- `Extras` — templates, attachments, images

`Docs` and `Examples` sit outside this list on purpose — they're reference/meta folders (the spec itself, and a worked example), not knowledge topics, so the folder rule below doesn't apply to them.

Folders answer "what kind of note is this, where does it stage." Links and MOCs answer "what is it about." Never use a folder to answer the second question — that's the one rule that matters most here.

## Note types

**Required:** Concept, Source, MOC, Home (one).
**Optional:** Project/Effort, Daily.

Nothing else gets its own note type — a question, idea, or insight is a bullet inside an existing note, not a new file. Full breakdown in [[04 Reference]].

## Properties

All notes:

```yaml
---
type:            # concept | source | moc | project | daily
created: 2026-08-29
tags: []
aliases: []
---
```

Concept notes add nothing mandatory; optionally `up:` (parent MOC) and `related:`.

Source notes add:

```yaml
author:
title:
year:
url:
status:          # Todo | In Progress | Done
```

Project notes add:

```yaml
status:          # Todo | In Progress | Done
due:
```

Properties are for querying (status, type, dates). Relationships between ideas go in `[[links]]`, never in properties.

## Linking

Link every real conceptual relationship, and note *why* right next to the link — that's where the actual thinking happens. Don't link things that don't mean anything to each other.

- Concept note → its MOC(s) — a note can sit on more than one.
- Source note → the concept notes it fed.
- MOC → its member notes, curated and manually ordered.
- Home note → your main MOCs.

## Tags

Tags are weak and don't scale — use them for workflow state, never for topics (that's what MOCs are for).

- `#moc` or `type: moc` — pick one, not both — to find your maps.
- `status` property (`Todo | In Progress | Done`) for processing state — not a tag.
- At most one or two "entry point" tags for a cross-cutting theme that doesn't deserve a map yet.

Avoid tag hierarchies (`#topic/subtopic`) and status-as-tag sprawl (`#wip #done`) — both just rebuild folders with extra steps.

## MOCs

Create one at the point a topic's notes (~5+) get hard to hold in your head — not before. Keep 5–15 main MOCs; past that they stop being a map and start being clutter. They live in `Atlas`, can link out to `Efforts`/`Calendar`, and can nest into sub-MOCs under the Home note. Order and curate the links by hand — that curation *is* the thinking. (Dataview/Bases can auto-generate a MOC once a topic's structure is well understood and stable — optional, and not a replacement for a hand-built map while you're still figuring the topic out.)
