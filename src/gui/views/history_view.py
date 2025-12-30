"""
History View - Displays user's past search/filter history and actions
"""

from datetime import datetime
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QListWidget,
    QListWidgetItem,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QSplitter,
)
from PyQt6.QtGui import QFont, QColor, QBrush, QIcon
from PyQt6.QtCore import Qt, pyqtSignal


class HistoryView(QWidget):
    """Functional history view showing search history and process actions"""

    def __init__(self):
        super().__init__()
        self.search_history = []
        self.action_history = []
        self.init_ui()

    def init_ui(self):
        """Initialize UI layout and appearance"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # --- Top header bar ---
        header = QFrame()
        header.setFixedHeight(50)
        header.setStyleSheet(
            """
            QFrame {
                background-color: #2d2d2d;
                border-bottom: 1px solid #3a3a3a;
            }
        """
        )
        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(16, 8, 16, 8)

        title_layout = QHBoxLayout()
        title = QLabel("🕐 Activity History")
        title.setStyleSheet(
            """
            color: #00d4ff;
            font-size: 14px;
            font-weight: bold;
        """
        )
        title_layout.addWidget(title)

        title_layout.addStretch()

        # Clear button
        clear_btn = QPushButton("🗑 Clear History")
        clear_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #3a3a3a;
                color: #e0e0e0;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
        """
        )
        clear_btn.clicked.connect(self.clear_history)
        title_layout.addWidget(clear_btn)

        header_layout.addLayout(title_layout)
        layout.addWidget(header)

        # --- Splitter for search and actions ---
        splitter = QSplitter(Qt.Orientation.Vertical)
        layout.addWidget(splitter)

        # Search history panel
        search_panel = self.create_history_panel("🔍 Search History", self.search_history)
        splitter.addWidget(search_panel)

        # Action history panel
        action_panel = self.create_history_panel("⚡ Process Actions", self.action_history)
        splitter.addWidget(action_panel)

        # Set splitter proportions
        splitter.setSizes([400, 400])

    def create_history_panel(self, title_text, history_list):
        """Create a history panel"""
        panel = QWidget()
        panel_layout = QVBoxLayout(panel)
        panel_layout.setContentsMargins(16, 16, 16, 16)

        # Panel title
        title = QLabel(title_text)
        title.setStyleSheet("font-size: 13px; font-weight: bold; color: #00d4ff; margin-bottom: 8px;")
        panel_layout.addWidget(title)

        # History list
        list_widget = QListWidget()
        list_widget.setAlternatingRowColors(True)
        list_widget.setStyleSheet(
            """
            QListWidget {
                background-color: #1a1a1a;
                color: #e0e0e0;
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                font-size: 11px;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #2d2d2d;
            }
            QListWidget::item:hover {
                background-color: #2d2d2d;
            }
            QListWidget::item:selected {
                background-color: #00d4ff;
                color: #1a1a1a;
            }
        """
        )
        panel_layout.addWidget(list_widget)

        # Store reference
        if "Search" in title_text:
            self.search_list = list_widget
        else:
            self.action_list = list_widget

        return panel

    def add_search_entry(self, query_text: str):
        """Add a search/filter entry to the history"""
        if not query_text.strip():
            return

        timestamp = datetime.now().strftime("%H:%M:%S")
        entry_text = f"[{timestamp}] 🔍 {query_text}"

        item = QListWidgetItem(entry_text)
        font = QFont("Consolas", 10)
        item.setFont(font)
        item.setForeground(QBrush(QColor("#00d4ff")))

        self.search_list.insertItem(0, item)  # Insert at top
        self.search_history.append(entry_text)

        # Limit to 100 entries
        if self.search_list.count() > 100:
            self.search_list.takeItem(self.search_list.count() - 1)
            self.search_history.pop()

    def add_action_entry(self, action_text: str, success: bool = True):
        """Add a process action entry to the history"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        icon = "✅" if success else "❌"
        color = "#51cf66" if success else "#ff6b6b"
        entry_text = f"[{timestamp}] {icon} {action_text}"

        item = QListWidgetItem(entry_text)
        font = QFont("Consolas", 10)
        item.setFont(font)
        item.setForeground(QBrush(QColor(color)))

        self.action_list.insertItem(0, item)  # Insert at top
        self.action_history.append(entry_text)

        # Limit to 100 entries
        if self.action_list.count() > 100:
            self.action_list.takeItem(self.action_list.count() - 1)
            self.action_history.pop()

    def clear_history(self):
        """Clear all history"""
        self.search_list.clear()
        self.action_list.clear()
        self.search_history.clear()
        self.action_history.clear()
