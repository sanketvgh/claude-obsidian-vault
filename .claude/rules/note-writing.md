---
paths:
  - "Concepts/**/*.md"
  - "Sources/**/*.md"
  - "Daily/**/*.md"
  - "Projects/**/*.md"
  - "Home.md"
---

# Note writing style

Notes are the user's own thinking, written by hand — not model output. Apply this to every note body, inside or outside the pipeline.

Cut on sight:
- Em-dashes as a crutch to bolt on a qualifier or reason ("X — which means Y"). Split into two sentences or use "because"/"so." One em-dash doing real parenthetical work is fine.
- Hedge-and-reveal voice: "not X, but really Y" / "it's not just A — it's B." State the claim directly.
- Stock AI transitions/intensifiers opening a sentence: "crucially," "importantly," "notably," "in essence," "ultimately," "fundamentally."
- Symmetrical triads ("X, Y, and — most importantly — Z"). Real notes are lumpy: some points get a clause, some a full sentence, some a fragment.
- Restating the question before answering it ("The reason phase 3 comes last is because..."). Just say the reason.

Write instead: short declaratives (fragments fine in lists); contractions ("doesn't," "can't"); concrete specifics (a number, a name) over abstract framing ("this has significant implications"); plain admissions of uncertainty ("not sure this is right, but—" not "it is worth noting that this claim remains contested").

Before finishing, read back every claim and bullet: would a person jotting this by hand phrase it this way, or does it sound generated? Rewrite anything that fails.

## Structure and formatting

Structure must be earned by the content, not applied by default and not banned by default. The template being blank means no prescribed shape — it doesn't mean no shape.

- **Prose is the default** for developing an argument. A note that makes one connected claim stays prose. Don't chop reasoning into bullets — bullets fragment an argument and hide the logic connecting the parts.
- **Bullets when the content is genuinely a list**: parallel items, enumerated options, steps, criteria. If the items don't share a shape, it isn't a list.
- **Tables when data has two or more dimensions**: score conversions, comparisons, option/tradeoff pairs. Never write tabular data as prose sentences.
- **Callouts for content that is a different *kind* than the body**, not for emphasis:
  - `> [!question]` — open questions the note leaves unresolved
  - `> [!example]` — a concrete illustration that supports but isn't part of the argument
  - `> [!warning]` — a caveat, limitation, or known failure mode
  - `> [!quote]` — source material in the author's own words
  - `> [!info]` / `> [!note]` — provenance, context, or an aside

  At most one or two callouts per note. A note that is mostly callouts has no body.
- **Headings only when a note genuinely has multiple sections.** A note under roughly 300 words almost never does. Never add a heading just to label a single paragraph.
- **Links stay inline** in the prose where the relationship comes up, with the reason attached — unchanged from the spec.

Same test as the rest of this file: every piece of structure has to justify itself. If removing a bullet list, callout, or heading would lose nothing, it wasn't earned.
