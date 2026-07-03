#!/usr/bin/env bash
# run.sh — One-shot launch for the interactive resume app
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$SCRIPT_DIR/venv"

# Activate venv
if [ ! -d "$VENV" ]; then
  echo "❌ venv not found. Run: python -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
  exit 1
fi

source "$VENV/bin/activate"

echo "⚡ Starting Abhinav Prakash — Interactive Resume..."
streamlit run "$SCRIPT_DIR/app/main.py" \
  --server.port 8501 \
  --browser.serverAddress localhost \
  --theme.base dark
