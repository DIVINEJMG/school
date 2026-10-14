#!/usr/bin/env bash
# Checks the tools this project needs and prints the next steps.
set -euo pipefail

if ! command -v git >/dev/null 2>&1; then
  echo "git is not installed. Install it from https://git-scm.com and run this script again." >&2
  exit 1
fi

echo "git $(git --version | awk '{print $3}') found."
echo "Setup complete. See README.md for the next steps."
