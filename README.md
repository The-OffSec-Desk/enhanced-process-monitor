<div align="center"><img src="src/assets/icons/ELPM-preview.png" alt="ELPM Logo" width="200"/></div>

# ELPM - Enhanced Linux Process Monitor

**Version 1.1.0** - Real-time process monitoring with fullscreen support

## 🚀 Quick Install & Run

### Linux/macOS (Automated)
```bash
git clone https://github.com/The-OffSec-Desk/enhanced-process-monitor.git
cd enhanced-process-monitor/src
chmod +x run_elpm.sh
./run_elpm.sh
```

### Windows (Automated)
```cmd
git clone https://github.com/The-OffSec-Desk/enhanced-process-monitor.git
cd enhanced-process-monitor\src
run_elpm.bat
```

### Manual Installation
```bash
pip install PyQt6 psutil
python src/elpm_main.py
```

---

## 📖 Documentation Index

## Complete Documentation Guide

Welcome to the ELPM (Enhanced Linux Process Monitor) PyQt6 documentation. This index helps you find the right document for your needs.

---

## Getting Started (New Users)

**Start here if this is your first time:**

1. **[QUICK_START.md](src/QUICK_START.md)** - Get up and running in 30 seconds
   - Fastest way to install and run
   - Basic usage instructions
   - Common tasks
   - Keyboard shortcuts

2. **[INSTALL.md](src/INSTALL.md)** - Detailed installation guide
   - Step-by-step installation
   - Prerequisites and requirements
   - Troubleshooting common issues
   - Virtual environment setup

3. **[CHECKLIST.md](src/CHECKLIST.md)** - Verification checklist
   - Pre-installation requirements
   - Installation steps
   - Post-installation verification
   - Success criteria

---

## Main Documentation (All Users)

**Read these for comprehensive information:**

4. **[README_PYQT.md](src/README_PYQT.md)** - Complete user guide
   - Full feature documentation
   - Usage instructions
   - Customization guide
   - Development information
   - ~1600 lines of documentation

5. **[README_SUMMARY.md](src/README_SUMMARY.md)** - Quick overview
   - Project summary
   - Key features list
   - Quick links to other docs
   - Performance metrics
   - Use cases

---

## Technical Documentation (Developers)

**For developers and contributors:**

6. **[ARCHITECTURE.md](src/ARCHITECTURE.md)** - System architecture
   - Application structure diagrams
   - Class hierarchy
   - Data flow diagrams
   - Signal/slot connections
   - Memory layout
   - Performance optimization points

7. **[FEATURES.md](src/FEATURES.md)** - Feature implementation status
   - Fully implemented features ✅
   - Partially implemented features ⚠️
   - Not implemented features ❌
   - Platform-specific features
   - Integration opportunities

8. **[CHANGELOG.md](src/CHANGELOG.md)** - Version history
   - Bug fixes
   - New features
   - Known limitations
   - Future enhancements
   - Migration guide

9. **[TROUBLESHOOTING.md](src/TROUBLESHOOTING.md)** - Problem resolution
   - Common errors and fixes
   - AttributeError solutions
   - Import error solutions
   - Display and performance issues
   - Diagnostic commands

---

## Quick Reference

**Quick answers to common questions:**

### Installation
- **How to install?** → [INSTALL.md](src/INSTALL.md) or [QUICK_START.md](src/QUICK_START.md)
- **Having issues?** → [INSTALL.md](src/INSTALL.md) § Troubleshooting
- **First time setup?** → [CHECKLIST.md](src/CHECKLIST.md)
- **Cross platform** → [CROSSPLATFORM.md](src/CROSSPLATFORM.md)

### Usage
- **How to use?** → [QUICK_START.md](src/QUICK_START.md) § Basic Usage
- **Keyboard shortcuts?** → [QUICK_START.md](src/QUICK_START.md) § Keyboard Shortcuts
- **What features work?** → [FEATURES.md](src/FEATURES.md)

