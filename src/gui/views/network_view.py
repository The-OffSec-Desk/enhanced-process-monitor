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
    QTabWidget,
    QFrame,
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont


class NetworkView(QWidget):
    """Enhanced network view showing interfaces and connections."""

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
        title_label = QLabel("🌐 Network Monitor")
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

        # ---- Tab Widget ----
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet(
            """
            QTabWidget::pane {
                border: 1px solid #2D2D2D;
                background-color: #121212;
            }
            QTabBar::tab {
                background-color: #1E1E1E;
                color: #CFCFCF;
                border: 1px solid #2D2D2D;
                padding: 8px 16px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #2A2A2A;
                color: #00d4ff;
            }
            QTabBar::tab:hover {
                background-color: #252525;
            }
        """
        )
        layout.addWidget(self.tab_widget)

        # Interfaces Tab
        self.interfaces_tab = self.create_interfaces_tab()
        self.tab_widget.addTab(self.interfaces_tab, "Interfaces")

        # Connections Tab
        self.connections_tab = self.create_connections_tab()
        self.tab_widget.addTab(self.connections_tab, "Connections")

        self.setLayout(layout)
        self.update_network_data()

    def create_interfaces_tab(self):
        """Create the interfaces statistics tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        self.interfaces_table = QTableWidget(0, 4)
        self.interfaces_table.setHorizontalHeaderLabels(
            ["Interface", "Bytes Sent", "Bytes Received", "Packets Sent/Recv"]
        )
        self.interfaces_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.interfaces_table.setAlternatingRowColors(True)
        self.interfaces_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.interfaces_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.interfaces_table.verticalHeader().setVisible(False)
        self.interfaces_table.setStyleSheet(
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

        layout.addWidget(self.interfaces_table)
        return tab

    def create_connections_tab(self):
        """Create the network connections tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Filter controls
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Filter:"))
        filter_layout.addStretch()

        self.conn_table = QTableWidget(0, 6)
        self.conn_table.setHorizontalHeaderLabels(
            ["PID", "Process", "Protocol", "Local Address", "Remote Address", "Status"]
        )
        self.conn_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.conn_table.setAlternatingRowColors(True)
        self.conn_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.conn_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.conn_table.verticalHeader().setVisible(False)
        self.conn_table.setStyleSheet(self.interfaces_table.styleSheet())

        layout.addLayout(filter_layout)
        layout.addWidget(self.conn_table)
        return tab

    # ------------------------------------------------------------
    # DATA HANDLING
    # ------------------------------------------------------------
    def update_network_data(self):
        """Fetch and display network statistics."""
        self.update_interfaces()
        self.update_connections()

    def update_interfaces(self):
        """Update interface statistics."""
        stats = psutil.net_io_counters(pernic=True)
        self.interfaces_table.setRowCount(0)

        for iface, info in stats.items():
            row = self.interfaces_table.rowCount()
            self.interfaces_table.insertRow(row)

            bytes_sent = self.format_bytes(info.bytes_sent)
            bytes_recv = self.format_bytes(info.bytes_recv)
            packets = f"{info.packets_sent}/{info.packets_recv}"

            self.interfaces_table.setItem(row, 0, QTableWidgetItem(iface))
            self.interfaces_table.setItem(row, 1, QTableWidgetItem(bytes_sent))
            self.interfaces_table.setItem(row, 2, QTableWidgetItem(bytes_recv))
            self.interfaces_table.setItem(row, 3, QTableWidgetItem(packets))

        self.interfaces_table.resizeRowsToContents()

    def update_connections(self):
        """Update network connections."""
        try:
            connections = psutil.net_connections(kind='inet')
            self.conn_table.setRowCount(0)

            for conn in connections:
                try:
                    # Get process name if PID exists
                    proc_name = "N/A"
                    if conn.pid:
                        try:
                            proc = psutil.Process(conn.pid)
                            proc_name = proc.name()[:20]  # Limit length
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass

                    # Format addresses
                    local_addr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                    remote_addr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

                    row = self.conn_table.rowCount()
                    self.conn_table.insertRow(row)

                    self.conn_table.setItem(row, 0, QTableWidgetItem(str(conn.pid or 0)))
                    self.conn_table.setItem(row, 1, QTableWidgetItem(proc_name))
                    self.conn_table.setItem(row, 2, QTableWidgetItem('TCP' if conn.type == 1 else 'UDP'))
                    self.conn_table.setItem(row, 3, QTableWidgetItem(local_addr))
                    self.conn_table.setItem(row, 4, QTableWidgetItem(remote_addr))
                    self.conn_table.setItem(row, 5, QTableWidgetItem(conn.status or 'N/A'))

                except Exception:
                    continue

            self.conn_table.resizeRowsToContents()
        except (psutil.AccessDenied, Exception):
            # Clear table if access denied
            self.conn_table.setRowCount(0)

    def start_auto_refresh(self, interval=5000):
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
