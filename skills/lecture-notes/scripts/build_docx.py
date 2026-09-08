#!/usr/bin/env python3
"""Build a styled lecture-notes .docx from a JSON spec.

Deterministic Word-document builder so the skill doesn't re-derive python-docx
styling from scratch every run. Feed it the notes as structured JSON; it applies
real Word styles (Heading 1/2/3, List Bullet, checkbox glyphs) and embeds images
with captions.

Usage:
    python build_docx.py notes.json out.docx

Spec shape (see SKILL.md "Output template"):
    {
      "title": "Requirements Engineering — Lecture 3",
      "date": "October 2025",                      # optional
      "overview": "2-4 sentence paragraph.",
      "key_topics": [
        {"term": "Verification", "gloss": "did we build it right?"}
      ],
      "notes": [                                    # ordered blocks
        {"type": "heading", "level": 2, "text": "Verification vs validation"},
        {"type": "paragraph", "text": "..."},
        {"type": "bullets", "items": ["a", "b"]},
        {"type": "image", "path": "slide4.png", "caption": "Diagram (slide 4)"}
      ],
      "todos": ["Read chapter 6 before next class"]  # [] renders the no-items line
    }

Only `title` is required; every other field is optional and skipped when absent.
"""
import json
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches

CHECKBOX = "☐ "  # Word has no native checkbox run; a glyph is the honest fallback.
PAGE_WIDTH_IN = 6.0   # ponytail: fixed 6in usable width (US Letter, 1in margins); expose if page size varies.


def build(spec, out_path):
    doc = Document()

    doc.add_heading(spec["title"], level=1)
    if spec.get("date"):
        p = doc.add_paragraph()
        p.add_run(spec["date"]).italic = True

    if spec.get("overview"):
        doc.add_heading("Overview", level=2)
        doc.add_paragraph(spec["overview"])

    topics = spec.get("key_topics") or []
    if topics:
        doc.add_heading("Key Topics", level=2)
        for t in topics:
            p = doc.add_paragraph(style="List Bullet")
            p.add_run(t["term"]).bold = True
            if t.get("gloss"):
                p.add_run(f" — {t['gloss']}")

    blocks = spec.get("notes") or []
    if blocks:
        doc.add_heading("Notes", level=2)
        for b in blocks:
            _add_block(doc, b)

    doc.add_heading("To-Dos", level=2)
    todos = spec.get("todos") or []
    if todos:
        for item in todos:
            doc.add_paragraph(CHECKBOX + item)
    else:
        doc.add_paragraph("No action items mentioned in this lecture.")

    doc.save(out_path)
    return out_path


def _add_block(doc, b):
    kind = b.get("type")
    if kind == "heading":
        doc.add_heading(b["text"], level=int(b.get("level", 3)))
    elif kind == "paragraph":
        doc.add_paragraph(b["text"])
    elif kind == "bullets":
        for item in b.get("items", []):
            doc.add_paragraph(item, style="List Bullet")
    elif kind == "image":
        doc.add_picture(b["path"], width=Inches(PAGE_WIDTH_IN))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        if b.get("caption"):
            cap = doc.add_paragraph()
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cap.add_run(b["caption"]).italic = True
    else:
        raise ValueError(f"unknown note block type: {kind!r}")


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: build_docx.py notes.json out.docx")
    with open(sys.argv[1], encoding="utf-8") as f:
        spec = json.load(f)
    print(build(spec, sys.argv[2]))


if __name__ == "__main__":
    main()
