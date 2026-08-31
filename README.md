# Claude Obsidian Vault

An Obsidian starter vault with a Claude Code toolchain that enforces its own note rules: two agents, a skill, and a deterministic linter.

Notes are atomic, connected by links rather than topic folders. Folders answer *what kind* of note something is; links and MOCs answer *what it's about*.

## What's here

```
CLAUDE.md              wires the rules and the pipeline into Claude Code
.claude/
  rules/vault.md       note types, folders, properties, linking, MOC timing
  rules/note-writing.md  style and structure; loads whenever a note is touched
  skills/note-pipeline/  write -> lint -> review -> resolve
  agents/note-writer.md    makes the judgment calls and writes the files
  agents/note-reviewer.md  checks that judgment; runs the linter
  lint-vault.py        deterministic checker, stdlib only
Extras/Templates/      the six note templates
Concepts/ Sources/ Daily/ Projects/    empty, ready to use
```

## Note types

Six, each mapped to exactly one folder. The linter enforces it.

| Type      | Folder      |
| --------- | ----------- |
| `concept` | `Concepts/` |
| `moc`     | `Concepts/` |
| `source`  | `Sources/`  |
| `daily`   | `Daily/`    |
| `project` | `Projects/` |
| `home`    | vault root  |

There's no inbox — capture goes into a dated note in `Daily/`. A concept note's title states a claim ("Mock Tests as Diagnosis, Not Practice"), not a topic ("Mock Tests"). MOCs get built on a friction trigger, never on note count.

The full rules are in `.claude/rules/vault.md`, which Claude Code loads every session.

## The linter

```
python .claude/lint-vault.py
```

Stdlib only, exits 1 on any error. It checks frontmatter, legal `type`/`status`, the type-to-folder mapping, property schema and order, leftover template placeholders, and dangling links. It warns on concept notes with no outgoing links.

Two things it reads live rather than hardcoding: the property schema comes from `Extras/Templates/`, and the legal `type` values come from the metadata-menu config. Edit a template and the rule moves with it.

Anything mechanical belongs to the linter. Atomicity and over-engineering can't be linted, which is why `note-reviewer` exists and why it surfaces findings instead of silently fixing them.

## Setup

1. Open this folder as a vault in Obsidian.
2. **Settings → Community plugins** and install **Metadata Menu** — it's what turns `type` and `status` into dropdowns. The config in `.obsidian/plugins/metadata-menu/data.json` is already set up; it just needs the plugin installed to take effect.
3. Open the folder in Claude Code. It reads `CLAUDE.md` automatically.

Python 3 is needed only for the linter. Everything else works as a plain Obsidian vault.
