<div align="center"><img src="src/assets/icons/ELPM-preview.png" alt="ELPM Logo" width="200"/></div>


# ELPM Documentation Index

## 📚 Complete Documentation Guide

Welcome to the ELPM (Enhanced Linux Process Monitor) PyQt6 documentation. This index helps you find the right document for your needs.

---

## 🚀 Getting Started (New Users)

**Start here if this is your first time:**

1. **[QUICK_START.md](QUICK_START.md)** - Get up and running in 30 seconds
   - Fastest way to install and run
   - Basic usage instructions
   - Common tasks
   - Keyboard shortcuts

2. **[INSTALL.md](INSTALL.md)** - Detailed installation guide
   - Step-by-step installation
   - Prerequisites and requirements
   - Troubleshooting common issues
   - Virtual environment setup

3. **[CHECKLIST.md](CHECKLIST.md)** - Verification checklist
   - Pre-installation requirements
   - Installation steps
   - Post-installation verification
   - Success criteria

---

## 📖 Main Documentation (All Users)

**Read these for comprehensive information:**

4. **[README_PYQT.md](README_PYQT.md)** - Complete user guide
   - Full feature documentation
   - Usage instructions
   - Customization guide
   - Development information
   - ~1600 lines of documentation

5. **[README_SUMMARY.md](README_SUMMARY.md)** - Quick overview
   - Project summary
   - Key features list
   - Quick links to other docs
   - Performance metrics
   - Use cases

---

## 🔧 Technical Documentation (Developers)

**For developers and contributors:**

6. **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture
   - Application structure diagrams
   - Class hierarchy
   - Data flow diagrams
   - Signal/slot connections
   - Memory layout
   - Performance optimization points

7. **[FEATURES.md](FEATURES.md)** - Feature implementation status
   - Fully implemented features ✅
   - Partially implemented features ⚠️
   - Not implemented features ❌
   - Platform-specific features
   - Integration opportunities

8. **[CHANGELOG.md](CHANGELOG.md)** - Version history
   - Bug fixes
   - New features
   - Known limitations
   - Future enhancements
   - Migration guide

9. **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Problem resolution
   - Common errors and fixes
   - AttributeError solutions
   - Import error solutions
   - Display and performance issues
   - Diagnostic commands

---

## 📋 Quick Reference

**Quick answers to common questions:**

### Installation
- **How to install?** → [INSTALL.md](INSTALL.md) or [QUICK_START.md](QUICK_START.md)
- **Having issues?** → [INSTALL.md](INSTALL.md) § Troubleshooting
- **First time setup?** → [CHECKLIST.md](CHECKLIST.md)

### Usage
- **How to use?** → [QUICK_START.md](QUICK_START.md) § Basic Usage
- **Keyboard shortcuts?** → [QUICK_START.md](QUICK_START.md) § Keyboard Shortcuts
- **What features work?** → [FEATURES.md](FEATURES.md)

### Development
- **How is it structured?** → [ARCHITECTURE.md](ARCHITECTURE.md)
- **Want to customize?** → [README_PYQT.md](README_PYQT.md) § Customization
- **Add real monitoring?** → [README_PYQT.md](README_PYQT.md) § Adding Real Process Data

### Troubleshooting
- **Won't start?** → [INSTALL.md](INSTALL.md) § Troubleshooting
- **Import errors?** → [INSTALL.md](INSTALL.md) § Issue: "ModuleNotFoundError"
- **Display issues?** → [INSTALL.md](INSTALL.md) § Issue: DPI scaling

---

## 📂 File Organization

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

## 🎯 Documentation by Task

### "I want to install ELPM"
1. Read: [QUICK_START.md](QUICK_START.md) § Installation
2. Or: [INSTALL.md](INSTALL.md) for detailed steps
3. Verify: [CHECKLIST.md](CHECKLIST.md)

### "I want to learn how to use ELPM"
1. Read: [QUICK_START.md](QUICK_START.md) § Basic Usage
2. Then: [README_PYQT.md](README_PYQT.md) § Usage
3. Reference: [FEATURES.md](FEATURES.md) for what works

### "I want to customize ELPM"
1. Read: [README_PYQT.md](README_PYQT.md) § Customization
2. Review: [ARCHITECTURE.md](ARCHITECTURE.md) § Customization Points
3. Modify: `gui/styles.py` for theme changes

### "I want to add real process monitoring"
1. Read: [README_PYQT.md](README_PYQT.md) § Adding Real Process Data
2. Install: `pip install psutil`
3. Modify: `models/process_model.py`

