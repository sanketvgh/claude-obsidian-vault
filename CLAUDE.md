# Obsidian Vault

Vault rules (note types, folders, properties, linking, MOC timing) live in `.claude/rules/vault.md` and load automatically every session.

## Working in this vault
For any non-trivial request to capture, process, distill, connect, or map content (deciding note type, folder, atomicity, links, or MOC timing involves a judgment call), use the `note-pipeline` skill instead of editing vault files directly. It runs:
- `note-writer` — decides stage/note type/folder/atomicity/links/MOC timing and writes the files
- `python .claude/lint-vault.py` — deterministic schema/folder/link check
- `note-reviewer` — reports the linter output and interrogates atomicity and over-engineering

Trivial edits (typo fixes, an already-obvious single link) can be done directly — skip the pipeline for those.

Writing style and structure rules live in `.claude/rules/note-writing.md` and load automatically whenever a note file is touched. Notes must read like the user's own writing, not generated text.

## Folders
`Concepts` (concepts + MOCs), `Sources`, `Daily` (capture, via dated daily notes), `Projects`, `Extras` (templates/attachments).
