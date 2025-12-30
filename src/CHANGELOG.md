# ELPM PyQt6 - Changelog

## Version 1.1.0 (12-30-2025) - Fullscreen Enhancement Release

### New Features Added

**Fullscreen Functionality**:
- ✅ App starts maximized by default for better user experience
- ✅ Added fullscreen toggle button (⛶) in top bar
- ✅ Toggle between normal and fullscreen modes
- ✅ Improved window management and responsiveness

**User Experience Improvements**:
- ✅ Better default window sizing
- ✅ Enhanced UI controls
- ✅ Updated diagnose.py for compatibility

### Technical Changes

**File Changes**:
- `src/elpm_main.py`: Changed to showMaximized() for default startup
- `src/gui/main_window.py`: Added toggle_fullscreen() method
- `src/gui/widgets/top_bar.py`: Added fullscreen button and signal
- `src/diagnose.py`: Updated imports for compatibility
- `src/AppImageBuilder.yml`: Added for AppImage packaging

---

## Version 1.0.0 (10-15-2025) - Real-Time Monitoring Release

### Major Features Added

**Real-Time Process Monitoring**:
- ✅ Integrated psutil for real system process data
- ✅ Displays actual running processes from system
- ✅ Real-time CPU and memory usage
- ✅ Process details from live system data
- ✅ Auto-refresh every 2 seconds (toggleable)

**Functional Signal Controls**:
- ✅ SIGTERM (15) - Graceful termination (Green button #283618)
- ✅ SIGKILL (9) - Force kill (Red button #F71735)
- ✅ SIGSTOP (19) - Pause process (Yellow button #F3CA40)
- ✅ SIGCONT (18) - Resume process (Blue button #090446)
- ✅ Colored buttons with hover/press effects
- ✅ Confirmation dialogs before sending signals
- ✅ Automatic privilege escalation with sudo
- ✅ Error handling and user feedback

**CSV Export**:
- ✅ Export current process list to CSV
- ✅ Includes all process information
- ✅ Timestamped filename
- ✅ Compatible with spreadsheet software

**Real System Graphs**:
- ✅ CPU usage from psutil (replaces simulated data)
- ✅ Memory usage from psutil (replaces simulated data)
- ✅ Updates every 2 seconds
- ✅ Real avg/max/min statistics

**Status Bar Improvements**:
- ✅ Real CPU percentage from system
- ✅ Real memory usage with GB display
- ✅ Real disk usage percentage
- ✅ Actual process count
- ✅ Updates every 1 second

### Technical Changes


**File Changes**:
- `models/process_model.py`: Complete rewrite with psutil integration
- `gui/views/processes_view.py`: Added signal sending and CSV export
- `gui/widgets/status_bar.py`: Real system stats
- `gui/main_window.py`: Fixed timer management
- `run_elpm.sh`: Added psutil installation check
- `run_elpm.bat`: Added psutil installation check
- `test_imports.py`: Added psutil verification


### Improvements

- Removed duplicate timers (ProcessesView now has own timer)
- Better error handling for process access
- Graceful handling of permission denied errors
- Proper cleanup of zombie processes

### Performance

- Handles 1000+ processes smoothly
- CPU usage: 2-5% typical
- Memory usage: 80-150 MB
- Refresh rate: 2 seconds (configurable)

### Known Limitations

- Requires psutil for full functionality
- Signal controls require appropriate permissions
- Some process details may be hidden without elevated privileges

## Version 1.0.1 (2025-10-08) - Bug Fix Release

### Fixed
- **Critical**: Fixed `AttributeError: 'ProcessesView' object has no attribute 'process_table'`
  - Moved `populate_table()` call to after `self.process_table` assignment
  - Removed premature `populate_table()` call from `create_process_table()` method
  - This was causing the application to crash on startup

### Added
- **Launcher Scripts**:
  - `run_elpm.sh` for Linux/macOS with automatic PyQt6 installation
  - `run_elpm.bat` for Windows with automatic PyQt6 installation
- **Documentation**:
  - `INSTALL.md` - Comprehensive installation guide with troubleshooting
  - `QUICK_START.md` - Quick reference for getting started
  - `test_imports.py` - Import verification script
- **README Updates**:
  - Added troubleshooting section to `README_PYQT.md`
  - Added environment setup instructions

## Version 1.0.0 (10-15-2025) - Initial Release

### Features
- Five main tabs: Processes, Process Tree, Network, Graphs, Search History
- Real-time process monitoring with 22 sample processes
- Detailed process information panel
- CPU and Memory usage graphs with custom painting
- Dark theme optimized for extended monitoring
- Color-coded status indicators and severity levels
- Auto-refresh functionality (2-second intervals)
- Advanced filtering and sorting options
- Signal control buttons (SIGTERM, SIGKILL, SIGSTOP, SIGCONT)
- Search functionality across all process attributes
- Status bar with system statistics
- 1400×800 default window size

### Technical Implementation
- **Main Window** (`gui/main_window.py`)
  - Tab-based navigation system
  - Integrated top bar and status bar
  - Timer-based auto-refresh
  - Window sizing and positioning

- **Processes View** (`gui/views/processes_view.py`)
  - QTableWidget-based process table
  - 70/30 split layout (table/details)
  - Real-time data updates
  - Process selection and highlighting
  - Comprehensive details panel with color-coded sections

- **Graphs View** (`gui/views/graphs_view.py`)
  - Custom QPainter-based graph widgets
  - CPU usage graph with gradient fill
  - Memory usage graph with gradient fill
  - Statistics panel with avg/max/min values
  - 60-second historical data display

- **Widgets** (`gui/widgets/`)
  - Top bar with gradient logo and search
  - Status bar with real-time system stats
  - Reusable components for consistency

- **Styling** (`gui/styles.py`)
  - Dark theme (#1a1a1a background)
  - Cyan accents (#00d4ff)
  - Color-coded severity indicators
  - Consistent spacing and borders
  - Professional, security-focused aesthetic

- **Data Model** (`models/process_model.py`)
  - Process dataclass with all attributes
  - Sample data generator
  - Ready for integration with psutil

### Design Specifications
- **Colors**:
  - Background: #1a1a1a
  - Panels: #2d2d2d
  - Borders: #3a3a3a
  - Text: #e0e0e0
  - Muted text: #a0a0a0
  - Primary (Cyan): #00d4ff
  - Critical (Red): #ff6b6b
  - Success (Green): #51cf66
  - Warning (Yellow): #ffd93d
  - Info (Light Cyan): #4ecdc4

- **Typography**:
  - UI Font: Segoe UI, 9pt
  - Monospace: Consolas, 9pt
  - Headers: 14pt
  - Status: 11pt

- **Layout**:
  - Window: 1400×800px
  - Top bar: 60px
  - Tab bar: 50px
  - Status bar: 35px
  - Process table: 70% width
  - Details panel: 30% width
---

## How to Report Issues

If you encounter any bugs or issues:

1. Check `INSTALL.md` and `README_PYQT.md` for known solutions
2. Verify you're using Python 3.8+ and PyQt6 is installed
3. Run `test_imports.py` to verify setup
4. Check that you're in the correct directory (`src/`)
5. Look for similar issues in this changelog