### "I'm having problems"
1. Check: [INSTALL.md](INSTALL.md) § Troubleshooting
2. Run: `python test_imports.py`
3. Verify: [CHECKLIST.md](CHECKLIST.md)

### "I want to contribute/develop"
1. Read: [ARCHITECTURE.md](ARCHITECTURE.md)
2. Review: [FEATURES.md](FEATURES.md) for what needs work
3. Check: [CHANGELOG.md](CHANGELOG.md) for recent changes

---

## 📊 Documentation Statistics

| Document | Lines | Words | Purpose | Audience |
|----------|-------|-------|---------|----------|
| QUICK_START.md | ~200 | ~1,500 | Quick reference | New users |
| INSTALL.md | ~300 | ~2,500 | Installation guide | All users |
| CHECKLIST.md | ~400 | ~2,000 | Verification steps | All users |
| README_PYQT.md | ~350 | ~3,000 | Complete guide | All users |
| README_SUMMARY.md | ~400 | ~3,500 | Project overview | All users |
| ARCHITECTURE.md | ~600 | ~4,000 | Technical docs | Developers |
| FEATURES.md | ~400 | ~3,000 | Feature status | Developers |
| CHANGELOG.md | ~300 | ~2,500 | Version history | Developers |
| INDEX.md | ~300 | ~2,000 | This file | All users |

**Total Documentation**: ~3,250 lines, ~24,000 words

---

## 🔍 Search Guide

### Find information about...

**Colors and Theme:**
- Primary: [README_PYQT.md](README_PYQT.md) § Color Coding
- Technical: [ARCHITECTURE.md](ARCHITECTURE.md) § Customization Points
- Implementation: `gui/styles.py` (source code)

**Process Table:**
- Usage: [QUICK_START.md](QUICK_START.md) § View Processes
- Features: [FEATURES.md](FEATURES.md) § Processes View
- Structure: [ARCHITECTURE.md](ARCHITECTURE.md) § Processes View Layout

**Graphs:**
- Usage: [QUICK_START.md](QUICK_START.md) § Monitor Resources
- Features: [FEATURES.md](FEATURES.md) § Graphs View
- Implementation: [ARCHITECTURE.md](ARCHITECTURE.md) § Graphs View Layout

**Installation Issues:**
- Quick fix: [QUICK_START.md](QUICK_START.md) § Troubleshooting
- Detailed: [INSTALL.md](INSTALL.md) § Troubleshooting
- Check: Run `test_imports.py`

**Data Models:**
- Overview: [README_PYQT.md](README_PYQT.md) § Project Structure
- Details: [ARCHITECTURE.md](ARCHITECTURE.md) § Data Flow
- Code: `models/process_model.py`

**Performance:**
- Metrics: [README_SUMMARY.md](README_SUMMARY.md) § Performance Metrics
- Optimization: [ARCHITECTURE.md](ARCHITECTURE.md) § Performance Optimization Points

---

## 🎓 Learning Paths

### Path 1: End User (30 minutes)
1. [QUICK_START.md](QUICK_START.md) - 5 min
2. Run application - 2 min
3. Explore features - 15 min
4. [README_PYQT.md](README_PYQT.md) § Usage - 8 min

### Path 2: Power User (2 hours)
1. [INSTALL.md](INSTALL.md) - 20 min
2. [README_PYQT.md](README_PYQT.md) - 40 min
3. [FEATURES.md](FEATURES.md) - 30 min
4. Experiment with customization - 30 min

### Path 3: Developer (4 hours)
1. [README_SUMMARY.md](README_SUMMARY.md) - 15 min
2. [ARCHITECTURE.md](ARCHITECTURE.md) - 90 min
3. [FEATURES.md](FEATURES.md) - 30 min
4. Review source code - 90 min
5. [CHANGELOG.md](CHANGELOG.md) - 15 min

### Path 4: Contributor (8 hours)
1. All documents above - 4 hours
2. Set up development environment - 1 hour
3. Add psutil integration - 2 hours
4. Test and document changes - 1 hour

---

## 🆘 Support Resources

### Documentation
- **General Help**: [README_PYQT.md](README_PYQT.md)
- **Installation Help**: [INSTALL.md](INSTALL.md)
- **Quick Help**: [QUICK_START.md](QUICK_START.md)

### Testing
- **Verify Setup**: `python test_imports.py`
- **Check Installation**: [CHECKLIST.md](CHECKLIST.md)

### Source Code
- **Main File**: `elpm_main.py`
- **Styles**: `gui/styles.py`
- **Data**: `models/process_model.py`

---

## 📝 Document Maintenance

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

## 🎯 Recommended Reading Order

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

For immediate help, start with [QUICK_START.md](QUICK_START.md)
