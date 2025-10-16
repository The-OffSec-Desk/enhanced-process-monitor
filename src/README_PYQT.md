# ELPM - Enhanced Linux Process Monitor (PyQt6)

## Overview

This is the PyQt6 desktop application version of ELPM (Enhanced Linux Process Monitor), a security-focused system monitoring tool designed for security professionals, SOC analysts, and system administrators.

## Features

- **Real-time Process Monitoring**: View all running processes with detailed information
- **Process Details Panel**: Comprehensive information about selected processes
- **CPU & Memory Graphs**: Real-time visualization of system resource usage
- **Advanced Filtering**: Filter by process name, PID, user, and command
- **Dark Theme**: Optimized for extended monitoring sessions
- **Signal Control**: Send SIGTERM, SIGKILL, SIGSTOP, and SIGCONT signals to processes
- **Color-Coded Status**: Quick visual identification of critical processes and resource usage

## Project Structure

```
elpm/
├── elpm_main.py          # Main application entry point
├── models/
│   ├── __init__.py
│   └── process_model.py  # Process data model
├── gui/
│   ├── __init__.py
│   ├── main_window.py    # Main application window
│   ├── styles.py         # Application-wide stylesheets
│   ├── widgets/          # Reusable widgets
│   │   ├── __init__.py
│   │   ├── top_bar.py    # Top bar with branding and search
│   │   └── status_bar.py # Bottom status bar with system stats
│   └── views/            # Main view components
│       ├── __init__.py
│       ├── processes_view.py    # Process table and details
│       ├── graphs_view.py       # CPU/Memory graphs
│       └── placeholder_view.py  # Placeholder for unimplemented tabs
└── README_PYQT.md        # This file
```

## Requirements

- Python 3.8 or higher
- PyQt6

## Installation

1. Install Python 3.8 or higher
2. Install PyQt6:

```bash
pip install PyQt6
```

## Running the Application

To run ELPM, execute:

```bash
python elpm_main.py
# or
python3 elpm_main.py
```

**First time setup test:**

```bash
# Test if all imports work correctly
python test_imports.py
```

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError: No module named 'PyQt6'`:

```bash
# Make sure PyQt6 is installed
pip install PyQt6
# or for Python 3
pip3 install PyQt6
```

### "No module named 'gui'" or "No module named 'models'"

Make sure you're running the script from the correct directory:

```bash
cd /path/to/elpm-desktop/src
python elpm_main.py
```

Or add the src directory to your Python path:

```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/elpm-desktop/src"
```

### Display Issues

If you experience scaling issues on high-DPI displays:

```bash
# Set Qt scaling environment variable
export QT_AUTO_SCREEN_SCALE_FACTOR=1
python elpm_main.py
```

## Usage

### Main Window

The application window consists of:

1. **Top Bar**: Application branding, search functionality, and window controls
2. **Tab Navigation**: Switch between Processes, Process Tree, Network, Graphs, and Search History views
3. **Main Content Area**: Current tab's content
4. **Status Bar**: Real-time system statistics (CPU, Memory, Disk usage, process count, time)

### Processes View

- **Process Table**: Displays all running processes with sortable columns
- **Details Panel**: Shows comprehensive information about the selected process
- **Filters**:
  - Sort by CPU%, Memory%, PID, or Name
  - Filter by root user only
  - Hide kernel threads
  - Toggle auto-refresh
- **Signal Controls**: Send signals to processes (SIGTERM, SIGKILL, SIGSTOP, SIGCONT)

### Graphs View

- **CPU Usage Graph**: Real-time CPU usage over the last 60 seconds
- **Memory Usage Graph**: Real-time memory usage over the last 60 seconds
- **Statistics Panel**: Shows average, maximum, and minimum values

### Search

Use the search bar in the top bar to filter processes by:
- Process name
- PID (Process ID)
- Command/executable path

## Color Coding

- **Cyan (#00d4ff)**: Primary actions and highlights
- **Red (#ff6b6b)**: Critical items (high CPU/memory, zombie processes, SIGKILL)
- **Green (#51cf66)**: Running processes, normal operation, SIGTERM
- **Yellow (#ffd93d)**: Warnings, stopped processes, SIGSTOP
- **Cyan (#4ecdc4)**: Sleeping processes, SIGCONT
- **Orange (#ffa500)**: Files & network connections section
- **Purple (#7c3aed)**: Command section

## Customization

### Modifying the Theme

Edit `gui/styles.py` to customize the application's appearance. The file contains all CSS-like stylesheet definitions.


### Adding Signal Functionality (In case you don't see any)

Connect the signal buttons in `gui/views/processes_view.py` to actual signal sending:

```python
import os
import signal

def send_signal(self, sig):
    if self.selected_process:
        try:
            os.kill(self.selected_process.pid, sig)
        except OSError as e:
            # Handle error
            pass
```

## Development

### Adding New Tabs

1. Create a new view in `gui/views/`
2. Import and add it to the tab widget in `gui/main_window.py`
3. Optionally add update logic in the timer callbacks

### Adding New Features

- **Custom widgets**: Add to `gui/widgets/`
- **Data models**: Add to `models/`
- **Utilities**: Create a new `utils/` directory

## License

This application is provided as-is for educational and professional use.

## Support

For issues, questions, or contributions, please refer to the project repository.
