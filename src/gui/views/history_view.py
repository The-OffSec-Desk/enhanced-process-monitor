"""
History View - Displays user's past search/filter history
"""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QFrame,
    QListWidget,
    QListWidgetItem,
)
from PyQt6.QtGui import QFont, QColor, QBrush
from PyQt6.QtCore import Qt


class HistoryView(QWidget):
    """Stylish placeholder and functional list for search history"""

    def __init__(self):
        super().__init__()
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

        title = QLabel("🕐 Search History")
        title.setStyleSheet(
            """
            color: #00d4ff;
            font-size: 14px;
            font-weight: bold;
        """
        )
        header_layout.addWidget(title)
        layout.addWidget(header)

        # --- History list (empty initially) ---
        self.history_list = QListWidget()
        self.history_list.setAlternatingRowColors(True)
        self.history_list.setStyleSheet(
            """
            QListWidget {
                background-color: #1a1a1a;
                color: #e0e0e0;
                border: none;
                font-size: 11px;
            }
            QListWidget::item {
                padding: 8px;
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
        layout.addWidget(self.history_list)

        # --- Placeholder message ---
        self.placeholder = QLabel(
            "No search history yet\nStart filtering processes to build your search history"
        )
        self.placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.placeholder.setStyleSheet(
            """
            QLabel {
                color: #777;
                font-size: 12px;
                padding: 40px;
            }
        """
        )
        layout.addWidget(self.placeholder)

        self.refresh_visibility()

    def refresh_visibility(self):
        """Show placeholder when no history exists"""
        has_history = self.history_list.count() > 0
        self.history_list.setVisible(has_history)
        self.placeholder.setVisible(not has_history)

    def add_history_entry(self, query_text: str):
        """Add a search/filter entry to the history list"""
        if not query_text.strip():
            return

        item = QListWidgetItem(f"🔍  {query_text}")
        font = QFont("Consolas", 10)
        item.setFont(font)
        item.setForeground(QBrush(QColor("#00d4ff")))

        self.history_list.insertItem(0, item)  # Insert at top (most recent first)
        self.refresh_visibility()
