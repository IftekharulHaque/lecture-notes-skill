#!/usr/bin/env python3
"""Turn lecture notes into an Anki-importable flashcard deck (CSV).

Input is either the JSON notes spec that build_docx.py consumes (preferred —
clean structured data) or the built .docx (parsed as a fallback, since that's
the artifact that actually gets saved). Output is a header-less CSV of
`Front,Back` rows: one card per Key Topic (Front = term, Back = gloss).

Usage:
    python anki_export.py notes.json  deck.csv
    python anki_export.py notes.docx  deck.csv

Import into Anki: File > Import, field separator Comma, map Field 1 -> Front,
Field 2 -> Back.
"""
import csv
import sys


def cards_from_spec(spec):
    """[(front, back), ...] from a build_docx JSON spec's key_topics."""
    out = []
    for t in spec.get("key_topics") or []:
        term = (t.get("term") or "").strip()
        if term:
            out.append((term, (t.get("gloss") or "").strip()))
    return out


def cards_from_docx(path):
    """[(front, back), ...] by reading the Key Topics bullets out of a .docx.

    Key Topics render as `List Bullet` paragraphs of `Term — gloss` (em dash),
    sitting between the "Key Topics" heading and the next heading.
    """
    from docx import Document

    doc = Document(path)
    out = []
    in_section = False
    for p in doc.paragraphs:
        style = p.style.name
        if style.startswith("Heading"):
            in_section = p.text.strip().lower() == "key topics"
            continue
        if in_section and style == "List Bullet" and p.text.strip():
            term, _, gloss = p.text.partition(" — ")
            out.append((term.strip(), gloss.strip()))
    return out


def load_cards(in_path):
    if in_path.lower().endswith(".json"):
        import json

        with open(in_path, encoding="utf-8") as f:
            return cards_from_spec(json.load(f))
    if in_path.lower().endswith(".docx"):
        return cards_from_docx(in_path)
    sys.exit(f"unsupported input (need .json or .docx): {in_path}")


def write_csv(cards, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(cards)
    return out_path


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: anki_export.py <notes.json|notes.docx> <deck.csv>")
    cards = load_cards(sys.argv[1])
    if not cards:
        sys.exit("no Key Topics found — nothing to export")
    print(f"{len(cards)} cards -> {write_csv(cards, sys.argv[2])}")


if __name__ == "__main__":
    main()
