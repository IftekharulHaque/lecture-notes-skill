---
description: Generate an Anki flashcard deck (CSV) from an existing lecture-notes document or its JSON spec. One card per Key Topic (term on the front, gloss on the back).
argument-hint: <path to notes .docx or notes .json>
---

# Lecture Notes → Anki Deck

On-demand companion to the **lecture-notes** skill. Given a notes document this
skill already produced, turn its Key Topics into an importable Anki deck. This
runs only when the user asks for it — a normal notes run never produces a deck.

## Input

The user names a source file (or you use the most recent one from this session):

- **A `.json` notes spec** (what `build_docx.py` consumed) — preferred, cleanest data.
- **A `.docx`** built by the skill — parsed for its Key Topics section as a fallback.

If neither is available (e.g. the notes were only shown as chat text), reconstruct
the JSON spec from the Key Topics you produced, then use that.

## Steps

1. Locate the source file the user means. If ambiguous, ask which notes to turn into a deck.
2. Ensure deps: `python -m pip install -r "${CLAUDE_PLUGIN_ROOT}/skills/lecture-notes/scripts/requirements.txt"`.
3. Run the exporter:
   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/skills/lecture-notes/scripts/anki_export.py" <source> <deck>.csv
   ```
   Name the CSV after the lecture (e.g. `software-testing-week4-anki.csv`).
4. Present the `.csv` and tell the user how to import it: in Anki, **File > Import**,
   set the field separator to **Comma**, map **Field 1 → Front** and **Field 2 → Back**.

## Notes

- The deck is header-less `Front,Back` rows — one card per Key Topic.
- If the source has no Key Topics, say so rather than emitting an empty deck.
