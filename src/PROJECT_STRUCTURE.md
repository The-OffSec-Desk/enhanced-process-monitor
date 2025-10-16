# ELPM Project Structure

Complete file organization for the PyQt6 desktop application.

## 📁 Directory Tree

```
elpm-desktop/
├── src/                                    # Main source directory
│   │
│   ├── 📄 elpm_main.py                    # Application entry point [START HERE]
│   ├── 📄 requirements.txt                 # Python dependencies
│   ├── 📄 test_imports.py                  # Verify installation script
│   ├── 📄 diagnose.py                      # Comprehensive diagnostics tool
│   ├── 🔧 run_elpm.sh                     # Linux/macOS launcher script
│   ├── 🔧 run_elpm.bat                    # Windows launcher script
│   │
│   ├── 📂 models/                          # Data models
│   │   ├── __init__.py                     # Package initializer
│   │   └── 📄 process_model.py            # Process data structures & samples
│   │                                       # - Process dataclass
│   │                                       # - get_sample_processes() function
│   │                                       # - 22 sample processes with full data
│   │
│   ├── 📂 gui/                             # GUI components
│   │   ├── __init__.py                     # Package initializer
│   │   │
│   │   ├── 📄 main_window.py              # Main application window
│   │   │                                   # - QMainWindow subclass
│   │   │                                   # - Tab management
│   │   │                                   # - Timer setup (refresh, status)
│   │   │                                   # - Layout: top bar, tabs, status bar
│   │   │
│   │   ├── 📄 styles.py                   # Application-wide stylesheets
│   │   │                                   # - MAIN_STYLES constant
│   │   │                                   # - Dark theme definitions
│   │   │                                   # - Color scheme (#1a1a1a, #00d4ff)
│   │   │                                   # - Widget-specific styles
│   │   │
│   │   ├── 📂 widgets/                    # Reusable UI components
│   │   │   ├── __init__.py                 # Package initializer
│   │   │   │
│   │   │   ├── 📄 top_bar.py              # Top navigation bar
│   │   │   │                               # - Logo with gradient
│   │   │   │                               # - Search bar with signal
│   │   │   │                               # - Control buttons (refresh, settings)
│   │   │   │                               # - Window controls (minimize, close)
│   │   │   │
│   │   │   └── 📄 status_bar.py           # Bottom status bar
│   │   │                                   # - CPU usage display
│   │   │                                   # - Memory usage display
│   │   │                                   # - Disk usage display
│   │   │                                   # - Process count
│   │   │                                   # - Current time (auto-updating)
│   │   │
│   │   └── 📂 views/                      # Main content views
│   │       ├── __init__.py                 # Package initializer
│   │       │
│   │       ├── 📄 processes_view.py       # Process monitoring view (main)
│   │       │                               # - Process table (QTableWidget)
│   │       │                               # - 9 columns: PID, User, CPU%, etc.
│   │       │                               # - Control bar with filters
│   │       │                               # - Sort: CPU%, Memory%, PID, Name
│   │       │                               # - Filters: root only, hide kernel
│   │       │                               # - Process details panel (70/30 split)
│   │       │                               # - 6 color-coded info sections
│   │       │                               # - 4 signal control buttons
│   │       │                               # - Search integration
│   │       │                               # - Auto-refresh support
│   │       │
│   │       ├── 📄 graphs_view.py          # CPU/Memory graphs view
│   │       │                               # - GraphWidget custom class
│   │       │                               # - CPU graph (cyan, 60s history)
│   │       │                               # - Memory graph (yellow, 60s history)
│   │       │                               # - Custom QPainter rendering
│   │       │                               # - Grid, axes, labels
│   │       │                               # - Statistics panel (avg/max/min)
│   │       │                               # - Gradient fills
│   │       │                               # - Auto-updating data
│   │       │
│   │       └── 📄 placeholder_view.py     # Placeholder for unimplemented tabs
│   │                                       # - Used by: Process Tree, Network,
│   │                                       #   Search History tabs
│   │                                       # - Shows icon and "Coming soon" text
│   │
│   └── 📂 docs/                            # Documentation (optional location)
│       └── [All .md files can go here or in root]
│
└── 📂 docs/                                # Documentation files
    │
    ├── 📘 START_HERE.md                   # **FIRST FILE TO READ** ⭐
    │                                       # Quick start, links, overview
    │
    ├── 📗 QUICK_START.md                  # Fast installation & usage
    │                                       # Installation (30 seconds)
    │                                       # Basic usage guide
    │                                       # Common tasks
    │                                       # Keyboard shortcuts
    │
    ├── 📗 INSTALL.md                      # Detailed installation guide
    │                                       # Step-by-step instructions
    │                                       # Prerequisites
    │                                       # Troubleshooting section
    │                                       # Virtual environment setup
    │                                       # Platform-specific notes
    │
    ├── 📗 CHECKLIST.md                    # Installation verification
    │                                       # Pre-installation checklist
    │                                       # Installation steps
    │                                       # Post-installation verification
    │                                       # Visual verification
    │                                       # Functionality tests
    │                                       # Success criteria
    │
    ├── 📙 README_PYQT.md                  # Complete user guide
    │                                       # Full feature documentation
    │                                       # Usage instructions
    │                                       # Customization guide
    │                                       # Development guide
    │                                       # API reference
    │
    ├── 📙 README_SUMMARY.md               # Project overview
    │                                       # Quick links
    │                                       # Feature summary
    │                                       # File structure
    │                                       # Performance metrics
    │
    ├── 📕 ARCHITECTURE.md                 # Technical architecture
    │                                       # ASCII diagrams
    │                                       # Class hierarchy
    │                                       # Data flow
    │                                       # Signal/slot connections
    │                                       # Memory layout
    │                                       # Optimization points
    │
    ├── 📕 FEATURES.md                     # Feature implementation status
    │                                       # ✅ Implemented features
    │                                       # ⚠️ Partial features
    │                                       # ❌ Not implemented
    │                                       # Integration opportunities
    │
    ├── 📕 CHANGELOG.md                    # Version history
    │                                       # Bug fixes
    │                                       # New features
    │                                       # Known limitations
    │                                       # Migration notes
    │
    ├── 📕 TROUBLESHOOTING.md              # Problem resolution
    │                                       # Common errors
    │                                       # Solutions
    │                                       # Diagnostic commands
    │                                       # Recovery procedures
    │
    ├── 📙 INDEX.md                        # Documentation index
    │                                       # All docs listed
    │                                       # Quick links
    │                                       # Search guide
    │                                       # Learning paths
    │
    └── 📄 PROJECT_STRUCTURE.md            # This file
                                            # Complete file tree
                                            # File descriptions
```

