"""
Main Window for ELPM Application
"""

import os

from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtGui import QColor, QIcon, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from gui.styles import STYLESHEET
from gui.views.graphs_view import GraphsView
from gui.views.placeholder_view import PlaceholderView
from gui.views.process_tree_view import ProcessTreeView
from gui.views.processes_view import ProcessesView
from gui.views.network_view import NetworkView
from gui.views.history_view import HistoryView
from gui.widgets.status_bar import StatusBar
from gui.widgets.top_bar import TopBar


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self):

        super().__init__()
        self.setWindowTitle("ELPM - Enhanced Linux Process Monitor")
        self.setGeometry(100, 100, 1400, 800)

        # Apply dark theme stylesheet
        self.setStyleSheet(STYLESHEET)

        # Set dark palette
        self.set_dark_palette()

        # Initialize UI
        self.init_ui()

        # Set only window icon (not the app one)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "../assets/icons/ELPM-preview.png")

        # Normalizing the path (for safety)
        icon_path = os.path.normpath(icon_path)

        print(f"🔍 Checking icon path: {icon_path}")
        print("Icon exists:", os.path.exists(icon_path))

        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print("⚠️ Icon file not found! Check your path.")

        # Setup update timer
        self.setup_timers()

    def set_dark_palette(self):
        """Set dark color palette for the application"""
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#1a1a1a"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#e0e0e0"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#2d2d2d"))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor("#1a1a1a"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#e0e0e0"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#2d2d2d"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#e0e0e0"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#00d4ff"))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor("#1a1a1a"))
        self.setPalette(palette)

    def init_ui(self):
        """Initialize the user interface"""
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Top bar
        self.top_bar = TopBar()
        main_layout.addWidget(self.top_bar)

        # Tab widget for navigation
        self.tab_widget = QTabWidget()
        self.tab_widget.setObjectName("mainTabs")
        self.tab_widget.setDocumentMode(True)

        # Add tabs
        self.history_view = HistoryView()
        self.processes_view = ProcessesView(history_callback=self.history_view)
        self.tab_widget.addTab(self.processes_view, "⚡ Processes")

        self.process_tree_view = ProcessTreeView()
        self.tab_widget.addTab(self.process_tree_view, "🌲 Process Tree")

        self.network_view = NetworkView()
        self.tab_widget.addTab(self.network_view, "🌐 Network")

        self.graphs_view = GraphsView()
        self.tab_widget.addTab(self.graphs_view, "📊 Graphs")

        self.tab_widget.addTab(self.history_view, "🕐 Activity History")

        main_layout.addWidget(self.tab_widget)

        # Status bar
        self.status_bar_widget = StatusBar()
        main_layout.addWidget(self.status_bar_widget)

        # Connect search functionality
        self.top_bar.search_changed.connect(self.on_search_changed)
        self.top_bar.refresh_clicked.connect(self.on_refresh_clicked)
        self.top_bar.fullscreen_toggled.connect(self.toggle_fullscreen)

    def setup_timers(self):
        """Setup update timers"""
        # Update status bar every second
        self.status_timer = QTimer()
        self.status_timer.timeout.connect(self.update_status_bar)
        self.status_timer.start(1000)

        # Process list has its own timer in ProcessesView
        # Graphs timer
        self.graph_timer = QTimer()
        self.graph_timer.timeout.connect(self.graphs_view.update_graphs)
        self.graph_timer.start(2000)  # Update every 2 seconds

    def update_status_bar(self):
        """Update status bar with current process count"""
        process_count = len(self.processes_view.processes)
        self.status_bar_widget.update_stats(process_count)

    def on_search_changed(self, query: str):
        """Handle search query changes"""
        self.processes_view.set_search_text(query)
        if query.strip():
            self.history_view.add_search_entry(query)

    def on_refresh_clicked(self):
        """Handle refresh button click"""
        self.processes_view.refresh_processes()
        self.graphs_view.update_graphs()
        self.update_status_bar()

    def toggle_fullscreen(self):
        """Toggle full screen mode"""
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
