#!/usr/bin/env bash
# macOS/Linux setup: bash setup.sh
set -e
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
[ -f .env ] || { cp .env.example .env; echo "Created .env - open it and add your keys."; }
echo "Done. In VS Code: Ctrl+Shift+P > 'Python: Select Interpreter' > .venv, then run: python check_setup.py"
