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

### Graphs Tab Verification
Click on "Graphs" tab and verify:

**CPU Graph:**
- [ ] Title: "CPU Usage History (60 seconds)"
- [ ] Current CPU percentage displayed (top right)
- [ ] Graph with cyan line visible
- [ ] Grid lines visible
- [ ] X-axis labels (-60s to 0s)
- [ ] Y-axis labels (0% to 100%)
- [ ] Graph updates every 2 seconds

**Memory Graph:**
- [ ] Title: "Memory Usage History (60 seconds)"
- [ ] Current memory percentage and GB display
- [ ] Graph with yellow line visible
- [ ] Grid lines visible
- [ ] Graph updates every 2 seconds

**Statistics Panel:**
- [ ] CPU stats: Avg, Max, Min percentages
- [ ] Memory stats: Avg, Max, Min percentages
- [ ] Color-coded values (cyan for avg, red for max, green for min)

### Other Tabs Verification
- [ ] "Process Tree" tab shows placeholder with tree icon
- [ ] "Network" tab shows placeholder with network icon
- [ ] "Search History" tab shows placeholder with clock icon
- [ ] All placeholders say "Coming soon"

### Functionality Verification

**Search Functionality:**
- [ ] Click search bar or press Ctrl+F
- [ ] Type "chrome" or "root"
- [ ] Process table filters automatically
- [ ] Clear button (X) appears in search bar
- [ ] Clicking X clears search and shows all processes

**Sorting:**
- [ ] Click "Sort by" dropdown
- [ ] Select "CPU%"
- [ ] Table re-sorts by CPU (highest first)
- [ ] Try other sort options (Memory%, PID, Name)
- [ ] Each sort works correctly

**Filtering:**
- [ ] Check "Root only" checkbox
- [ ] Table shows only root user processes
- [ ] Uncheck - all processes return
- [ ] Check "Auto-refresh"
- [ ] Notice table updates every 2 seconds
- [ ] Uncheck - updates stop

**Process Selection:**
- [ ] Click different rows in process table
- [ ] Details panel updates for each selection
- [ ] Selected row remains highlighted
- [ ] Information matches selected process

**Real-time Updates:**
- [ ] Watch graphs for 10 seconds
- [ ] Both graphs animate/update
- [ ] Status bar time updates every second
- [ ] CPU/Memory percentages change
- [ ] Process table updates every 2 seconds (if auto-refresh on)

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
- [ ] Search filters instantly (<100ms)
- [ ] CPU usage < 10% when running
- [ ] Memory usage < 150 MB
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

### UI-Only Features ⚠️
(Present but not functional)
- [ ] Signal control buttons (visual only)
- [ ] Export CSV button (not implemented)
- [ ] Settings button (no dialog)
- [ ] Window minimize/close (not connected)

### Not Implemented ❌
- [ ] Process Tree view (placeholder)
- [ ] Network view (placeholder)
- [ ] Search History view (placeholder)
- [ ] Real system process data (uses sample data)

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
- [ ] Learn keyboard shortcuts
- [ ] Review FEATURES.md for capabilities

**Customization:**
- [ ] Review gui/styles.py for theming
- [ ] Check ARCHITECTURE.md for structure
- [ ] Consider adding psutil for real data
- [ ] Explore models/process_model.py

**Development:**
- [ ] Set up Python virtual environment
- [ ] Install optional dependencies (psutil)
- [ ] Read contribution guidelines
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

## Final Verification

- [ ] Opened application 3+ times successfully
- [ ] No error messages on startup
- [ ] All tabs accessible
- [ ] Graphs updating smoothly
- [ ] Search works correctly
- [ ] Process selection works
- [ ] Status bar updates
- [ ] Can close application cleanly
- [ ] Read documentation (at least QUICK_START.md)
- [ ] Know where to find help (README_PYQT.md, INSTALL.md)

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
