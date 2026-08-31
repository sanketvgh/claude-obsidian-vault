#!/usr/bin/env python3
"""Deterministic linter for this vault. Stdlib only.

Run from the vault root: python .claude/lint-vault.py
Exit code 1 if any ERROR is found; warnings alone exit 0.
"""
import os
import re
import sys
import json

VAULT_ROOT = os.getcwd()

EXCLUDE_DIRS = {".claude", ".obsidian", "Extras"}
LEGAL_STATUS = {"Todo", "In Progress", "Done"}

# Root markdown that documents the repo rather than being a note in it.
SKIP_FILES = {"CLAUDE.md", "README.md", "LICENSE.md", "CONTRIBUTING.md"}

TYPE_FOLDER = {
    "concept": "Concepts",
    "moc": "Concepts",
    "source": "Sources",
    "daily": "Daily",
    "project": "Projects",
    "home": None,  # vault root
}

TEMPLATE_MAP = {
    "concept": "New Concept.md",
    "moc": "New MOC.md",
    "source": "New Source.md",
    "daily": "New Daily.md",
    "project": "New Project.md",
    "home": "New Home.md",
}


def find_notes(root):
    notes = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        parts = [] if rel_dir == "." else rel_dir.split(os.sep)
        if parts and parts[0] in EXCLUDE_DIRS:
            dirnames[:] = []
            continue
        # prune excluded dirs from further descent
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            if rel in SKIP_FILES:
                continue
            notes.append(rel)
    return sorted(notes)


def parse_frontmatter(text):
    """Return (ordered list of (key, raw_value) pairs, body_text) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.DOTALL)
    if not m:
        return None, text
    fm_text = m.group(1)
    body = text[m.end():]
    pairs = []
    for line in fm_text.split("\n"):
        if not line.strip():
            continue
        if re.match(r"^\s", line):
            # continuation line (e.g. list item under a key) - skip, not a new key
            continue
        km = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if km:
            pairs.append((km.group(1), km.group(2)))
    return pairs, body


def get_legal_types(data_json_path):
    try:
        with open(data_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return None
    for pf in data.get("presetFields", []):
        if pf.get("name") == "type":
            vals = pf.get("options", {}).get("valuesList", {})
            return set(vals.values())
    return None


def strip_code_blocks(text):
    """Remove fenced code blocks so links inside them aren't checked."""
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


LINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def extract_links(body):
    clean = strip_code_blocks(body)
    return LINK_RE.findall(clean)


# Conceptual links only: excludes ![[embeds]] and asset targets. An embedded
# image is not a connection to another idea, so it must not clear the orphan check.
NOTE_LINK_RE = re.compile(r"(?<!!)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
ASSET_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".mp4", ".mp3", ".excalidraw")


def extract_note_links(body):
    clean = strip_code_blocks(body)
    return [t for t in NOTE_LINK_RE.findall(clean)
            if not t.strip().lower().endswith(ASSET_EXT)]


def load_templates(root):
    """Return {type: [prop_keys_in_order]}."""
    tpl_dir = os.path.join(root, "Extras", "Templates")
    schemas = {}
    for note_type, fname in TEMPLATE_MAP.items():
        path = os.path.join(tpl_dir, fname)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        pairs, _ = parse_frontmatter(text)
        if pairs is None:
            continue
        schemas[note_type] = [k for k, v in pairs]
    return schemas


def main():
    root = VAULT_ROOT
    legal_types = get_legal_types(os.path.join(root, ".obsidian", "plugins", "metadata-menu", "data.json"))
    if legal_types is None:
        legal_types = {"concept", "source", "moc", "project", "daily", "home"}

    schemas = load_templates(root)

    notes = find_notes(root)
    note_basenames = {}
    for rel in notes:
        base = os.path.splitext(os.path.basename(rel))[0]
        note_basenames.setdefault(base, []).append(rel)

    # collect image/asset files too, for embeds
    asset_names = set()
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        parts = [] if rel_dir == "." else rel_dir.split(os.sep)
        if parts and parts[0] in (".claude", ".obsidian"):
            dirnames[:] = []
            continue
        for fn in filenames:
            asset_names.add(fn)
            asset_names.add(os.path.splitext(fn)[0])

    errors = {}
    warnings = {}

    def err(rel, msg):
        errors.setdefault(rel, []).append(msg)

    def warn(rel, msg):
        warnings.setdefault(rel, []).append(msg)

    for rel in notes:
        full = os.path.join(root, rel)
        with open(full, "r", encoding="utf-8") as f:
            text = f.read()
        pairs, body = parse_frontmatter(text)

        if pairs is None:
            err(rel, "no frontmatter found")
            continue

        keys = [k for k, v in pairs]
        fm = dict(pairs)

        # type check
        if "type" not in fm:
            err(rel, "missing 'type' property")
            note_type = None
        else:
            note_type = fm["type"].strip()
            if note_type not in legal_types:
                err(rel, f"illegal type '{note_type}' (legal: {sorted(legal_types)})")

        # status check
        if "status" in fm:
            status_val = fm["status"].strip().strip('"').strip("'")
            if status_val and status_val not in LEGAL_STATUS:
                err(rel, f"illegal status '{status_val}' (legal: {sorted(LEGAL_STATUS)})")

        # folder check
        if note_type in TYPE_FOLDER:
            expected_folder = TYPE_FOLDER[note_type]
            actual_dir = os.path.dirname(rel)
            if expected_folder is None:
                if actual_dir != "":
                    err(rel, f"type '{note_type}' must live at vault root, found in '{actual_dir}'")
            else:
                top = actual_dir.split(os.sep)[0] if actual_dir else ""
                if top != expected_folder:
                    err(rel, f"type '{note_type}' must live in '{expected_folder}/', found in '{actual_dir}'")

        # schema match: same keys, same order
        if note_type in schemas:
            expected_keys = schemas[note_type]
            if keys != expected_keys:
                err(rel, f"property mismatch: expected {expected_keys}, got {keys}")

        # placeholders
        if re.search(r"\[\[\s*\]\]", body):
            err(rel, "leftover template placeholder '[[ ]]'")
        if re.search(r"^\s*-\s*$", body, re.MULTILINE):
            err(rel, "leftover empty bullet '- '")

        # dangling links
        for target in extract_links(body):
            target = target.strip()
            if not target:
                continue
            base = os.path.basename(target)
            base_noext = os.path.splitext(base)[0]
            if base_noext in note_basenames or base in asset_names or base_noext in asset_names:
                continue
            err(rel, f"dangling link [[{target}]]")

        # orphan concept warning
        if note_type == "concept":
            links = extract_note_links(body)
            if not links:
                warn(rel, "concept note has zero outgoing links")

    total_errors = sum(len(v) for v in errors.values())
    total_warnings = sum(len(v) for v in warnings.values())

    for rel in sorted(set(errors) | set(warnings)):
        print(f"\n{rel}")
        for msg in errors.get(rel, []):
            print(f"  ERROR: {msg}")
        for msg in warnings.get(rel, []):
            print(f"  WARNING: {msg}")

    print(f"\n--- Summary: {len(notes)} notes checked, {total_errors} errors, {total_warnings} warnings ---")

    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
