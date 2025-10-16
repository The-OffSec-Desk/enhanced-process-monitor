import psutil
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QHeaderView,
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont


class NetworkView(QWidget):
    """Stylish dark-mode widget displaying live network interface stats."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        self.start_auto_refresh()

    # ------------------------------------------------------------
    # UI SETUP
    # ------------------------------------------------------------
    def init_ui(self):
        """Initialize and style the network view interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(8)

        # ---- Header ----
        header_layout = QHBoxLayout()
        title_label = QLabel("Active Network Interfaces")
        title_label.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #E0E0E0;")

        refresh_btn = QPushButton("↻ Refresh")
        refresh_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        refresh_btn.setFixedWidth(100)
        refresh_btn.clicked.connect(self.update_network_data)
        refresh_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #1E1E1E;
                color: #CFCFCF;
                border: 1px solid #2D2D2D;
                border-radius: 6px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #2A2A2A;
                border: 1px solid #3D3D3D;
            }
        """
        )

        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(refresh_btn)
        layout.addLayout(header_layout)

        # ---- Table ----
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(
            ["Interface", "Bytes Sent", "Bytes Received", "Packets Sent/Recv"]
        )
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet(
            """
            QTableWidget {
                background-color: #121212;
                color: #E0E0E0;
                gridline-color: #2A2A2A;
                selection-background-color: #323232;
                alternate-background-color: #181818;
                border: 1px solid #2D2D2D;
                border-radius: 8px;
            }
            QHeaderView::section {
                background-color: #1C1C1C;
                color: #BBBBBB;
                border: 1px solid #2A2A2A;
                padding: 4px;
            }
        """
        )

        layout.addWidget(self.table)
        self.setLayout(layout)
        self.update_network_data()

    # ------------------------------------------------------------
    # DATA HANDLING
    # ------------------------------------------------------------
    def update_network_data(self):
        """Fetch and display network statistics."""
        stats = psutil.net_io_counters(pernic=True)
        self.table.setRowCount(0)

        for iface, info in stats.items():
            row = self.table.rowCount()
            self.table.insertRow(row)

            bytes_sent = self.format_bytes(info.bytes_sent)
            bytes_recv = self.format_bytes(info.bytes_recv)
            packets = f"{info.packets_sent}/{info.packets_recv}"

            self.table.setItem(row, 0, QTableWidgetItem(iface))
            self.table.setItem(row, 1, QTableWidgetItem(bytes_sent))
            self.table.setItem(row, 2, QTableWidgetItem(bytes_recv))
            self.table.setItem(row, 3, QTableWidgetItem(packets))

        self.table.resizeRowsToContents()

    def start_auto_refresh(self, interval=3000):
        """Start automatic refresh every few seconds."""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_network_data)
        self.timer.start(interval)

    # ------------------------------------------------------------
    # UTILITIES
    # ------------------------------------------------------------
    @staticmethod
    def format_bytes(num):
        """Convert bytes to a human-readable format."""
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if num < 1024:
                return f"{num:.1f} {unit}"
            num /= 1024
        return f"{num:.1f} PB"
