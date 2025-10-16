# ELPM Troubleshooting Guide

## Common Issues and Solutions

This guide covers common problems and their solutions. If you're experiencing an issue, find it below and follow the solution steps.

---


## ❌ ModuleNotFoundError: No module named 'PyQt6'

### Symptom
```
ModuleNotFoundError: No module named 'PyQt6'
```

### Cause
PyQt6 is not installed in your Python environment.

### Solution 1: Automated (Recommended)
```bash
# Linux/macOS
./run_elpm.sh

# Windows
run_elpm.bat
```

The launcher scripts will automatically install PyQt6 if missing.

### Solution 2: Manual
```bash
# Install PyQt6
pip install PyQt6

# Or for Python 3 specifically
pip3 install PyQt6

# Verify installation
pip list | grep PyQt6
```

### Solution 3: Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install PyQt6
pip install PyQt6

# Run ELPM
python elpm_main.py
```

### Verification
```bash
# Test if PyQt6 is available
python -c "import PyQt6; print('PyQt6 installed successfully')"
```

---

## ❌ ModuleNotFoundError: No module named 'gui'

### Symptom
```
ModuleNotFoundError: No module named 'gui'
```

### Cause
You're running the script from the wrong directory.

### Solution
```bash
# Check current directory
pwd  # Linux/macOS
cd   # Windows

# Navigate to the src directory
cd /path/to/elpm-desktop/src

# Verify you're in the right place
ls -la  # Should see: elpm_main.py, gui/, models/, etc.

# Now run
python elpm_main.py
```

### Alternative Solution
Add the src directory to Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/elpm-desktop/src"
python elpm_main.py
```

---

## ❌ Application Window is Too Small/Large (DPI Issues)

### Symptom
- Window appears tiny on high-DPI displays
- Window appears huge on low-DPI displays
- UI elements overlap or are cut off

### Solution 1: Environment Variable (Linux/macOS)
```bash
export QT_AUTO_SCREEN_SCALE_FACTOR=1
python elpm_main.py
```

### Solution 2: Windows Compatibility Settings
1. Right-click `elpm_main.py`
2. Properties → Compatibility
3. Check "Override high DPI scaling behavior"
4. Select "Application" from dropdown
5. Click OK

### Solution 3: Manual Scaling
Edit `elpm_main.py`:
```python
# Add before QApplication creation
import os
os.environ["QT_SCALE_FACTOR"] = "1.5"  # Adjust value as needed
```

---

## ❌ ImportError: cannot import name 'Process' from 'models'

### Symptom
```
ImportError: cannot import name 'Process' from 'models'
```

### Cause
Missing `__init__.py` files or corrupted model file.

### Solution
1. Verify file structure:
```bash
ls -la models/
# Should see:
# __init__.py
# process_model.py
```

2. Check `models/__init__.py` exists:
```bash
touch models/__init__.py  # Create if missing
```

3. Verify `models/process_model.py` contains the Process class:
```bash
grep "class Process" models/process_model.py
```

---

## ❌ QWidget: Must construct a QApplication before a QWidget

### Symptom
```
QWidget: Must construct a QApplication before a QWidget
```

### Cause
Trying to create widgets before QApplication is initialized.

### Solution
This should not happen with the provided code. If it does:

1. Verify you're using the original `elpm_main.py`
2. Check that you haven't modified the import order
3. Make sure `app = QApplication(sys.argv)` comes before `window = MainWindow()`

---

## ❌ Application Crashes on Startup (No Error Message)

### Symptom
- Application starts but immediately closes
- No error message visible
- Window flashes briefly

### Solution
Run from terminal to see error messages:
```bash
# Linux/macOS
cd /path/to/elpm-desktop/src
python3 elpm_main.py

# Windows
cd C:\path\to\elpm-desktop\src
python elpm_main.py
```

Look for error messages in the terminal output.

### Common Hidden Errors
1. **Missing font**: Install Consolas or Segoe UI fonts
2. **Graphics driver**: Update graphics drivers
3. **Qt platform**: Install Qt platform plugins

---

## ❌ Graphs Not Displaying/Blank Graphs

### Symptom
- Graph tabs show blank space
- No lines or grid visible
- "Graphs" tab appears empty

### Cause
QPainter issues or graphics driver problems.

### Solution 1: Update Graphics Drivers
Update your graphics card drivers to the latest version.

### Solution 2: Software Rendering
```bash
export QT_XCB_GL_INTEGRATION=none  # Linux
python elpm_main.py
```

### Solution 3: Check Python Version
```bash
python --version
# Must be 3.8 or higher
```

---

## ❌ Table Not Showing Process Data

### Symptom
- Process table is empty
- Headers visible but no rows
- Right panel shows no details

