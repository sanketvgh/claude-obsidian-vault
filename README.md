# IMF Obsidian Template

A starter Obsidian vault implementing the **IMF Framework** (Index, Maps of Content, Fluid Frameworks) — atomic notes, source notes, MOCs, and one Home note, connected by links instead of topic folders. Comes with a `CLAUDE.md` so it works out of the box with [Claude Code](https://claude.com/claude-code).

## What's here

- `CLAUDE.md` — points Claude Code at the spec below before it touches anything in this vault
- `Docs/IMF Framework/` — the full spec: definitions, workflow, folder/tag/MOC rules, templates, data model
- `Examples/Coffee Brewing/` — a fully worked example (fictional) showing every note type populated and linked together
- `Extras/Templates/` — the 5 note templates, wired into Obsidian's core Templates plugin
- `+ Inbox`, `Atlas`, `Sources`, `Calendar`, `Efforts` — empty, ready to use (each has a `.gitkeep` so the folder survives the clone)

## Setup

1. Open this folder as a vault in Obsidian.
2. Go to **Settings → Community plugins** and install **Metadata Menu** (required — it's what turns `status`/`type` into dropdowns; the settings are already configured in `.obsidian/plugins/metadata-menu/data.json`, they just need the plugin installed to take effect).
3. Read `Docs/IMF Framework/00 Overview.md` to start, or open this folder in Claude Code — it reads `CLAUDE.md` first automatically.
4. Delete `Examples/` once you've read through it, or keep it around as a live reference.
