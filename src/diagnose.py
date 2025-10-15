#!/usr/bin/env python3
"""
ELPM Diagnostic Tool
Checks system for common issues and provides detailed diagnostic information
"""

import sys
import os
import platform

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def print_check(name, status, message=""):
    """Print a check result"""
    symbol = "✓" if status else "✗"
    color = "\033[92m" if status else "\033[91m"
    reset = "\033[0m"
    print(f"{color}{symbol}{reset} {name}", end="")
    if message:
        print(f": {message}")
    else:
        print()

def main():
    print_header("ELPM System Diagnostics")
    print("Running comprehensive system check...\n")
    
    all_passed = True
    
    # Python Version Check
    print_header("Python Environment")
    
    py_version = sys.version_info
    py_version_str = f"{py_version.major}.{py_version.minor}.{py_version.micro}"
    py_ok = py_version.major == 3 and py_version.minor >= 8
    print_check("Python Version", py_ok, py_version_str)
    if not py_ok:
        print("  ⚠️  Python 3.8 or higher required")
        all_passed = False
    
    # Platform Info
    print_check("Platform", True, f"{platform.system()} {platform.release()}")
    print_check("Architecture", True, platform.machine())
    
    # Python Executable
    print_check("Python Executable", True, sys.executable)
    
    # PyQt6 Check
    print_header("PyQt6 Installation")
    
    try:
        import PyQt6
        pyqt_version = PyQt6.QtCore.PYQT_VERSION_STR
        print_check("PyQt6 Core", True, f"v{pyqt_version}")
    except ImportError as e:
        print_check("PyQt6 Core", False, str(e))
        print("  ⚠️  Install with: pip install PyQt6")
        all_passed = False
        pyqt_version = None
    
    if pyqt_version:
        try:
            from PyQt6.QtWidgets import QApplication
            print_check("PyQt6 Widgets", True)
        except ImportError as e:
            print_check("PyQt6 Widgets", False, str(e))
            all_passed = False
        
        try:
            from PyQt6.QtGui import QFont, QPainter
            print_check("PyQt6 GUI", True)
        except ImportError as e:
            print_check("PyQt6 GUI", False, str(e))
            all_passed = False
    
    # File Structure Check
    print_header("File Structure")
    
    required_files = [
        "elpm_main.py",
        "models/__init__.py",
        "models/process_model.py",
        "gui/__init__.py",
        "gui/main_window.py",
        "gui/styles.py",
        "gui/views/__init__.py",
        "gui/views/processes_view.py",
        "gui/views/graphs_view.py",
        "gui/views/placeholder_view.py",
        "gui/widgets/__init__.py",
        "gui/widgets/top_bar.py",
        "gui/widgets/status_bar.py",
    ]
    
    for file_path in required_files:
        exists = os.path.exists(file_path)
        print_check(file_path, exists)
        if not exists:
            all_passed = False
    
    # Import Checks
    print_header("Module Imports")
    
    try:
        from models.process_model import Process, get_sample_processes
        processes = get_sample_processes()
        print_check("Process Model", True, f"{len(processes)} sample processes")
    except Exception as e:
        print_check("Process Model", False, str(e))
        all_passed = False
    
    try:
        from gui.styles import MAIN_STYLES
        style_len = len(MAIN_STYLES)
        print_check("Styles", True, f"{style_len} characters")
    except Exception as e:
        print_check("Styles", False, str(e))
        all_passed = False
    
    try:
        from gui.widgets.top_bar import TopBarWidget
        print_check("Top Bar Widget", True)
    except Exception as e:
        print_check("Top Bar Widget", False, str(e))
        all_passed = False
    
    try:
        from gui.widgets.status_bar import StatusBarWidget
        print_check("Status Bar Widget", True)
    except Exception as e:
        print_check("Status Bar Widget", False, str(e))
        all_passed = False
    
    try:
        from gui.views.processes_view import ProcessesView
        print_check("Processes View", True)
    except Exception as e:
        print_check("Processes View", False, str(e))
        all_passed = False
    
    try:
        from gui.views.graphs_view import GraphsView
        print_check("Graphs View", True)
    except Exception as e:
        print_check("Graphs View", False, str(e))
        all_passed = False
    
    try:
        from gui.views.placeholder_view import PlaceholderView
        print_check("Placeholder View", True)
    except Exception as e:
        print_check("Placeholder View", False, str(e))
        all_passed = False
    
    # Environment Variables
    print_header("Environment")
    
    pythonpath = os.environ.get('PYTHONPATH', 'Not set')
    print_check("PYTHONPATH", True, pythonpath)
    
    qt_vars = [var for var in os.environ if var.startswith('QT_')]
    if qt_vars:
        for var in qt_vars:
            print_check(var, True, os.environ[var])
    else:
        print("  ℹ️  No Qt environment variables set (this is usually fine)")
    
    # Pip Packages
    print_header("Installed Packages")
    
    try:
        import subprocess
        result = subprocess.run([sys.executable, '-m', 'pip', 'list'], 
                              capture_output=True, text=True)
        packages = result.stdout
        
        # Check for PyQt6
        if 'PyQt6' in packages:
            for line in packages.split('\n'):
                if line.startswith('PyQt6'):
                    print(f"  {line}")
        else:
            print("  ⚠️  PyQt6 not found in pip list")
            all_passed = False
            
    except Exception as e:
        print(f"  ⚠️  Could not list packages: {e}")
    
    # System Resources
    print_header("System Resources")
    
    try:
        import resource
        max_open_files = resource.getrlimit(resource.RLIMIT_NOFILE)
        print_check("Max Open Files", True, f"{max_open_files[0]} / {max_open_files[1]}")
    except:
        print("  ℹ️  Resource limits not available on this platform")
    
    # Current Directory
    print_header("Working Directory")
    
    cwd = os.getcwd()
    print_check("Current Directory", True, cwd)
    
    # Check if we're in the right place
    in_src = os.path.exists('elpm_main.py')
    print_check("In Correct Directory", in_src)
    if not in_src:
        print("  ⚠️  You should be in the 'src' directory")
        print("  💡 Run: cd /path/to/elpm-desktop/src")
        all_passed = False
    
    # Final Summary
    print_header("Diagnostic Summary")
    
    if all_passed:
        print("✅ All checks passed! ELPM should run correctly.")
        print("\nTo start ELPM, run:")
        print("  python elpm_main.py")
        return 0
    else:
        print("❌ Some checks failed. Please review the errors above.")
        print("\nCommon fixes:")
        print("  1. Install PyQt6: pip install PyQt6")
        print("  2. Navigate to src directory: cd /path/to/elpm-desktop/src")
        print("  3. Check Python version: python --version (need 3.8+)")
        print("\nFor more help, see:")
        print("  - INSTALL.md")
        print("  - TROUBLESHOOTING.md")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nDiagnostics interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Diagnostic tool crashed: {e}")
        print("This might indicate a serious problem with your Python installation.")
        sys.exit(1)
