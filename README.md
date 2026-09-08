# Lecture Notes Skill

A Claude skill that turns a raw lecture/class/seminar transcript into clean, chronological study notes as a Word document (`.docx`) — with a key-topics summary and a to-do list of anything the lecturer assigned.

## What it does

- Reconstructs garbled auto-transcript text (dropped words, misheard terms) from context instead of reproducing errors.
- Cross-checks names, terms, and structure against any other course material you provide (slides, handouts, PDFs, syllabus, whiteboard photo).
- Produces a `.docx` with an overview, key topics, chronological notes, and a checklist of to-dos.
- Works for meeting-style recordings too, not just lectures.

See [`SKILL.md`](SKILL.md) for the full workflow and [`assets/example-output.md`](assets/example-output.md) for a worked example.

## Install

```bash
git clone https://github.com/IftekharulHaque/lecture-notes-skill.git
cd lecture-notes-skill
./install.sh
```

Symlinks this folder into `~/.claude/skills/lecture-notes`. `git pull` later to update.

## Usage

Paste or upload a transcript (optionally with slides/handouts/syllabus) and ask for notes, a summary, or a study guide — the skill triggers automatically.

## License

MIT — see [LICENSE](LICENSE).
