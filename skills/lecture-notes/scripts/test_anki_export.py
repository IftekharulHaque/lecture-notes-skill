#!/usr/bin/env python3
"""Self-check for anki_export.py. Run: python test_anki_export.py

Covers both input paths (JSON spec and parsed .docx) and the CSV shape.
Assert-only, no framework.
"""
import csv
import os
import tempfile

from build_docx import build
from anki_export import cards_from_spec, cards_from_docx, write_csv

SPEC = {
    "title": "Test Lecture",
    "key_topics": [
        {"term": "Stub", "gloss": "canned data"},
        {"term": "Mock", "gloss": "asserts calls"},
        {"term": "", "gloss": "dropped — no term"},
    ],
    "notes": [{"type": "paragraph", "text": "body"}],
    "todos": [],
}


def test_cards_from_spec_skips_empty_terms():
    cards = cards_from_spec(SPEC)
    assert cards == [("Stub", "canned data"), ("Mock", "asserts calls")], cards


def test_docx_roundtrip_matches_spec():
    with tempfile.TemporaryDirectory() as d:
        docx_path = build(SPEC, os.path.join(d, "n.docx"))
        cards = cards_from_docx(docx_path)
    assert ("Stub", "canned data") in cards, cards
    assert ("Mock", "asserts calls") in cards, cards


def test_write_csv_shape():
    with tempfile.TemporaryDirectory() as d:
        out = write_csv([("Stub", "canned data")], os.path.join(d, "deck.csv"))
        with open(out, newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
    assert rows == [["Stub", "canned data"]], rows  # header-less, 2 cols


if __name__ == "__main__":
    test_cards_from_spec_skips_empty_terms()
    test_docx_roundtrip_matches_spec()
    test_write_csv_shape()
    print("ok")
