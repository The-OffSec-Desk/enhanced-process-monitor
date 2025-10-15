# ELPM Quick Start Guide

## Installation (30 seconds)

### Option 1: Automated Launcher (Easiest)

**Linux/macOS:**
```bash
cd /path/to/elpm-desktop/src
chmod +x run_elpm.sh
./run_elpm.sh
```

**Windows:**
```cmd
cd C:\path\to\elpm-desktop\src
run_elpm.bat
```

### Option 2: Manual (If launcher doesn't work)

```bash
# 1. Install PyQt6
pip install PyQt6

# 2. Navigate to src directory
cd /path/to/elpm-desktop/src

# 3. Run ELPM
python elpm_main.py
```

## Basic Usage

### 1. View Processes
- **Processes tab** shows all running processes
- Click any row to see detailed information
- Use search bar to filter processes

### 2. Monitor Resources
- **Graphs tab** shows real-time CPU and Memory usage
- Updates every 2 seconds automatically

### 3. Filter Processes
- **Sort by**: CPU%, Memory%, PID, or Name
- **Checkboxes**: Root only, Hide kernel threads, Auto-refresh

### 4. Control Processes (Visual only - not functional yet)
- **SIGTERM** (Green): Graceful termination
- **SIGKILL** (Red): Force kill
- **SIGSTOP** (Yellow): Pause process
- **SIGCONT** (Cyan): Resume process

## Keyboard Shortcuts

- `Ctrl+F` or `/` - Focus search bar
- `Ctrl+R` - Refresh (when auto-refresh is off)
- `Ctrl+W` or `Ctrl+Q` - Close application
- `Arrow Keys` - Navigate process list
- `Tab` - Switch between tabs

## Color Meanings

| Color        | Meaning    |
|--------------|------------|
| 🔵 Cyan      |  (#00d4ff) | Primary actions, selected items |
| 🔴 Red       |  (#ff6b6b) | Critical (high CPU/memory >70%, zombie processes) |
| 🟢 Green     |  (#51cf66) | Running processes, normal operation |
| 🟡 Yellow    |  (#ffd93d) | Warning, stopped processes |
| 🔵 Light Cyan|  (#4ecdc4) | Sleeping processes |

## Common Tasks

### Find a Specific Process
1. Type process name or PID in search bar
2. Process list filters automatically
3. Click on process to see details

### Monitor High CPU Processes
1. Click "Sort by" dropdown
2. Select "CPU%"
3. Processes sorted by CPU usage (highest first)

### Check Memory Usage
1. Go to **Graphs** tab
2. View real-time memory graph
3. Check stats panel for average/max/min values

### View Process Details
1. Click any process in the table
2. Right panel shows:
   - Process information (PID, status, user)
   - Resource usage (CPU, memory, threads)
   - Timing information
   - Full command line
   - Working directory
   - Open files and network connections

## Troubleshooting

### "ModuleNotFoundError: No module named 'PyQt6'"
```bash
pip install PyQt6
```

### "No module named 'gui'"
```bash
"""
ELPM - Enhanced Linux Process Monitor
PyQt6 Desktop Application
Main application entry point
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from gui.main_window import MainWindow


def main():
    """Initialize and run the ELPM application"""
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    app = QApplication(sys.argv)
    app.setApplicationName("ELPM")
    app.setApplicationVersion("1.0")

    # ✅ Global app icon
    app.setWindowIcon(QIcon("/home/gr3ytrac3/Pictures/desktop-images/ELPM.png"))
    
    # Set default application font
    font = QFont("Segoe UI", 9)
    app.setFont(font)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
# Make sure you're in the src directory
cd /path/to/elpm-desktop/src
python elpm_main.py
```

### Application doesn't start
```bash
# Test imports first
python test_imports.py

# Check Python version (need 3.8+)
python --version
```

## Next Steps

1. **Add real monitoring**: Install `psutil` for actual system data
   ```bash
   pip install psutil
   ```

2. **Customize theme**: Edit `gui/styles.py`

3. **Enable signal controls**: See `README_PYQT.md` for implementation

4. **Read full documentation**: See `README_PYQT.md` and `INSTALL.md`

---

Need help? Check `README_PYQT.md` for detailed documentation.
