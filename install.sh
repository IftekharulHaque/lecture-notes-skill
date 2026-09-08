#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/IftekharulHaque/lecture-notes-skill.git"
CLAUDE_DIR="$HOME/.claude/skills/lecture-notes"
CODEX_DIR="$HOME/.codex/skills/lecture-notes"
SCRIPT_PATH="${BASH_SOURCE[0]:-}"

if [ -n "$SCRIPT_PATH" ] && [ -f "$(dirname "$SCRIPT_PATH")/SKILL.md" ]; then
  # Run from inside a cloned checkout: use it as the source, git pull keeps it fresh.
  SRC_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
else
  # Run standalone (e.g. curl | bash): clone once into the Claude slot, use that as source.
  mkdir -p "$(dirname "$CLAUDE_DIR")"
  if [ ! -e "$CLAUDE_DIR" ]; then
    git clone -q "$REPO_URL" "$CLAUDE_DIR"
  fi
  SRC_DIR="$CLAUDE_DIR"
fi

for skill_dir in "$CLAUDE_DIR" "$CODEX_DIR"; do
  [ "$skill_dir" = "$SRC_DIR" ] && continue
  mkdir -p "$(dirname "$skill_dir")"
  if [ -e "$skill_dir" ] || [ -L "$skill_dir" ]; then
    echo "Already exists: $skill_dir (remove it first to reinstall)"
    continue
  fi
  ln -s "$SRC_DIR" "$skill_dir"
  echo "Installed: $skill_dir -> $SRC_DIR"
done

[ "$SRC_DIR" = "$CLAUDE_DIR" ] && echo "Installed: $CLAUDE_DIR"
