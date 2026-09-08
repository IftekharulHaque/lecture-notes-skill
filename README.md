# Lecture Notes Skill

An agent skill for Claude Code and Codex CLI that turns a raw lecture/class/seminar transcript into clean, chronological study notes as a Word document (`.docx`) — with a key-topics summary and a to-do list of anything the lecturer assigned.

## What it does

- Reconstructs garbled auto-transcript text (dropped words, misheard terms) from context instead of reproducing errors.
- Cross-checks names, terms, and structure against any other course material you provide (slides, handouts, PDFs, syllabus, whiteboard photo).
- Produces a `.docx` with an overview, key topics, chronological notes, and a checklist of to-dos.
- Works for meeting-style recordings too, not just lectures.

See [`SKILL.md`](skills/lecture-notes/SKILL.md) for the full workflow and [`assets/example-output.md`](skills/lecture-notes/assets/example-output.md) for a worked example.

## Install

### Claude Code (plugin)

```
/plugin marketplace add IftekharulHaque/lecture-notes-skill
/plugin install lecture-notes@lecture-notes-skill
```

Update later with `/plugin update lecture-notes@lecture-notes-skill` (plugin installs are cache snapshots, not a live git checkout — a `git pull` won't touch them).

### Codex, or a script-based install

Directly, no clone needed:

```bash
curl -fsSL https://raw.githubusercontent.com/IftekharulHaque/lecture-notes-skill/main/install.sh | bash
```

That clones into `~/.local/share/lecture-notes-skill`. Or work from your own clone instead:

```bash
git clone https://github.com/IftekharulHaque/lecture-notes-skill.git
cd lecture-notes-skill
./install.sh
```

Either way, `~/.claude/skills/lecture-notes` and `~/.codex/skills/lecture-notes` are symlinked at the checkout — Codex reads the same `SKILL.md` layout as Claude Code, and `git pull` in the checkout updates both. Delete either symlink to uninstall for that agent.

## Usage

Paste or upload a transcript (optionally with slides/handouts/syllabus) and ask for notes, a summary, or a study guide — the skill triggers automatically.

## Development

The skill lives in `skills/lecture-notes/`. Its `.docx` builder and test are in `skills/lecture-notes/scripts/`:

```bash
python -m pip install -r skills/lecture-notes/scripts/requirements.txt
python skills/lecture-notes/scripts/test_build_docx.py   # -> "ok"
```

Releasing: bump `version` in **both** `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (they must match), then `claude plugin validate .` before pushing.

## License

MIT — see [LICENSE](LICENSE).
