# 🚀 ELPM - Start Here!

Welcome to ELPM (Enhanced Linux Process Monitor) - PyQt6 Desktop Application

---

## ⚡ Quick Start (Choose One)

### Option 1: Automated Launcher (Easiest) ⭐

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

### Option 2: Manual Launch
```bash
cd /path/to/elpm-desktop/src
pip install PyQt6
python elpm_main.py
```

---

## 📚 Documentation Quick Links

**I want to...**

| Task | Document | Time |
|------|----------|------|
| **Install quickly** | [QUICK_START.md](QUICK_START.md) | 2 min |
| **Install with details** | [INSTALL.md](INSTALL.md) | 10 min |
| **Verify installation** | [CHECKLIST.md](CHECKLIST.md) | 5 min |
| **Fix problems** | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | varies |
| **Learn to use** | [README_PYQT.md](README_PYQT.md) | 20 min |
| **See all docs** | [INDEX.md](INDEX.md) | 2 min |
| **Understand structure** | [ARCHITECTURE.md](ARCHITECTURE.md) | 30 min |
| **Check features** | [FEATURES.md](FEATURES.md) | 10 min |

---

## 🔧 Troubleshooting

### Not Starting?

**Run diagnostics:**
```bash
python diagnose.py
```

**Or check imports:**
```bash
python test_imports.py
```

### Common Errors

| Error                           | Solution                             |
|---------------------------------|--------------------------------------|
| `ModuleNotFoundError: PyQt6`    | Run `pip install PyQt6`              |
| `No module named 'gui'`         | Make sure you're in `src/` directory |
| `AttributeError: process_table` | Update to latest code (v1.0.1+)      |

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for more.

---

## ✅ What You Should See

After running, you should see:

```
┌─────────────────────────────────────────────┐
│ [Logo] ELPM v1.0    [Search]    [Controls]  │  ← Top bar
├─────────────────────────────────────────────┤
│ Processes | Process Tree | Network | ...    │  ← Tabs
├─────────────────────────────────────────────┤
│                                             │
│  Process table with 22 entries              │  ← Main content
│  + Process details panel on right           │
│                                             │
├─────────────────────────────────────────────┤
│ CPU: 45% | Memory: 62% | Disk: 78% | Time   │  ← Status bar
└─────────────────────────────────────────────┘
```

**Dark theme, cyan accents, real-time updates!**

---

## 📦 What's Included

- ✅ **Process Monitor**: Table with 22 sample processes
- ✅ **Process Details**: Comprehensive information panel
- ✅ **CPU/Memory Graphs**: Real-time visualization
- ✅ **Search & Filter**: Find processes instantly
- ✅ **Dark Theme**: Security-focused design
- ✅ **Auto-refresh**: 2-second updates

---

## 🎯 Key Features

### Working Now ✅
- Process table with sorting
- Detailed process information
- Real-time graphs (60 seconds)
- Search and filtering
- Color-coded status indicators
- Auto-refresh

### Coming Soon 🚧
- Process Tree view
- Network connections
- Search History
- Real system monitoring (with psutil)
- Signal controls (SIGTERM, SIGKILL, etc.)

---

## 🆘 Need Help?

1. **Installation issues?** → [INSTALL.md](INSTALL.md)
2. **Usage questions?** → [QUICK_START.md](QUICK_START.md)
3. **Errors?** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
4. **Everything?** → [INDEX.md](INDEX.md)

**Quick diagnostic:**
```bash
python diagnose.py
```

---

## 📖 Full Documentation

See **[INDEX.md](INDEX.md)** for complete documentation index with:
- Installation guides
- User manuals
- Technical documentation
- Troubleshooting
- Architecture docs
- Feature lists

**Total docs**: 10 documents, ~25,000 words

---

## 🎓 Learning Path

### Beginner (30 min)
1. Read this file ✓
2. Run installation
3. Read [QUICK_START.md](QUICK_START.md)
4. Explore the app!

### Intermediate (2 hours)
1. [INSTALL.md](INSTALL.md)
2. [README_PYQT.md](README_PYQT.md)
3. [FEATURES.md](FEATURES.md)
4. Customize theme

### Advanced (4 hours)
1. [ARCHITECTURE.md](ARCHITECTURE.md)
2. Review source code
3. Add psutil integration
4. Contribute!

---

## 💻 System Requirements

**Minimum:**
- Python 3.8+
- PyQt6 6.5.0+
- 512 MB RAM
- Any OS (Linux/macOS/Windows)

**Recommended:**
- Python 3.10+
- 1 GB RAM
- 1400×800 display

---

## 🚀 Next Steps

After installation:

1. ✅ **Verify it works** - Run `python diagnose.py`
2. 📚 **Read documentation** - Start with [QUICK_START.md](QUICK_START.md)
3. 🎨 **Customize** - Edit `gui/styles.py`
4. 📊 **Add real data** - Install psutil (see [README_PYQT.md](README_PYQT.md))
5. 🎯 **Contribute** - Review [FEATURES.md](FEATURES.md) for ideas

---

## 📊 Quick Stats

- **Version**: 1.0.1
- **Release Date**: 2025-10-08
- **Language**: Python 3.8+
- **Framework**: PyQt6
- **Default Window**: 1400×800
- **Sample Processes**: 22
- **Theme**: Dark (#1a1a1a)
- **Primary Color**: Cyan (#00d4ff)

---

## ✨ At a Glance

```
┌─────────────────────────────────────────────────────────────┐
│  ELPM - Enhanced Linux Process Monitor                      │
│  ───────────────────────────────────────────────────────    │
│                                                             │
│  ✓ Professional dark theme                                  │
│  ✓ Real-time process monitoring                             │
│  ✓ CPU & Memory graphs                                      │
│  ✓ Advanced filtering & search                              │
│  ✓ Color-coded severity levels                              │
│  ✓ Security-focused design                                  │
│                                                             │
│  📦 Installation: 2 minutes                                 │
│  🎯 Use case: Security professionals, sysadmins             │
│  🌟 Status: Ready to use!                                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎉 Ready?

**Let's go!**

```bash
# 1. Navigate to src
cd /path/to/elpm-desktop/src

# 2. Run launcher (or install manually)
./run_elpm.sh    # Linux/macOS
run_elpm.bat     # Windows

# 3. Enjoy ELPM! 🚀
```

---

**Last Updated**: 2025-10-08 | **Version**: 1.0.1 | **Status**: ✅ Production Ready

**Questions?** See [INDEX.md](INDEX.md) for all documentation.
