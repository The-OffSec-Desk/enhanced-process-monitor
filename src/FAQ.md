# ELPM - Frequently Asked Questions (FAQ)

## 📋 Table of Contents

1. [Installation & Setup](#installation--setup)
2. [Usage & Features](#usage--features)
3. [Customization](#customization)
4. [Troubleshooting](#troubleshooting)
5. [Development](#development)
6. [Performance](#performance)
7. [Platform-Specific](#platform-specific)

---

## Installation & Setup

### Q: What do I need to install ELPM?

**A:** You need:
- Python 3.8 or higher
- PyQt6 (will be installed automatically if you use the launcher scripts)
- About 200 MB of disk space

### Q: How do I install ELPM?

**A:** The easiest way:
```bash
# Linux/macOS
cd /path/to/elpm-desktop/src
./run_elpm.sh

# Windows
cd C:\path\to\elpm-desktop\src
run_elpm.bat
```

Or manually:
```bash
pip install PyQt6
python elpm_main.py
```

See [QUICK_START.md](QUICK_START.md) for details.

### Q: Do I need administrator/root privileges?

**A:** No, you don't need special privileges to run ELPM. However:
- Some processes may be hidden if you don't have permissions
- Signal controls (when implemented) may require elevated privileges
- Currently uses sample data, so permissions don't matter

### Q: Can I use a virtual environment?

**A:** Yes! Recommended:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install PyQt6
python elpm_main.py
```

### Q: How do I verify the installation worked?

**A:** Run the diagnostic tools:
```bash
python test_imports.py     # Quick check
python diagnose.py         # Comprehensive check
```

Or see [CHECKLIST.md](CHECKLIST.md) for a complete verification checklist.

---

## Usage & Features

### Q: Is the process data real?

**A:** No, currently ELPM uses sample/mock data for demonstration. To get real process data:

1. Install psutil: `pip install psutil`
2. Modify `models/process_model.py` to fetch real processes
3. See [README_PYQT.md](README_PYQT.md) § Adding Real Process Data

### Q: Do the signal buttons (SIGTERM, SIGKILL, etc.) work?

**A:** Not yet. They're UI-only in v1.0.1. To implement:
- Add signal sending functionality
- Requires proper permissions
- See [README_PYQT.md](README_PYQT.md) § Adding Signal Functionality

### Q: Why are some tabs empty ("Coming soon")?

**A:** Process Tree, Network, and Search History tabs are not implemented yet. Currently working tabs:
- ✅ Processes (fully functional)
- ✅ Graphs (fully functional)
- ⚠️ Process Tree (placeholder)
- ⚠️ Network (placeholder)
- ⚠️ Search History (placeholder)

### Q: How do I search for a process?

**A:** 
1. Click the search bar at the top (or press Ctrl+F)
2. Type process name, PID, or part of command
3. Table filters automatically
4. Click X in search bar to clear

### Q: How do I sort processes?

**A:**
1. Go to Processes tab
2. Click "Sort by" dropdown
3. Choose: CPU%, Memory%, PID, or Name
4. Table re-sorts automatically

### Q: What do the colors mean?

**A:**
- **Cyan (#00d4ff)**: Primary actions, selected items
- **Red (#ff6b6b)**: Critical (CPU >70%, zombie processes)
- **Yellow (#ffd93d)**: Warnings (stopped processes)
- **Green (#51cf66)**: Normal/running processes
- **Light Cyan (#4ecdc4)**: Sleeping processes

See [README_PYQT.md](README_PYQT.md) § Color Coding.

### Q: Can I export data to CSV?

**A:** Not yet. The button exists but isn't functional in v1.0.1.

### Q: How often does the data refresh?

**A:** 
- Main data: Every 2 seconds (configurable)
- Graphs: Every 2 seconds
- Status bar: Every 1 second
- You can disable auto-refresh with the checkbox

### Q: What are the keyboard shortcuts?

**A:**
- `Ctrl+F` or `/`: Focus search bar
- `Ctrl+R`: Refresh (when auto-refresh is off)
- `Ctrl+W` or `Ctrl+Q`: Close application
- `Arrow Keys`: Navigate process list
- `Tab`: Switch between tabs

---

## Customization

### Q: Can I change the theme colors?

**A:** Yes! Edit `gui/styles.py`:

```python
# Find colors in MAIN_STYLES
background: #1a1a1a;    # Main background
background: #2d2d2d;    # Panel background
color: #00d4ff;         # Cyan accent
# etc.
```

See [README_PYQT.md](README_PYQT.md) § Modifying the Theme.

### Q: Can I change the window size?

**A:** Yes. Edit `gui/main_window.py`:

```python
self.setGeometry(100, 100, 1400, 800)  # x, y, width, height
```

Change `1400, 800` to your preferred size.

### Q: Can I add more processes to the sample data?

**A:** Yes. Edit `models/process_model.py` and add to the `processes` list in `get_sample_processes()`.

### Q: Can I change the refresh rate?

**A:** Yes. Edit `gui/main_window.py`:

```python
self.refresh_timer.setInterval(2000)  # milliseconds (2000 = 2 seconds)
```

### Q: Can I change fonts?

**A:** Yes. Several places:
- Application-wide: `elpm_main.py` - `QFont("Segoe UI", 9)`
- Monospace: `gui/views/processes_view.py` - `QFont("Consolas", 9)`
- Styles: `gui/styles.py` - search for `font-family`

---

## Troubleshooting

### Q: I get "ModuleNotFoundError: No module named 'PyQt6'"

**A:** Install PyQt6:
```bash
pip install PyQt6
# or
pip3 install PyQt6
```

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for details.

### Q: I get "No module named 'gui'"

**A:** You're not in the correct directory:
```bash
cd /path/to/elpm-desktop/src
python elpm_main.py
```

### Q: The application starts but crashes immediately

**A:** Run from terminal to see error messages:
```bash
python elpm_main.py
# Look for error output
```

Also run diagnostics:
```bash
python diagnose.py
```

### Q: The window is too small/large (DPI issues)

**A:** Set scaling:
```bash
# Linux/macOS
export QT_AUTO_SCREEN_SCALE_FACTOR=1
python elpm_main.py

# Windows: Use compatibility settings
```

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) § DPI Issues.

### Q: The graphs are blank/not showing

**A:**
1. Make sure you're on the "Graphs" tab
2. Wait a few seconds for data to accumulate
3. Update graphics drivers
4. Try software rendering: `export QT_XCB_GL_INTEGRATION=none`

### Q: Process table is empty

**A:**
1. Check that you're on the "Processes" tab
2. Clear any search filters (click X in search bar)
3. Uncheck "Root only" filter if checked
4. Run `python diagnose.py` to check installation

### Q: Auto-refresh doesn't work

**A:**
1. Make sure "Auto-refresh" checkbox is checked
2. Verify you're watching for changes (graphs animate, time updates)
3. Check that data IS changing (it's sample data, so changes are simulated)

---

## Development

### Q: How can I add real system monitoring?

**A:** 
1. Install psutil: `pip install psutil`
2. Modify `models/process_model.py`:

```python
import psutil

def get_real_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):
        try:
            processes.append(Process(
                pid=proc.info['pid'],
                # ... map other fields
            ))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return processes
```

See [README_PYQT.md](README_PYQT.md) § Adding Real Process Data.

### Q: How do I implement the signal controls?

**A:**
```python
import os, signal

def send_signal(self, sig):
    if self.selected_process:
        try:
            os.kill(self.selected_process.pid, sig)
        except PermissionError:
            # Show error dialog
            pass
```

See [README_PYQT.md](README_PYQT.md) § Adding Signal Functionality.

### Q: How is the application structured?

**A:** See [ARCHITECTURE.md](ARCHITECTURE.md) for:
- Complete architecture diagrams
- Class hierarchy
- Data flow
- File dependencies

### Q: Where should I start if I want to contribute?

**A:**
1. Read [ARCHITECTURE.md](ARCHITECTURE.md)
2. Review [FEATURES.md](FEATURES.md) for what needs work
3. Check [CHANGELOG.md](CHANGELOG.md) for recent changes
4. Pick a "Not Implemented" feature and start coding!

### Q: Can I add new tabs?

**A:** Yes! 
1. Create new view in `gui/views/my_view.py`
2. Add to `gui/main_window.py`:
```python
my_view = MyView()
self.tab_widget.addTab(my_view, "My Tab")
```

### Q: How do I debug the application?

**A:**
```bash
# Use Python debugger
python -m pdb elpm_main.py

# Or add print statements
print(f"Debug: {variable_name}")

# Or use logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## Performance

### Q: How much RAM does ELPM use?

**A:** Typically 50-100 MB. With large process lists (1000+), up to 150 MB.

### Q: How much CPU does it use?

**A:**
- Idle: 1-2%
- Active refresh: 5-10%
- With real data (psutil): May be higher depending on system

### Q: Can it handle 1000+ processes?

**A:** Yes, but:
- Table updates may slow down slightly
- Consider implementing virtual scrolling
- May want to increase refresh interval

### Q: Why does the graph repaint every frame?

**A:** Currently using full repaint for simplicity. Optimization possible:
- Cache grid as QPixmap
- Only redraw data line
- See [ARCHITECTURE.md](ARCHITECTURE.md) § Performance Optimization

### Q: How can I make it faster?

**A:**
1. Disable auto-refresh when not needed
2. Increase refresh interval (from 2s to 5s)
3. Reduce graph history (from 60 to 30 points)
4. Implement incremental table updates (vs full rebuild)

---

## Platform-Specific

### Q: Does it work on Linux?

**A:** Yes! Tested on:
- Ubuntu 20.04+
- Debian 11+
- Fedora 35+
- Arch Linux

### Q: Does it work on macOS?

**A:** Yes! Tested on:
- macOS 11 (Big Sur)
- macOS 12 (Monterey)
- macOS 13 (Ventura)

Note: Some fonts may look different. Segoe UI → San Francisco.

### Q: Does it work on Windows?

**A:** Yes! Tested on:
- Windows 10
- Windows 11

Use `run_elpm.bat` for automatic setup.

### Q: Are there platform-specific issues?

**A:**
- **Linux**: May need to install python3-tk
- **macOS**: Font rendering may differ slightly
- **Windows**: May need Visual C++ redistributables for PyQt6

### Q: Can I create a standalone executable?

**A:** Yes, use PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed elpm_main.py
```

Note: Executable will be large (~50-100 MB) due to PyQt6.

### Q: Can I create a .app (macOS) or .exe (Windows)?

**A:** Yes:
- **macOS**: Use `py2app`
- **Windows**: Use `PyInstaller` or `cx_Freeze`
- **Linux**: Create `.deb` or `.rpm` packages

---

## General Questions

### Q: Is ELPM free?

**A:** Yes, check the project license for terms.

### Q: Can I use this in production?

**A:** Current version (1.0.1) is for demonstration/educational purposes. For production:
- Add real process monitoring (psutil)
- Implement security features
- Add error handling
- Test thoroughly

### Q: Who should use ELPM?

**A:**
- Security professionals learning system monitoring
- SOC analysts needing a monitoring tool template
- System administrators
- Developers learning PyQt6
- Students studying GUI development

### Q: What's the difference between this and other process monitors?

**A:**
- **ELPM**: Educational, customizable, dark theme, Python/PyQt6
- **htop/top**: Terminal-based, lightweight, standard tools
- **System Monitor**: OS built-in, comprehensive
- **Commercial tools**: Feature-rich, expensive, closed-source

ELPM is designed to be a learning tool and template.

### Q: Can I contribute?

**A:** Yes! Review:
- [ARCHITECTURE.md](ARCHITECTURE.md) for structure
- [FEATURES.md](FEATURES.md) for what needs work
- Source code for coding standards

### Q: Where can I get help?

**A:**
1. **Quick help**: [QUICK_START.md](QUICK_START.md)
2. **Installation**: [INSTALL.md](INSTALL.md)
3. **Errors**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
4. **Everything**: [INDEX.md](INDEX.md)

### Q: Is there a tutorial?

**A:** Yes! Follow the learning paths in [INDEX.md](INDEX.md):
- Beginner: 30 minutes
- Intermediate: 2 hours
- Advanced: 4 hours
- Contributor: 8 hours

### Q: What's next for ELPM?

**A:** Planned features:
- Process Tree view
- Network connections view
- Search History tracking
- Real system monitoring
- Signal controls
- Export functionality
- Alert system

See [CHANGELOG.md](CHANGELOG.md) § Future Enhancements.

---

## Quick Answers

**Most Common Questions:**

| Question | Answer |
|----------|--------|
| How to install? | `./run_elpm.sh` or `pip install PyQt6; python elpm_main.py` |
| How to run? | `python elpm_main.py` from src directory |
| Is data real? | No, sample data. Use psutil for real data |
| Do signals work? | No, UI only. Needs implementation |
| How to search? | Type in top search bar, filters automatically |
| How to sort? | Use "Sort by" dropdown in Processes tab |
| Why is tab empty? | Some tabs not implemented (Process Tree, Network, History) |
| How to export? | Not implemented yet |
| Can I customize? | Yes! Edit `gui/styles.py` for theme |
| Where's documentation? | See [INDEX.md](INDEX.md) for all docs |

---

**Still have questions?**

1. Check [INDEX.md](INDEX.md) for all documentation
2. Run `python diagnose.py` for system check
3. See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for problems
4. Review source code - it's well commented!

---

**Last Updated**: 2025-10-08  
**Version**: 1.0.1  
**Questions Answered**: 50+
