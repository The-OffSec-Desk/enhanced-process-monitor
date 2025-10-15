"""
Process Tree View - Hierarchical process display with enhanced UI
"""

import psutil
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QBrush, QColor, QFont
from PyQt6.QtWidgets import (
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class ProcessTreeView(QWidget):
    """Enhanced process tree view with modern styling"""

    def __init__(self):
        super().__init__()
        self.search_text = ""
        self.show_threads = False
        self.init_ui()

        # Auto-refresh timer
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.populate_process_tree)
        self.refresh_timer.start(3000)  # Refresh every 3 seconds

    def init_ui(self):
        """Initialize UI with styling"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Tree widget with custom styling
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(
            ["PID", "Process Name", "CPU%", "MEM%", "Status", "User"]
        )
        self.tree_widget.setAlternatingRowColors(True)
        self.tree_widget.setAnimated(True)
        self.tree_widget.setIndentation(20)

        # Control bar
        control_bar = self.create_control_bar()
        layout.addWidget(control_bar)

        # Set column widths
        self.tree_widget.setColumnWidth(0, 80)  # PID
        self.tree_widget.setColumnWidth(1, 350)  # Process Name
        self.tree_widget.setColumnWidth(2, 80)  # CPU%
        self.tree_widget.setColumnWidth(3, 80)  # MEM%
        self.tree_widget.setColumnWidth(4, 100)  # Status
        self.tree_widget.setColumnWidth(5, 120)  # User

        # Apply dark theme styling
        self.tree_widget.setStyleSheet(
            """
            QTreeWidget {
                background-color: #1a1a1a;
                color: #e0e0e0;
                border: none;
                font-size: 11px;
                outline: none;
            }
            QTreeWidget::item {
                padding: 4px;
                border: none;
            }
            QTreeWidget::item:hover {
                background-color: #2d2d2d;
            }
            QTreeWidget::item:selected {
                background-color: #00d4ff;
                color: #1a1a1a;
            }
            QTreeWidget::branch {
                background-color: #1a1a1a;
            }
            QTreeWidget::branch:has-children:!has-siblings:closed,
            QTreeWidget::branch:closed:has-children:has-siblings {
                border-image: none;
                image: url(none);
            }
            QTreeWidget::branch:open:has-children:!has-siblings,
            QTreeWidget::branch:open:has-children:has-siblings {
                border-image: none;
                image: url(none);
            }
            QHeaderView::section {
                background-color: #2d2d2d;
                color: #00d4ff;
                padding: 8px;
                border: none;
                border-right: 1px solid #3a3a3a;
                border-bottom: 1px solid #3a3a3a;
                font-weight: bold;
                font-size: 11px;
            }
            QScrollBar:vertical {
                background-color: #1a1a1a;
                width: 12px;
                border: none;
            }
            QScrollBar::handle:vertical {
                background-color: #3a3a3a;
                border-radius: 6px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: #4a4a4a;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """
        )

        layout.addWidget(self.tree_widget)

        # Initial population
        self.populate_process_tree()

    def create_control_bar(self):
        """Create control bar with filters"""
        control_bar = QFrame()
        control_bar.setStyleSheet(
            """
            QFrame {
                background-color: #2d2d2d;
                border-bottom: 1px solid #3a3a3a;
            }
        """
        )
        control_bar.setFixedHeight(50)

        layout = QHBoxLayout(control_bar)
        layout.setContentsMargins(16, 0, 16, 0)
        layout.setSpacing(16)

        # Title
        title = QLabel("🌲 Process Tree")
        title.setStyleSheet(
            """
            color: #00d4ff;
            font-size: 14px;
            font-weight: bold;
        """
        )
        layout.addWidget(title)

        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search processes...")
        self.search_box.setFixedWidth(250)
        self.search_box.textChanged.connect(self.on_search_changed)
        self.search_box.setStyleSheet(
            """
            QLineEdit {
                background-color: #1a1a1a;
                color: #e0e0e0;
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                padding: 6px 12px;
                font-size: 11px;
            }
            QLineEdit:focus {
                border: 1px solid #00d4ff;
            }
        """
        )
        layout.addWidget(self.search_box)

        # Show threads checkbox
        self.threads_cb = QCheckBox("Show threads")
        self.threads_cb.stateChanged.connect(self.on_threads_changed)
        self.threads_cb.setStyleSheet(
            """
            QCheckBox {
                color: #a0a0a0;
                font-size: 11px;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 1px solid #3a3a3a;
                border-radius: 3px;
                background-color: #1a1a1a;
            }
            QCheckBox::indicator:checked {
                background-color: #00d4ff;
                border-color: #00d4ff;
            }
        """
        )
        layout.addWidget(self.threads_cb)

        layout.addStretch()

        # Refresh button
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.clicked.connect(self.populate_process_tree)
        refresh_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #3a3a3a;
                color: #e0e0e0;
                border: none;
                border-radius: 4px;
                padding: 6px 16px;
                font-size: 11px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4a4a4a;
            }
            QPushButton:pressed {
                background-color: #2a2a2a;
            }
        """
        )
        layout.addWidget(refresh_btn)

        # Expand/Collapse buttons
        expand_btn = QPushButton("⊕ Expand All")
        expand_btn.clicked.connect(self.tree_widget.expandAll)
        expand_btn.setStyleSheet(refresh_btn.styleSheet())
        layout.addWidget(expand_btn)

        collapse_btn = QPushButton("⊖ Collapse All")
        collapse_btn.clicked.connect(self.tree_widget.collapseAll)
        collapse_btn.setStyleSheet(refresh_btn.styleSheet())
        layout.addWidget(collapse_btn)

        return control_bar

    def on_search_changed(self, text):
        """Handle search text changes"""
        self.search_text = text.lower()
        self.populate_process_tree()

    def on_threads_changed(self):
        """Handle threads checkbox change"""
        self.show_threads = self.threads_cb.isChecked()
        self.populate_process_tree()

    def populate_process_tree(self):
        """Populate the process tree with enhanced styling"""
        self.tree_widget.clear()
        processes = {}

        # Collect all processes
        for proc in psutil.process_iter(
            [
                "pid",
                "ppid",
                "name",
                "cpu_percent",
                "memory_percent",
                "status",
                "username",
            ]
        ):
            try:
                info = proc.info
                pid = info["pid"]

                # Apply search filter
                if (
                    self.search_text
                    and self.search_text not in str(pid)
                    and self.search_text not in info["name"].lower()
                ):
                    continue

                processes[pid] = {
                    "ppid": info["ppid"],
                    "name": info["name"],
                    "cpu": info.get("cpu_percent", 0.0),
                    "mem": info.get("memory_percent", 0.0),
                    "status": info.get("status", "unknown"),
                    "user": info.get("username", "N/A")[:15],
                    "item": None,
                }
            except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
                continue

        # Create items for all processes
        mono_font = QFont("Consolas", 9)

        for pid, data in processes.items():
            # Create item
            cpu_str = f"{data['cpu']:.1f}%" if data["cpu"] else "0.0%"
            mem_str = f"{data['mem']:.1f}%" if data["mem"] else "0.0%"

            item = QTreeWidgetItem(
                [str(pid), data["name"], cpu_str, mem_str, data["status"], data["user"]]
            )

            # Style the item
            item.setFont(0, mono_font)  # PID
            item.setTextAlignment(
                0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )

            item.setFont(2, mono_font)  # CPU%
            item.setTextAlignment(
                2, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )

            item.setFont(3, mono_font)  # MEM%
            item.setTextAlignment(
                3, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )

            # Color coding
            # CPU color
            cpu_val = data["cpu"]
            if cpu_val > 50:
                item.setForeground(2, QBrush(QColor("#ff6b6b")))
            elif cpu_val > 20:
                item.setForeground(2, QBrush(QColor("#ffd93d")))
            else:
                item.setForeground(2, QBrush(QColor("#51cf66")))

            # Status color
            status_colors = {
                "running": "#51cf66",
                "sleeping": "#4ecdc4",
                "zombie": "#ff6b6b",
                "stopped": "#ffd93d",
                "idle": "#a0a0a0",
            }
            status_color = status_colors.get(data["status"], "#e0e0e0")
            item.setForeground(4, QBrush(QColor(status_color)))

            # Root user highlight
            if data["user"] == "root":
                item.setForeground(5, QBrush(QColor("#ff6347")))

            data["item"] = item

        # Build tree structure
        root_items = []
        for pid, data in processes.items():
            ppid = data["ppid"]
            item = data["item"]

            if ppid in processes and processes[ppid]["item"]:
                # Add as child to parent
                processes[ppid]["item"].addChild(item)
            else:
                # Root process (no parent or parent not found)
                root_items.append(item)

        # Add all root items to tree
        self.tree_widget.addTopLevelItems(root_items)

        # Expand first two levels by default
        if not self.search_text:
            self.tree_widget.expandToDepth(1)
        else:
            # Expand all when searching
            self.tree_widget.expandAll()
