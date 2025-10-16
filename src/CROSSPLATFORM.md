# ELPM - Cross-Platform Installation Guide

Welcome! ELPM (Enhanced Linux Process Monitor) is now available as standalone executables for Windows, macOS, and Linux. No installation required — just download and run.

## What's New

ELPM has been packaged as native executables for all major operating systems using PyInstaller. This means:

- **No Python installation required** — Everything is bundled together
- **No dependencies to install** — PyQt6 and psutil are included
- **Full system access** — The app can monitor all system processes without sandbox restrictions
- **One-click launch** — Download, make executable, and run

## System Requirements

### Linux
- **OS:** Any Linux distribution (tested on Fedora 42, should work on Ubuntu, Debian, Arch, etc.)
- **Architecture:** x86_64 (64-bit)
- **RAM:** 256MB minimum
- **Dependencies:** None (all bundled)

### macOS
- **OS:** macOS 10.13 or later
- **Architecture:** Intel x86_64 (M1/M2/M3 support coming soon)
- **RAM:** 256MB minimum
- **Dependencies:** None (all bundled)

### Windows
- **OS:** Windows 10 or later
- **Architecture:** 64-bit
- **RAM:** 256MB minimum
- **Dependencies:** None (all bundled)

## Installation

### Linux

1. Download `ELPM` from the releases page
2. Make it executable:
   ```bash
   chmod +x ELPM
   ```
3. Run it:
   ```bash
   ./ELPM
   ```

**Optional:** Create a desktop shortcut or add to your applications menu:
```bash
cp ELPM ~/.local/bin/ELPM
```

### macOS

1. Download `ELPM.app` from the releases page
2. Move it to your Applications folder:
   ```bash
   mv ELPM.app /Applications/
   ```
3. Launch it from Applications or Spotlight search

**Note:** On first launch, macOS may ask for permission. Click "Open" when prompted.

If you get a "cannot be opened because the developer cannot be verified" error:
- Right-click the app and select "Open"
- Or go to System Settings → Privacy & Security → Allow anyway

### Windows

1. Download `ELPM.exe` from the releases page
2. Double-click to run (or place it anywhere in your PATH for command-line access)
3. The app will start immediately

**Optional:** Create a shortcut on your desktop by right-clicking the `.exe` file and selecting "Create shortcut"

## Usage

Once launched, ELPM provides:

- **Process monitoring** — Real-time view of all running processes
- **CPU/Memory tracking** — Monitor resource usage per process
- **Process tree** — View parent-child process relationships
- **Network monitoring** — See network connections
- **Search & filter** — Find specific processes quickly
- **Export data** — Save process data to CSV

## Building from Source

If you want to build the executable for your specific OS:

### Requirements
- Python 3.11 or higher
- PyQt6 and psutil packages

### Build Steps

```bash
# Clone the repository
git clone https://github.com/The-OffSec-Desk/enhanced-process-monitor.git
cd enhanced-process-monitor/src

# Install dependencies
pip install PyQt6 psutil pyinstaller

# Build the executable
python3 -m PyInstaller --onefile --windowed --name ELPM elpm_main.py

# The executable will be in dist/ELPM (or dist/ELPM.exe on Windows)
```

## Troubleshooting

### "App cannot be opened" (macOS)
- Right-click the app and select "Open"
- Go to System Settings → Privacy & Security → Allow anyway

### "Permission denied" (Linux)
- Ensure the file is executable: `chmod +x ELPM`
- Try running with `./ELPM` instead of just `ELPM`

### GUI doesn't appear
- On some Linux systems, you may need to install additional graphics libraries
- Try running from terminal to see error messages: `./ELPM`

### No processes showing
- The app requires permission to read process information
- On Linux, all processes should be visible
- On macOS/Windows, some system processes may be restricted

## Architecture Support

Current releases support:
- **Linux:** x86_64
- **macOS:** Intel x86_64 (M1/M2/M3 builds coming soon)
- **Windows:** x86_64

If you need a build for a different architecture (ARM, ARM64, etc.), you can build it yourself following the "Building from Source" section.

## Contributing & Support

Found a bug or have a feature request? Visit the GitHub repository:
https://github.com/The-OffSec-Desk/enhanced-process-monitor

## License

See the LICENSE file in the repository for details.

---

Enjoy monitoring your processes across all platforms!
