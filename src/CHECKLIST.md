# ELPM Installation & Verification Checklist

## Pre-Installation Checklist

### System Requirements
- [ ] Operating System: Linux, macOS 10.13+, or Windows 10+
- [ ] Python installed (3.8 or higher)
- [ ] Terminal/Command Prompt access
- [ ] Internet connection (for installing PyQt6)
- [ ] 200 MB free disk space

### Verify Python Installation
```bash
# Linux/macOS
python3 --version

# Windows
python --version
```
- [ ] Python version is 3.8 or higher
- [ ] pip is available (`python3 -m pip --version`)

## Installation Checklist

### Option 1: Automated Installation (Recommended)

**Linux/macOS:**
- [ ] Navigated to `/path/to/elpm-desktop/src`
- [ ] Made script executable: `chmod +x run_elpm.sh`
- [ ] Ran launcher: `./run_elpm.sh`
- [ ] PyQt6 installed automatically (if needed)
- [ ] Application started successfully

**Windows:**
- [ ] Navigated to `C:\path\to\elpm-desktop\src`
- [ ] Ran launcher: `run_elpm.bat`
- [ ] PyQt6 installed automatically (if needed)
- [ ] Application started successfully

### Option 2: Manual Installation

- [ ] Navigated to project src directory
- [ ] Installed PyQt6: `pip install PyQt6`
- [ ] Verified installation: `python test_imports.py`
- [ ] All import checks show ✓ (green checkmarks)
- [ ] Ran application: `python elpm_main.py`
- [ ] Application started successfully

## Post-Installation Verification

### Visual Verification
When the application starts, verify you see:

**Window & Layout:**
- [ ] Window opens at 1400×800 size (or similar)
- [ ] Dark theme (dark gray/black background)
- [ ] No error messages in terminal/console

**Top Bar:**
- [ ] Gradient logo (cyan to purple) on left
- [ ] "ELPM v1.0" text visible
- [ ] Search bar in center
- [ ] Four control buttons on right (Refresh, Settings, Minimize, Close)

**Tab Navigation:**
- [ ] Five tabs visible: Processes, Process Tree, Network, Graphs, Search History
- [ ] Active tab highlighted in cyan
- [ ] Tabs respond to clicks

**Status Bar (Bottom):**
- [ ] CPU percentage with green icon
- [ ] Memory percentage and GB display
- [ ] Disk percentage
- [ ] Process count (should show "287")
- [ ] Current time (updating every second)

### Processes Tab Verification
Click on "Processes" tab and verify:

**Left Panel - Process Table:**
- [ ] Table with 9 columns: PID, User, CPU%, MEM%, VSZ, RSS, Status, Threads, Command
- [ ] 22 rows of process data visible
- [ ] Alternating row colors (striped)
- [ ] Rows highlight on hover
- [ ] Clicking a row selects it (cyan highlight)

**Control Bar:**
- [ ] "Sort by" dropdown with options: CPU%, Memory%, PID, Name
- [ ] Three checkboxes: "Root only", "Hide kernel threads", "Auto-refresh"
- [ ] "Export CSV" button visible

**Right Panel - Process Details:**
- [ ] "Process Details" header
- [ ] Color-coded section headers:
  - [ ] Cyan: "Process Information"
  - [ ] Yellow: "Resource Usage"
  - [ ] Green: "Timing"
  - [ ] Purple: "Command"
  - [ ] Cyan: "Working Directory"
  - [ ] Orange: "Files & Connections"
- [ ] Four signal buttons at bottom:
  - [ ] Green: "SIGTERM (15)"
  - [ ] Red: "SIGKILL (9)"
  - [ ] Yellow: "SIGSTOP (19)"
  - [ ] Cyan: "SIGCONT (18)"

**Process Details Content:**
- [ ] PID number shown
- [ ] Process name extracted from command
- [ ] Status badge (color-coded: running=green, sleeping=cyan)
- [ ] User name (root in red if applicable)
- [ ] CPU percentage with progress bar
- [ ] Memory percentage with progress bar
- [ ] Full command line in dark box
- [ ] Working directory path
- [ ] Open files count
- [ ] Network connections count


## Troubleshooting Checklist

If application doesn't start, check:

- [ ] In correct directory (`src/`)
- [ ] Python 3.8+ installed
- [ ] PyQt6 installed (`pip list | grep PyQt6`)
- [ ] No antivirus blocking Python
- [ ] Sufficient permissions to run scripts

If display looks wrong, check:

- [ ] Monitor resolution ≥ 1024×768
- [ ] DPI scaling not too high
- [ ] Graphics drivers up to date
- [ ] PyQt6 version ≥ 6.5.0

If errors appear, check:

- [ ] Full error message copied
- [ ] Python version confirmed
- [ ] All files present in src directory
- [ ] No modified/corrupted files
- [ ] Run `test_imports.py` - all pass?

## Performance Checklist

Normal operation should show:

- [ ] Smooth window resizing
- [ ] No lag when clicking tabs
- [ ] Instant row selection response
- [ ] Graphs update smoothly without flicker
- [ ] No freezing or hanging

## Feature Completeness Checklist

### Working Features ✅
- [ ] Dark theme rendering
- [ ] All 5 tabs present and clickable
- [ ] Process table with 22 entries
- [ ] Process details panel
- [ ] CPU and Memory graphs
- [ ] Search and filter
- [ ] Sorting options
- [ ] Auto-refresh toggle
- [ ] Status bar updates
- [ ] Time display updates


## Next Steps Checklist

After successful installation:

**Basic Usage:**
- [ ] Read QUICK_START.md
- [ ] Explore all five tabs
- [ ] Try searching for processes
- [ ] Test different sort options
- [ ] Watch graphs update in real-time

**Advanced Usage:**
- [ ] Read README_PYQT.md
- [ ] Understand color coding
- [ ] Review FEATURES.md for capabilities

**Customization:**
- [ ] Review gui/styles.py for theming
- [ ] Check ARCHITECTURE.md for structure
- [ ] Explore models/process_model.py

**Development:**
- [ ] Set up Python virtual environment
-- [ ] Read contribution guidelines
- [ ] Review code structure

## Success Criteria

✅ Installation is successful if:

1. Application starts without errors
2. Window displays with dark theme
3. All UI elements are visible and positioned correctly
4. Process table shows 22 entries
5. Graphs animate and update
6. Status bar shows updating stats
7. Search and filters work
8. No crashes or freezes

---

✅ **ALL CHECKS PASSED?** Congratulations! ELPM is successfully installed and working.

❌ **Some checks failed?** See INSTALL.md troubleshooting section or review error messages.

**Date Completed**: _______________
**Python Version**: _______________
**PyQt6 Version**: _______________
**Operating System**: _______________

---

**Need Help?**
1. Check INSTALL.md for troubleshooting
2. Review README_PYQT.md for usage
3. Run `python test_imports.py` to verify setup
