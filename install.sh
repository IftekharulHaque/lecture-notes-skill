#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/IftekharulHaque/lecture-notes-skill.git"
SKILL_DIR="$HOME/.claude/skills/lecture-notes"
SCRIPT_PATH="${BASH_SOURCE[0]:-}"

mkdir -p "$(dirname "$SKILL_DIR")"

if [ -e "$SKILL_DIR" ] || [ -L "$SKILL_DIR" ]; then
  echo "Already exists: $SKILL_DIR (remove it first to reinstall)"
  exit 1
fi

if [ -n "$SCRIPT_PATH" ] && [ -f "$(dirname "$SCRIPT_PATH")/SKILL.md" ]; then
  # Run from inside a cloned checkout: symlink it in, git pull keeps it fresh.
  SRC_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
  ln -s "$SRC_DIR" "$SKILL_DIR"
  echo "Installed: $SKILL_DIR -> $SRC_DIR"
else
  # Run standalone (e.g. curl | bash): clone straight into the skills dir.
  git clone "$REPO_URL" "$SKILL_DIR"
  echo "Installed: $SKILL_DIR"
fi
