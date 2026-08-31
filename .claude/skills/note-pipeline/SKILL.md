---
name: note-pipeline
description: Runs the vault note workflow — note-writer, then the linter, then note-reviewer — for any request to capture, process, distill, connect, or map vault content. Use whenever the user wants non-trivial content added to or restructured in this vault, instead of doing the work directly.
---

# Note Pipeline

## Steps

1. **Write** — call `note-writer` with the raw input and what the user asked for. It decides stage, note type, folder, atomicity, links, and MOC timing, and creates/edits the files itself. It reports what it did and what it decided against.

2. **Lint** — run `python .claude/lint-vault.py`. This is deterministic; don't skip it even if the writer's report looks clean.

3. **Review** — call `note-reviewer` with the writer's report and the linter output. It re-reports the linter results and adds judgment on atomicity and over-engineering.

4. **Resolve findings**:
   - Any linter ERROR or reviewer "needs fix" → send back to `note-writer` to correct, then confirm the specific fix — no need to re-run the whole review.
   - Any "needs justification" or open question → send back to `note-writer` for an answer. A real justification gets added to the note (e.g. a `why` next to a link). If the answer reveals the call was wrong, have it revise the files.
   - Don't loop more than twice on the same finding — surface it to the user after that.

5. **Report to the user**: files created/changed, a one-line verdict per note, and any unresolved findings. Don't dump full transcripts.

## When to skip

A trivial edit (typo fix, one already-obvious link) doesn't need this — just do it directly.
