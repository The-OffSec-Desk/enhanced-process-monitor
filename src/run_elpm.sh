╰─ cat run_elpm.sh
#!/bin/bash

# ELPM Launcher Script
# This script helps run ELPM with proper environment setup

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script directory
cd "$SCRIPT_DIR"

echo "=========================================="
echo "  ELPM - Enhanced Linux Process Monitor  "
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✓ Found Python: $PYTHON_VERSION"
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
    echo "✓ Found Python: $PYTHON_VERSION"
else
    echo "✗ Python not found. Please install Python 3.8 or higher."
    exit 1
fi

# Check PyQt6
echo ""
echo "Checking PyQt6..."
if $PYTHON_CMD -c "import PyQt6" 2>/dev/null; then
    echo "✓ PyQt6 is installed"
else
    echo "✗ PyQt6 not found"
    echo ""
    echo "Installing PyQt6..."
    $PYTHON_CMD -m pip install PyQt6

    if [ $? -eq 0 ]; then
        echo "✓ PyQt6 installed successfully"
    else
        echo "✗ Failed to install PyQt6"
        echo "Please run: pip install PyQt6"
        exit 1
    fi
fi

# Check psutil
echo ""
echo "Checking psutil..."
if $PYTHON_CMD -c "import psutil" 2>/dev/null; then
    echo "✓ psutil is installed"
else
    echo "✗ psutil not found"
    echo ""
    echo "Installing psutil..."
    $PYTHON_CMD -m pip install psutil

    if [ $? -eq 0 ]; then
        echo "✓ psutil installed successfully"
    else
        echo "✗ Failed to install psutil"
        echo "Please run: pip install psutil"
        exit 1
    fi
fi

# Run the application
echo ""
echo "Starting ELPM..."
echo ""
$PYTHON_CMD elpm_main.py

# If it failed, suggest diagnostics
if [ $? -ne 0 ]; then
    echo ""
    echo "✗ Application failed to start"
    echo "Run diagnostics: python diagnose.py"
fi
