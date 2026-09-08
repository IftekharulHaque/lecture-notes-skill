#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/IftekharulHaque/lecture-notes-skill.git"
# The skill itself lives in a subdirectory so the repo can double as a Claude plugin.
SKILL_SUBPATH="skills/lecture-notes"
SCRIPT_PATH="${BASH_SOURCE[0]:-}"

if [ -n "$SCRIPT_PATH" ] && [ -f "$(dirname "$SCRIPT_PATH")/$SKILL_SUBPATH/SKILL.md" ]; then
  # Run from inside a cloned checkout: use it as the source, git pull keeps it fresh.
  REPO_DIR="$(cd "$(dirname "$SCRIPT_PATH")" && pwd)"
else
  # Run standalone (e.g. curl | bash): clone once somewhere neutral, so removing one
  # agent's skill directory never leaves the other pointing at a deleted checkout.
  REPO_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/lecture-notes-skill"
  [ -d "$REPO_DIR" ] || git clone -q "$REPO_URL" "$REPO_DIR"
fi
SRC_DIR="$REPO_DIR/$SKILL_SUBPATH"

for skill_dir in "$HOME/.claude/skills/lecture-notes" "$HOME/.codex/skills/lecture-notes"; do
  mkdir -p "$(dirname "$skill_dir")"
  if [ -e "$skill_dir" ] || [ -L "$skill_dir" ]; then
    echo "Already exists: $skill_dir (remove it first to reinstall)"
    continue
  fi
  ln -s "$SRC_DIR" "$skill_dir"
  echo "Installed: $skill_dir -> $SRC_DIR"
done
