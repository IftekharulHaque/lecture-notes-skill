#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$HOME/.claude/skills/lecture-notes"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$(dirname "$SKILL_DIR")"

if [ -e "$SKILL_DIR" ] || [ -L "$SKILL_DIR" ]; then
  echo "Already exists: $SKILL_DIR (remove it first to reinstall)"
  exit 1
fi

ln -s "$SRC_DIR" "$SKILL_DIR"
echo "Installed: $SKILL_DIR -> $SRC_DIR"
