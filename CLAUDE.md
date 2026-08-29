# Sanket Space (Obsidian Vault)

Always read the framework spec in `Docs/IMF Framework/` first, before doing any work in this vault. It defines the note types, folder roles, property schema, and template conventions this vault follows — treat it as the source of truth for how notes should be structured. The spec is split into five files, read in order:

- `00 Overview.md` — what IMF is, its purpose, the problem it solves
- `01 Principles & Concepts.md` — core principles and note-type definitions (Atomic Note, Concept Note, Source Note, MOC, Index, Home Note, Fluid Framework, Link)
- `02 Implementation.md` — the 5-stage workflow, folder architecture, note types, properties, and linking/tag/MOC/folder strategy
- `03 Templates.md` — the 5 note templates
- `04 Reference.md` — data model, a worked example, implementation rules, common mistakes, limitations, framework diagram

## Key conventions from that spec
- Note types: Concept, Source, MOC, Home, Project (optional), Daily (optional).
- Folders stage by *kind*, not topic: `+ Inbox` (capture), `Atlas` (concepts + MOCs), `Sources`, `Calendar`, `Efforts`, `Extras` (templates/attachments).
- Templates live in `Extras/Templates`.
- `status` is a metadata-menu Select field with fixed options: `Todo`, `In Progress`, `Done`. Never introduce other status values (e.g. `active`, `to-process`) — check `.obsidian/plugins/metadata-menu/data.json` `presetFields` before adding any new Select-backed property.
- Organize topics with MOCs and links, never folders or topical tags.
