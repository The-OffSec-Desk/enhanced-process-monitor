#!/bin/bash

# ELPM Launcher Script (Flatpak version)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "  ELPM - Enhanced Linux Process Monitor  "
echo "=========================================="
echo ""

echo "Starting ELPM..."
python3 /app/bin/elpm_main.py