### Development
- **How is it structured?** → [ARCHITECTURE.md](src/ARCHITECTURE.md)
- **Want to customize?** → [README_PYQT.md](src/README_PYQT.md) § Customization
- **Add real monitoring?** → [README_PYQT.md](src/README_PYQT.md) § Adding Real Process Data

### Troubleshooting
- **Won't start?** → [INSTALL.md](src/INSTALL.md) § Troubleshooting
- **Import errors?** → [INSTALL.md](src/INSTALL.md) § Issue: "ModuleNotFoundError"
- **Display issues?** → [INSTALL.md](src/INSTALL.md) § Issue: DPI scaling
---

## File Organization

### Source Code Files
```
src/
├── elpm_main.py              # Main entry point - START HERE
├── test_imports.py           # Test if setup is correct
├── run_elpm.sh              # Linux/macOS launcher
├── run_elpm.bat             # Windows launcher
├── requirements.txt          # Python dependencies
│
├── models/                   # Data models
│   └── process_model.py     # Process data structure
│
└── gui/                      # GUI components
    ├── main_window.py       # Main application window
    ├── styles.py            # Dark theme stylesheet
    ├── widgets/             # Reusable widgets
    │   ├── top_bar.py
    │   └── status_bar.py
    └── views/               # Tab content views
        ├── processes_view.py
        ├── graphs_view.py
        └── placeholder_view.py
```

### Documentation Files
```
docs/ (or src/)
├── INDEX.md                  # This file - Documentation index
├── QUICK_START.md           # Quick start guide
├── INSTALL.md               # Installation guide
├── CHECKLIST.md             # Verification checklist
├── README_PYQT.md           # Complete documentation
├── README_SUMMARY.md        # Project summary
├── ARCHITECTURE.md          # Technical architecture
├── FEATURES.md              # Feature list
└── CHANGELOG.md             # Version history
```

---

## Documentation by Task

### "I want to install ELPM"
1. Read: [QUICK_START.md](src/QUICK_START.md) § Installation
2. Or: [INSTALL.md](src/INSTALL.md) for detailed steps
3. Verify: [CHECKLIST.md](src/CHECKLIST.md)

### "I want to learn how to use ELPM"
1. Read: [QUICK_START.md](src/QUICK_START.md) § Basic Usage
2. Then: [README_PYQT.md](src/README_PYQT.md) § Usage
3. Reference: [FEATURES.md](src/FEATURES.md) for what works

### "I want to customize ELPM"
1. Read: [README_PYQT.md](src/README_PYQT.md) § Customization
2. Review: [ARCHITECTURE.md](src/ARCHITECTURE.md) § Customization Points
3. Modify: `gui/styles.py` for theme changes

### "I want to add real process monitoring"
1. Read: [README_PYQT.md](src/README_PYQT.md) § Adding Real Process Data
2. Install: `pip install Post-installation`
3. Modify: `models/process_model.py`

### "I'm having problems"
1. Check: [INSTALL.md](src/INSTALL.md) § Troubleshooting
2. Run: `python test_imports.py`
3. Verify: [CHECKLIST.md](src/CHECKLIST.md)

### "I want to contribute/develop"
1. Read: [ARCHITECTURE.md](src/ARCHITECTURE.md)
2. Review: [FEATURES.md](src/FEATURES.md) for what needs work
3. Check: [CHANGELOG.md](src/CHANGELOG.md) for recent changes

---

## Search Guide

### Find information about...

**Colors and Theme:**
- Primary: [README_PYQT.md](src/README_PYQT.md) § Color Coding
- Technical: [ARCHITECTURE.md](src/ARCHITECTURE.md) § Customization Points
- Implementation: `gui/styles.py` (source code)

**Process Table:**
- Usage: [QUICK_START.md](src/QUICK_START.md) § View Processes
- Features: [FEATURES.md](src/FEATURES.md) § Processes View
- Structure: [ARCHITECTURE.md](src/ARCHITECTURE.md) § Processes View Layout

