"""
Quick test script to verify all imports are working
"""

print("Testing imports...")

try:
    from PyQt6.QtWidgets import QApplication
    print("✓ PyQt6.QtWidgets")
except ImportError as e:
    print(f"✗ PyQt6.QtWidgets: {e}")

try:
    from PyQt6.QtCore import Qt
    print("✓ PyQt6.QtCore")
except ImportError as e:
    print(f"✗ PyQt6.QtCore: {e}")

try:
    from PyQt6.QtGui import QFont
    print("✓ PyQt6.QtGui")
except ImportError as e:
    print(f"✗ PyQt6.QtGui: {e}")

try:
    from gui.main_window import MainWindow
    print("✓ gui.main_window")
except ImportError as e:
    print(f"✗ gui.main_window: {e}")

try:
    import psutil
    print("✓ psutil")
except ImportError as e:
    print(f"✗ psutil: {e}")

try:
    from models.process_model import ProcessModel
    print("✓ models.process_model")
except ImportError as e:
    print(f"✗ models.process_model: {e}")

print("\nAll imports successful! Ready to run elpm_main.py")