## 📊 File Statistics

### Source Code
| Category        | Files | Lines  | Purpose                         |
|-----------------|-------|--------|---------------------------------|
| **Entry Point** | 1     | 38     | Application startup             |
| **Data Models** | 1     | 150    | Process data structures         |
| **Main Window** | 1     | 200    | Application window & tabs       |
| **Styles**      | 1     | 100    | Dark theme CSS                  |
| **Widgets**     | 2     | 300    | Top bar, status bar             |
| **Views**       | 3     | 800    | Processes, graphs, placeholders |
| **Utilities**   | 2     | 200    | Tests, diagnostics              |
| **Launchers**   | 2     | 100    | Shell scripts                   |
| **Total**       | 13    | ~1,900 | Complete application            |

### Documentation
| Document             | Words   | Purpose         | Audience   |
|----------------------|---------|-----------------|------------|
| START_HERE.md        | 1,200   | Entry point     | Everyone   |
| QUICK_START.md       | 1,500   | Quick guide     | Beginners  |
| INSTALL.md           | 2,500   | Installation    | All users  |
| CHECKLIST.md         | 2,000   | Verification    | All users  |
| README_PYQT.md       | 3,000   | User manual     | All users  |
| README_SUMMARY.md    | 3,500   | Overview        | All users  |
| ARCHITECTURE.md      | 4,000   | Technical       | Developers |
| FEATURES.md          | 3,000   | Feature list    | Developers |
| CHANGELOG.md         | 2,500   | History         | Developers |
| TROUBLESHOOTING.md   | 3,500   | Problem solving | All users  |
| INDEX.md             | 2,000   | Navigation      | All users  |
| PROJECT_STRUCTURE.md | 1,500   | This file       | All users  |
| **Total**            | ~30,200 | Complete docs   | -          |

## 🎯 File Purposes

### Core Application Files

#### `elpm_main.py`
- **Purpose**: Application entry point
- **Lines**: ~38
- **Key Functions**:
  - Initialize QApplication
  - Set font and DPI scaling
  - Create and show main window
  - Start event loop

#### `models/process_model.py`
- **Purpose**: Data structures
- **Lines**: ~150
- **Key Components**:
  - `Process` dataclass with 15 fields
  - `get_sample_processes()` function
  - 22 realistic sample processes
  - Ready for psutil integration

