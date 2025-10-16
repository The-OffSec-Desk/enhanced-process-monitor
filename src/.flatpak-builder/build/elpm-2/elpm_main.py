"""
ELPM - Enhanced Linux Process Monitor
PyQt6 Desktop Application
Main application entry point
"""

import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication

from gui.main_window import MainWindow


def main():
    """Initialize and run the ELPM application"""
    # Enable High DPI scaling
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setApplicationName("ELPM")
    app.setApplicationVersion("1.0")
    app.setDesktopFileName("elpmd.desktop")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(base_dir, "assets/icons/ELPM-preview.png")

    app.setWindowIcon(QIcon(icon_path))

    # Set default application font
    font = QFont("Segoe UI", 9)
    app.setFont(font)

    # Create and show main window
    window = MainWindow()
    window.setWindowIcon(QIcon(str(icon_path)))
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