**Graphs:**
- Usage: [QUICK_START.md](src/QUICK_START.md) § Monitor Resources
- Features: [FEATURES.md](src/FEATURES.md) § Graphs View
- Implementation: [ARCHITECTURE.md](src/ARCHITECTURE.md) § Graphs View Layout

**Installation Issues:**
- Quick fix: [QUICK_START.md](src/QUICK_START.md) § Troubleshooting
- Detailed: [INSTALL.md](src/INSTALL.md) § Troubleshooting
- Check: Run `test_imports.python`

**Data Models:**
- Overview: [README_PYQT.md](src/README_PYQT.md) § Project Structure
- Details: [ARCHITECTURE.md](src/ARCHITECTURE.md) § Data Flow
- Code: `models/process_model.py`

**Performance:**
- Metrics: [README_SUMMARY.md](src/README_SUMMARY.md) § Performance Metrics
- Optimization: [ARCHITECTURE.md](src/ARCHITECTURE.md) § Performance Optimization Points

---

## Learning Paths

### Path 1: End User (30 minutes)
1. [QUICK_START.md](src/QUICK_START.md) - 5 min
2. Run application - 2 min
3. Explore features - 15 min
4. [README_PYQT.md](src/README_PYQT.md) § Usage - 8 min

### Path 2: Power User (2 hours)
1. [INSTALL.md](src/INSTALL.md) - 20 min
2. [README_PYQT.md](src/README_PYQT.md) - 40 min
3. [FEATURES.md](src/FEATURES.md) - 30 min
4. Experiment with customization - 30 min

### Path 3: Developer (4 hours)
1. [README_SUMMARY.md](src/README_SUMMARY.md) - 15 min
2. [ARCHITECTURE.md](src/ARCHITECTURE.md) - 90 min
3. [FEATURES.md](src/FEATURES.md) - 30 min
4. Review source Cross-references - 90 min
5. [CHANGELOG.md](src/CHANGELOG.md) - 15 min

### Path 4: Contributor (8 hours)
1. All documents above - 4 hours
2. Set up development environment - 1 hour
3. Add psutil integration - 2 hours
4. Test and document changes - 1 hour

---

## Support Resources

### Documentation
- **General Help**: [README_PYQT.md](src/README_PYQT.md)
- **Installation Help**: [INSTALL.md](src/INSTALL.md)
- **Quick Help**: [QUICK_START.md](src/QUICK_START.md)

### Testing
- **Verify Setup**: `python test_imports.py`
- **Check Installation**: [CHECKLIST.md](src/CHECKLIST.md)

### Source Code
- **Main File**: `elpm_main.py`
- **Styles**: `gui/styles.py`
- **Data**: `models/process_model.py`

---

## Document Maintenance

**Last Updated**: 2025-10-08
**Version**: 1.0.1
**Total Pages**: 9 documents
**Total Size**: ~24,000 words

### Document Status
- ✅ All documents current
- ✅ Cross-references verified
- ✅ Code examples tested
- ✅ Screenshots available (in original docs)
- ✅ Links functional

---

## Recommended Reading Order

### First Time Users
1. INDEX.md (you are here) ← **START**
2. QUICK_START.md
3. CHECKLIST.md
4. README_SUMMARY.md
5. README_PYQT.md

### Developers
1. INDEX.md (you are here) ← **START**
2. README_SUMMARY.md
3. ARCHITECTURE.md
4. FEATURES.md
5. Source code review
6. CHANGELOG.md

### Troubleshooting
1. QUICK_START.md § Troubleshooting ← **START**
2. INSTALL.md § Troubleshooting
3. Run `test_imports.py`
4. CHECKLIST.md
5. README_PYQT.md

---

**Happy monitoring! 🚀**

For immediate help, start with [QUICK_START.md](src/QUICK_START.md)