### Solution
Check if `populate_table()` is being called:
```bash
# Add debug print in gui/views/processes_view.py
def populate_table(self):
    print(f"Populating table with {len(self.filtered_processes)} processes")
    # ... rest of code
```


---

## ❌ Search Bar Not Filtering

### Symptom
- Typing in search bar does nothing
- All processes remain visible
- No filtering occurs

### Solution
1. Check that signal is connected (already done in code)
2. Verify you're in the Processes tab
3. Try clicking in the search bar before typing

### Debug
```bash
# Add to gui/widgets/top_bar.py
def on_search_text_changed(self, text):
    print(f"Search text changed to: {text}")  # Debug print
    self.search_changed.emit(text)
```

---

## ❌ Auto-Refresh Not Working

### Symptom
- Data doesn't update automatically
- Graphs don't animate
- Time doesn't change

### Solution
1. Check "Auto-refresh" checkbox is enabled
2. Verify timers are running:
```python
# Add to gui/main_window.py init_ui()
print(f"Refresh timer active: {self.refresh_timer.isActive()}")
print(f"Status timer active: {self.status_timer.isActive()}")
```

3. Check timer intervals:
```bash
# Should be 2000ms for refresh, 1000ms for status
```

---

## ❌ Application Freezes/Hangs

### Symptom
- Application becomes unresponsive
- Can't click buttons
- Must force quit

### Cause
- Infinite loop in code
- Blocking operation on main thread
- Memory leak

### Solution 1: Check CPU Usage
```bash
# Linux/macOS
top -p $(pgrep -f elpm_main)

# Windows
# Use Task Manager
```

### Solution 2: Run with Profiling
```bash
python -m cProfile -o profile.stats elpm_main.py
# Analyze profile.stats to find bottleneck
```

---

## ❌ Permission Denied Errors (Linux/macOS)

### Symptom
```
Permission denied: './run_elpm.sh'
```

### Solution
```bash
# Make script executable
chmod +x run_elpm.sh
chmod +x elpm_main.py

# Then run
./run_elpm.sh
```

---

## ❌ Colors Look Wrong/Theme Not Applied

### Symptom
- Default Qt theme instead of dark theme
- Colors are bright/light
- No cyan accents

### Cause
Stylesheet not being applied correctly.

### Solution
1. Check `gui/styles.py` exists:
```bash
ls -la gui/styles.py
```

2. Verify stylesheet is applied:
```python
# In gui/main_window.py
print(f"Stylesheet length: {len(MAIN_STYLES)}")  # Should be >1000
```

3. Force stylesheet reload:
```python
# Add to main_window.py
self.setStyleSheet("")  # Clear
self.setStyleSheet(MAIN_STYLES)  # Reapply
```

---

## Diagnostic Commands

### Full System Check
```bash
# Run this comprehensive check
python test_imports.py && \
python -c "import PyQt6; print('PyQt6 OK')" && \
python -c "from models.process_model import get_sample_processes; print(f'{len(get_sample_processes())} processes')" && \
echo "All checks passed!"
```

### Verify File Integrity
```bash
# Check all required files exist
ls -la elpm_main.py
ls -la gui/main_window.py
ls -la gui/styles.py
ls -la gui/views/processes_view.py
ls -la gui/views/graphs_view.py
ls -la models/process_model.py
```

### Check Python Environment
```bash
# Display environment info
python --version
pip list | grep PyQt
which python
echo $PYTHONPATH
```

---

## Getting More Help

If none of these solutions work:

### 1. Gather Information
```bash
# System info
python --version
pip list | grep PyQt
uname -a  # Linux/macOS
ver       # Windows

# Run with verbose errors
python -v elpm_main.py 2>&1 | tee error.log
```

### 2. Check Documentation
- [INSTALL.md](INSTALL.md) - Installation guide
- [README_PYQT.md](README_PYQT.md) - Full documentation
- [CHECKLIST.md](CHECKLIST.md) - Verification steps

### 3. Verify Installation
```bash
# Run the import test
python test_imports.py

# Check file structure
tree -L 3  # Linux/macOS
dir /s     # Windows
```

---

##  Known Issues (v1.0.1)

### Recovery Procedures

### Complete Reinstall
```bash
# 1. Remove virtual environment (if used)
rm -rf venv/

# 2. Reinstall PyQt6
pip uninstall PyQt6
pip install PyQt6

# 3. Clear Python cache
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete

# 4. Re-run application
python elpm_main.py
```

### Reset to Defaults
```bash
# Download fresh copy of files
# Or re-copy from original source
# All customizations will be lost!
```

---

**Last Updated**: 10-15-2025
**Version**: 1.0.0
**Status**: All major issues resolved

**Still having issues?** Check [INSTALL.md](INSTALL.md) or run `python test_imports.py`