#### `gui/main_window.py`
- **Purpose**: Main application window
- **Lines**: ~200
- **Key Components**:
  - QMainWindow subclass
  - Tab widget management
  - Timer setup (refresh, status)
  - View initialization
  - Search integration

#### `gui/styles.py`
- **Purpose**: Application theming
- **Lines**: ~100
- **Key Components**:
  - `MAIN_STYLES` constant (large string)
  - Dark theme colors
  - Widget-specific styles
  - Hover effects, borders, fonts

### Widget Files

#### `gui/widgets/top_bar.py`
- **Purpose**: Top navigation bar
- **Lines**: ~150
- **Key Components**:
  - Gradient logo
  - Search bar with clear button
  - Refresh and settings buttons
  - Window control buttons
  - Custom signals

#### `gui/widgets/status_bar.py`
- **Purpose**: Bottom status display
- **Lines**: ~150
- **Key Components**:
  - System stats (CPU, memory, disk)
  - Process count
  - Time display (auto-updating)
  - Icon integration

### View Files

#### `gui/views/processes_view.py`
- **Purpose**: Main process monitoring view
- **Lines**: ~500
- **Key Components**:
  - QTableWidget with 9 columns
  - Control bar (sort, filters)
  - Details panel (6 sections)
  - Signal buttons (4 types)
  - Search filtering
  - Row selection handling
  - Color-coded indicators

#### `gui/views/graphs_view.py`
- **Purpose**: CPU/Memory visualization
- **Lines**: ~250
- **Key Components**:
  - Custom GraphWidget class
  - QPainter rendering
  - 60-second data history
  - Two graphs (CPU, Memory)
  - Statistics panel
  - Gradient fills
  - Grid and axes

#### `gui/views/placeholder_view.py`
- **Purpose**: Placeholder for unimplemented tabs
- **Lines**: ~50
- **Key Components**:
  - Centered icon
  - Title text
  - "Coming soon" message

### Utility Files

#### `test_imports.py`
- **Purpose**: Verify installation
- **Lines**: ~50
- **Tests**:
  - PyQt6 modules
  - Application modules
  - Data models
  - All views

#### `diagnose.py`
- **Purpose**: Comprehensive diagnostics
- **Lines**: ~250
- **Checks**:
  - Python version
  - PyQt6 installation
  - File structure
  - Module imports
  - Environment variables
  - System resources

## 🗂️ File Dependencies

```
elpm_main.py
    ↓
gui/main_window.py
    ├─→ gui/styles.py
    ├─→ gui/widgets/top_bar.py
    ├─→ gui/widgets/status_bar.py
    ├─→ gui/views/processes_view.py
    │       ├─→ models/process_model.py
    │       └─→ gui/styles.py
    ├─→ gui/views/graphs_view.py
    │       └─→ gui/styles.py
    └─→ gui/views/placeholder_view.py
```

## 📋 Documentation Reading Order

### For New Users
1. **START_HERE.md** ← Begin here
2. **QUICK_START.md**
3. **CHECKLIST.md**
4. Run the application
5. **README_PYQT.md** (as reference)

### For Developers
1. **START_HERE.md**
2. **README_SUMMARY.md**
3. **ARCHITECTURE.md**
4. **FEATURES.md**
5. Review source code
6. **CHANGELOG.md**

### For Troubleshooting
1. **TROUBLESHOOTING.md**
2. Run `diagnose.py`
3. **INSTALL.md** § Troubleshooting
4. **CHECKLIST.md**

## 🎨 File Naming Conventions

- **Uppercase .md**: Documentation (README, INSTALL, etc.)
- **lowercase .py**: Source code (Python files)
- **.sh/.bat**: Shell scripts (launchers)
- **__init__.py**: Python package markers
- **test_*.py**: Test/verification scripts
```

## 📍 Important Locations

| What             | Where                              |
|------------------|------------------------------------|
| **Start Here**   | `START_HERE.md`                    |
| **Run App**      | `elpm_main.py`                     |
| **Test Setup**   | `test_imports.py` or `diagnose.py` |
| **Main Code**    | `gui/main_window.py`               |
| **Theme**        | `gui/styles.py`                    |
| **Data**         | `models/process_model.py`          |
| **Processes**    | `gui/views/processes_view.py`      |
| **Graphs**       | `gui/views/graphs_view.py`         |
| **Help**         | `INDEX.md` or `TROUBLESHOOTING.md` |

---

**Last Updated**: 10-15-2025
**Version**: 1.0.0
