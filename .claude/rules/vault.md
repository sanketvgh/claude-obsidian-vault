# Vault Rules

## Note types and folders
- `concept` → `Concepts/`
- `moc` → `Concepts/`
- `source` → `Sources/`
- `daily` → `Daily/`
- `project` → `Projects/`
- `home` → vault root
Only these six types exist. Folders answer *what kind*; links and MOCs answer *what about*. Never file by topic.

## Properties
Read `Extras/Templates/*.md` for the exact current property set and order per type — that is the source of truth, not this file. Don't add or drop properties the template doesn't have.

## Select fields
`type` and `status` are metadata-menu Select fields (see `.obsidian/plugins/metadata-menu/data.json` presetFields). Legal `type`: concept, source, moc, daily, project, home. Legal `status`: Todo, In Progress, Done. Never introduce another value for either without adding it there first.

## Naming
A concept note's title states a claim, not a topic ("Mock Tests as Diagnosis, Not Practice", not "Mock Tests"). Topic-labelled material is reference, not a concept.

## Reference material
Tables, figures, links, citations — anything you look up rather than think with — lives in a source note or a property. Never in a concept note.

## MOCs
Build only on a friction trigger: you went looking for something and couldn't find it, or you've re-explained the same relationship three times. Never build on note count. First line must state the question the MOC answers. Keep total MOCs under ~15.

## Workflow stages
1. **Capture** — raw input into today's daily note in `Daily/`.
2. **Process** — turn a source into a source note.
3. **Distill** — pull one idea into a concept note.
4. **Connect** — link concepts to each other.
5. **Map** — build/update a MOC, only on a friction trigger.
6. **Output** — use the notes for something. No new folder or note type. A cluster with no downstream output is a signal to prune, not grow.

## Links
Inline in the prose where the relationship arises, with the reason stated next to the link. Relationships live in links, never in properties.

## Atomicity
One idea per note. Notes accumulate; they are never "finished."

## What is not a note
Questions, ideas, and insights are bullets inside an existing note, not new files.

## Tags
Workflow state only (e.g. capture status). Never topics.

## Maintenance
`reviewed:` is a date property marking staleness. Deleting a note is a success, not a failure — pruning is a first-class action.

## Templates
`Extras/Templates/` is the single source of truth for note shape (frontmatter + title). Body structure is chosen per note per `.claude/rules/note-writing.md`, never prescribed by the template.
