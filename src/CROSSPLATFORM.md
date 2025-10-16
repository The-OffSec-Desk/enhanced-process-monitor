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

### All Platforms (Clone & Run)

The quickest way to get ELPM running on any platform is to clone the repository and run the executable:

1. Clone the repository:
   ```bash
   git clone https://github.com/The-OffSec-Desk/enhanced-process-monitor.git
   cd enhanced-process-monitor/src
   ```

2. Make the executable (Linux/macOS only):
   ```bash
   chmod +x dist/ELPM
   ```

3. Run it:
   ```bash
   # Linux/macOS
   ./dist/ELPM

   # Windows
   dist\ELPM.exe
   ```

### Platform-Specific Notes

**Linux**
- The executable is at `dist/ELPM`
- Make it executable first: `chmod +x dist/ELPM`
- Optional: Create a desktop shortcut or add to your PATH for easy access

**macOS**
- The executable is at `dist/ELPM`
- On first launch, you may see a security warning
- If you get "cannot be opened because the developer cannot be verified":
  - Right-click the app and select "Open"
  - Or go to System Settings → Privacy & Security → Allow anyway

**Windows**
- The executable is at `dist\ELPM.exe`
- Double-click to run or execute from command prompt
- Windows Defender may ask for permission — click "Run anyway"

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
