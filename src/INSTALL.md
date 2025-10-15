# ELPM Installation Guide

## Quick Start

### Linux / macOS

```bash
# 1. Navigate to the src directory
cd /path/to/elpm-desktop/src

# 2. Make the launcher executable (Linux/macOS only)
chmod +x run_elpm.sh

# 3. Run the launcher
./run_elpm.sh
```

### Windows

```cmd
# 1. Navigate to the src directory
cd C:\path\to\elpm-desktop\src

# 2. Run the launcher
run_elpm.bat
```

## Manual Installation

### Prerequisites

- **Python 3.8 or higher** (Python 3.10+ recommended)
- **pip** (Python package installer)

### Step 1: Check Python Installation

```bash
# Linux/macOS
python3 --version

# Windows
python --version
```

You should see something like `Python 3.10.x` or higher.

### Step 2: Install PyQt6

```bash
# Linux/macOS
pip3 install PyQt6

# Windows
pip install PyQt6
```

### Step 3: Verify Installation

```bash
# Navigate to the src directory
cd /path/to/elpm-desktop/src

# Run the test script
python3 test_imports.py
```

You should see all checks pass with ✓ marks.

### Step 4: Run ELPM

```bash
# Linux/macOS
python3 elpm_main.py

# Windows
python elpm_main.py
```

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'PyQt6'"

**Solution:**
```bash
# Ensure PyQt6 is installed
pip3 install PyQt6

# If using a virtual environment, make sure it's activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Issue: "ModuleNotFoundError: No module named 'gui'" or "No module named 'models'"

**Solution:**
Make sure you're in the correct directory:

```bash
# Check your current directory
pwd  # Linux/macOS
cd   # Windows

# Should be: /path/to/elpm-desktop/src
# Navigate to the correct location
cd /path/to/elpm-desktop/src
```

### Issue: Application window is tiny or huge (DPI scaling issues)

**Solution for Linux/macOS:**
```bash
export QT_AUTO_SCREEN_SCALE_FACTOR=1
python3 elpm_main.py
```

**Solution for Windows:**
- Right-click `elpm_main.py` → Properties → Compatibility
- Check "Override high DPI scaling behavior"
- Select "Application" from dropdown

### Issue: "AttributeError" or other Python errors

**Solution:**
1. Make sure you have the latest version of all files
2. Delete any `__pycache__` directories:
   ```bash
   find . -type d -name "__pycache__" -exec rm -r {} +  # Linux/macOS
   ```
3. Try running again

### Issue: Permission denied (Linux/macOS)

**Solution:**
```bash
# Make sure the scripts have execute permissions
chmod +x run_elpm.sh
chmod +x elpm_main.py
```

## Virtual Environment Setup (Recommended)

Using a virtual environment keeps your project dependencies isolated:

### Linux/macOS

```bash
# Navigate to project directory
cd /path/to/elpm-desktop/src

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install PyQt6

# Run ELPM
python elpm_main.py

# When done, deactivate
deactivate
```

### Windows

```cmd
# Navigate to project directory
cd C:\path\to\elpm-desktop\src

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install PyQt6

# Run ELPM
python elpm_main.py

# When done, deactivate
deactivate
```

## System Requirements

### Minimum Requirements
- **OS**: Linux, macOS 10.13+, Windows 10+
- **Python**: 3.8+
- **RAM**: 512 MB
- **Disk Space**: 100 MB

### Recommended Requirements
- **OS**: Linux (Ubuntu 20.04+), macOS 11+, Windows 10/11
- **Python**: 3.10+
- **RAM**: 1 GB
- **Disk Space**: 200 MB
- **Display**: 1400×800 or higher resolution

## Optional: Adding Real System Monitoring

To add real system process monitoring capabilities:

```bash
# Install psutil for actual process data
pip3 install psutil

# Then modify models/process_model.py to use real data
# See README_PYQT.md for implementation examples
```

## Development Setup

For development with auto-reload and debugging:

```bash
# Install development dependencies
pip3 install PyQt6 psutil black pylint

# Run with Python debugger
python3 -m pdb elpm_main.py
```

## Getting Help

If you encounter issues:

1. Check this installation guide
2. Read the troubleshooting section in `README_PYQT.md`
3. Verify all files are present and not corrupted
4. Check Python and PyQt6 versions
5. Try running in a fresh virtual environment

## Next Steps

After successful installation:

1. Read `README_PYQT.md` for usage instructions
2. Explore the application's features
3. Customize the theme in `gui/styles.py`
4. Add real process monitoring with `psutil`
5. Implement signal controls for process management

---

**Version**: 1.0  
**Last Updated**: 2025-10-08
