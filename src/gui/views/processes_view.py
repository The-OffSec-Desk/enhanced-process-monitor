"""
Processes view with process table and details panel - with real process monitoring
"""

import csv
import os
import signal as sig_module
import subprocess
from datetime import datetime

import psutil
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QBrush, QColor, QFont
from PyQt6.QtWidgets import (QCheckBox, QComboBox, QFileDialog, QFrame,
                             QHBoxLayout, QHeaderView, QLabel, QMessageBox,
                             QProgressBar, QPushButton, QScrollArea,
                             QTableWidget, QTableWidgetItem, QVBoxLayout,
                             QWidget)

from models.process_model import ProcessModel, format_bytes, get_real_processes


class ProcessesView(QWidget):
    """Main processes view with table and details panel"""

    def __init__(self):
        super().__init__()
        self.processes = []
        self.filtered_processes = []
        self.selected_process = None
        self.search_text = ""
        self.init_ui()

        # Start refresh timer
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.refresh_processes)
        self.refresh_timer.start(2000)  # Refresh every 2 seconds

    def init_ui(self):
        """Initialize UI components"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Left panel - Process table (70%)
        left_panel = QWidget()
        left_panel.setMinimumWidth(700)
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)

        # Control bar
        control_bar = self.create_control_bar()
        left_layout.addWidget(control_bar)

        # Process table
        self.process_table = self.create_process_table()
        left_layout.addWidget(self.process_table)

        layout.addWidget(left_panel, 7)

        # Right panel - Details (30%)
        right_panel = self.create_details_panel()
        layout.addWidget(right_panel, 3)

        # Load initial data
        self.refresh_processes()

    def create_control_bar(self):
        """Create control bar with filters and options"""
        control_bar = QFrame()
        control_bar.setStyleSheet(
            "background-color: #2d2d2d; border-bottom: 1px solid #3a3a3a;"
        )
        control_bar.setFixedHeight(40)

        layout = QHBoxLayout(control_bar)
        layout.setContentsMargins(16, 0, 16, 0)
        layout.setSpacing(16)

        # Sort by
        sort_label = QLabel("Sort by:")
        sort_label.setStyleSheet("color: #a0a0a0; font-size: 11px;")
        layout.addWidget(sort_label)

        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["CPU%", "Memory%", "PID", "Name"])
        self.sort_combo.currentTextChanged.connect(self.apply_filters)
        layout.addWidget(self.sort_combo)

        # Checkboxes
        self.root_only_cb = QCheckBox("Root only")
        self.root_only_cb.stateChanged.connect(self.apply_filters)
        layout.addWidget(self.root_only_cb)

        self.hide_kernel_cb = QCheckBox("Hide kernel threads")
        self.hide_kernel_cb.stateChanged.connect(self.apply_filters)
        layout.addWidget(self.hide_kernel_cb)

        self.auto_refresh_cb = QCheckBox("Auto-refresh (2s)")
        self.auto_refresh_cb.setChecked(True)
        self.auto_refresh_cb.stateChanged.connect(self.toggle_auto_refresh)
        layout.addWidget(self.auto_refresh_cb)

        layout.addStretch()

        # Export button
        export_btn = QPushButton("📥 Export CSV")
        export_btn.setStyleSheet("font-size: 11px;")
        export_btn.clicked.connect(self.export_csv)
        layout.addWidget(export_btn)

        return control_bar

    def create_process_table(self):
        """Create the process table"""
        table = QTableWidget()
        table.setColumnCount(9)
        table.setHorizontalHeaderLabels(
            [
                "PID",
                "User",
                "CPU%",
                "MEM%",
                "VSZ",
                "RSS",
                "Status",
                "Threads",
                "Command",
            ]
        )

        # Set column widths
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(0, 70)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(1, 100)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(2, 80)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(3, 80)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(4, 90)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(5, 90)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(6, 90)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(7, 70)
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Stretch)

        # Enable alternating row colors
        table.setAlternatingRowColors(True)

        # Connect selection
        table.itemSelectionChanged.connect(self.on_process_selected)

        return table

    def refresh_processes(self):
        """Refresh process list from system"""
        # Get real processes
        self.processes = get_real_processes()
        self.apply_filters()

    def apply_filters(self):
        """Apply filters and sorting to process list"""
        filtered = self.processes.copy()

        # Apply root only filter
        if self.root_only_cb.isChecked():
            filtered = [p for p in filtered if p.user == "root"]

        # Apply hide kernel threads filter
        if self.hide_kernel_cb.isChecked():
            filtered = [p for p in filtered if not p.command.startswith("[")]

        # Apply search filter
        if self.search_text:
            search_lower = self.search_text.lower()
            filtered = [
                p
                for p in filtered
                if search_lower in p.command.lower()
                or search_lower in str(p.pid)
                or search_lower in p.user.lower()
            ]

        # Apply sorting
        sort_by = self.sort_combo.currentText()
        if sort_by == "CPU%":
            filtered.sort(key=lambda x: x.cpu, reverse=True)
        elif sort_by == "Memory%":
            filtered.sort(key=lambda x: x.mem, reverse=True)
        elif sort_by == "PID":
            filtered.sort(key=lambda x: x.pid)
        elif sort_by == "Name":
            filtered.sort(key=lambda x: x.command.lower())

        self.filtered_processes = filtered
        self.populate_table()

    def populate_table(self):
        """Populate the process table with data"""
        self.process_table.setRowCount(len(self.filtered_processes))

        mono_font = QFont("Consolas", 9)

        for row, process in enumerate(self.filtered_processes):
            # PID
            pid_item = QTableWidgetItem(str(process.pid))
            pid_item.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            pid_item.setFont(mono_font)
            self.process_table.setItem(row, 0, pid_item)

            # User
            user_item = QTableWidgetItem(process.user[:15])
            if process.user == "root":
                user_item.setForeground(QBrush(QColor("#ff6347")))
            self.process_table.setItem(row, 1, user_item)

            # CPU%
            cpu_item = QTableWidgetItem(f"{process.cpu:.1f}")
            cpu_item.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            cpu_item.setFont(mono_font)
            cpu_color = self.get_cpu_color(process.cpu)
            cpu_item.setForeground(QBrush(QColor(cpu_color)))
            if process.cpu > 70:
                cpu_item.setBackground(QBrush(QColor("#ff6b6b").darker(300)))
            self.process_table.setItem(row, 2, cpu_item)

            # MEM%
            mem_item = QTableWidgetItem(f"{process.mem:.1f}")
            mem_item.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            mem_item.setFont(mono_font)
            if process.mem > 10:
                mem_item.setBackground(QBrush(QColor("#ff6b6b").darker(300)))
            self.process_table.setItem(row, 3, mem_item)

            # VSZ
            vsz_item = QTableWidgetItem(format_bytes(process.vsz))
            vsz_item.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            vsz_item.setFont(mono_font)
            vsz_item.setForeground(QBrush(QColor("#a0a0a0")))
            self.process_table.setItem(row, 4, vsz_item)

            # RSS
            rss_item = QTableWidgetItem(format_bytes(process.rss))
            rss_item.setTextAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter
            )
            rss_item.setFont(mono_font)
            rss_item.setForeground(QBrush(QColor("#a0a0a0")))
            self.process_table.setItem(row, 5, rss_item)

            # Status
            status_item = QTableWidgetItem(process.status)
            status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            status_color = self.get_status_color(process.status)
            status_item.setForeground(QBrush(QColor(status_color)))
            self.process_table.setItem(row, 6, status_item)

            # Threads
            threads_item = QTableWidgetItem(str(process.threads))
            threads_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            threads_item.setFont(mono_font)
            self.process_table.setItem(row, 7, threads_item)

            # Command
            cmd_item = QTableWidgetItem(process.command[:80])
            self.process_table.setItem(row, 8, cmd_item)

    def create_details_panel(self):
        """Create the right details panel"""
        panel = QFrame()
        panel.setObjectName("detailsPanel")
        panel.setMinimumWidth(300)

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header
        header = QFrame()
        header.setStyleSheet(
            "background-color: #2d2d2d; border-bottom: 1px solid #3a3a3a; padding: 12px;"
        )
        header_layout = QVBoxLayout(header)
        title = QLabel("Process Details")
        title.setStyleSheet("font-weight: bold; font-size: 13px;")
        header_layout.addWidget(title)
        layout.addWidget(header)

        # Scrollable details area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)

        self.details_widget = QWidget()
        self.details_layout = QVBoxLayout(self.details_widget)
        self.details_layout.setContentsMargins(16, 16, 16, 16)
        self.details_layout.setSpacing(16)

        scroll.setWidget(self.details_widget)
        layout.addWidget(scroll)

        # Action buttons with colors
        actions_frame = QFrame()
        actions_frame.setStyleSheet(
            "background-color: #2d2d2d; border-top: 1px solid #3a3a3a; padding: 16px;"
        )
        actions_layout = QVBoxLayout(actions_frame)
        actions_layout.setSpacing(8)

        # SIGTERM button (Green)
        self.sigterm_btn = QPushButton("✓ SIGTERM (15)")
        self.sigterm_btn.setFixedHeight(40)
        self.sigterm_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #283618;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #344a1f;
            }
            QPushButton:pressed {
                background-color: #1f2914;
            }
        """
        )
        self.sigterm_btn.clicked.connect(
            lambda: self.send_signal(sig_module.SIGTERM, "SIGTERM")
        )
        actions_layout.addWidget(self.sigterm_btn)

        # SIGKILL button (Red)
        self.sigkill_btn = QPushButton("⚡ SIGKILL (9)")
        self.sigkill_btn.setFixedHeight(40)
        self.sigkill_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #F71735;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ff2547;
            }
            QPushButton:pressed {
                background-color: #d10f28;
            }
        """
        )
        self.sigkill_btn.clicked.connect(
            lambda: self.send_signal(sig_module.SIGKILL, "SIGKILL")
        )
        actions_layout.addWidget(self.sigkill_btn)

        # SIGSTOP button (Orange/Yellow)
        self.sigstop_btn = QPushButton("⏸ SIGSTOP (19)")
        self.sigstop_btn.setFixedHeight(40)
        self.sigstop_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #F3CA40;
                color: #1a1a1a;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ffd954;
            }
            QPushButton:pressed {
                background-color: #d9b52c;
            }
        """
        )
        self.sigstop_btn.clicked.connect(
            lambda: self.send_signal(sig_module.SIGSTOP, "SIGSTOP")
        )
        actions_layout.addWidget(self.sigstop_btn)

        # SIGCONT button (Blue)
        self.sigcont_btn = QPushButton("▶ SIGCONT (18)")
        self.sigcont_btn.setFixedHeight(40)
        self.sigcont_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #090446;
                color: white;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0d0662;
            }
            QPushButton:pressed {
                background-color: #060330;
            }
        """
        )
        self.sigcont_btn.clicked.connect(
            lambda: self.send_signal(sig_module.SIGCONT, "SIGCONT")
        )
        actions_layout.addWidget(self.sigcont_btn)

        layout.addWidget(actions_frame)

        return panel

    def send_signal(self, signal, signal_name):
        """Send signal to selected process"""
        if not self.selected_process:
            QMessageBox.warning(self, "No Selection", "Please select a process first")
            return

        pid = self.selected_process.pid
        proc_name = (
            self.selected_process.command.split()[0]
            if self.selected_process.command
            else "Unknown"
        )

        # Confirm with user
        reply = QMessageBox.question(
            self,
            "Confirm Signal",
            f"Send {signal_name} to:\n\n"
            f"PID: {pid}\n"
            f"Name: {proc_name}\n\n"
            f"Continue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        try:
            # Try to send signal directly
            os.kill(pid, signal)
            QMessageBox.information(self, "Success", f"{signal_name} sent to PID {pid}")
            # Refresh after a short delay
            QTimer.singleShot(500, self.refresh_processes)

        except PermissionError:
            # Try with sudo
            reply = QMessageBox.question(
                self,
                "Permission Required",
                "Permission denied. Try with sudo privileges?\n\n"
                "Note: This will prompt for your password in terminal.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )

            if reply == QMessageBox.StandardButton.Yes:
                try:
                    result = subprocess.run(
                        ["sudo", "kill", f"-{signal}", str(pid)],
                        capture_output=True,
                        text=True,
                        timeout=30,
                    )

                    if result.returncode == 0:
                        QMessageBox.information(
                            self, "Success", f"{signal_name} sent to PID {pid}"
                        )
                        QTimer.singleShot(500, self.refresh_processes)
                    else:
                        QMessageBox.critical(self, "Error", f"Failed: {result.stderr}")

                except subprocess.TimeoutExpired:
                    QMessageBox.critical(self, "Error", "Command timed out")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Failed: {str(e)}")

        except ProcessLookupError:
            QMessageBox.critical(self, "Error", "Process no longer exists")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send signal: {str(e)}")

    def export_csv(self):
        """Export current process list to CSV"""
        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Export Process List",
            f"processes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "CSV Files (*.csv)",
        )

        if not filename:
            return

        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    [
                        "PID",
                        "User",
                        "CPU%",
                        "MEM%",
                        "VSZ",
                        "RSS",
                        "Status",
                        "Threads",
                        "Command",
                    ]
                )

                for process in self.filtered_processes:
                    writer.writerow(
                        [
                            process.pid,
                            process.user,
                            f"{process.cpu:.1f}",
                            f"{process.mem:.1f}",
                            format_bytes(process.vsz),
                            format_bytes(process.rss),
                            process.status,
                            process.threads,
                            process.command,
                        ]
                    )

            QMessageBox.information(
                self,
                "Success",
                f"Exported {len(self.filtered_processes)} processes to:\n{filename}",
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export: {str(e)}")

    def toggle_auto_refresh(self):
        """Toggle auto refresh on/off"""
        if self.auto_refresh_cb.isChecked():
            self.refresh_timer.start(2000)
        else:
            self.refresh_timer.stop()

    def set_search_text(self, text):
        """Set search text from main window"""
        self.search_text = text
        self.apply_filters()

    def on_process_selected(self):
        """Handle process selection"""
        selection = self.process_table.selectedItems()
        if not selection:
            return

        row = selection[0].row()
        if row < len(self.filtered_processes):
            self.selected_process = self.filtered_processes[row]
            self.update_details_panel()

    def update_details_panel(self):
        """Update the details panel with selected process info"""
        # Clear existing widgets
        while self.details_layout.count():
            child = self.details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not self.selected_process:
            return

        p = self.selected_process
        mono_font = QFont("Consolas", 9)

        # Process Information Section
        self.add_section_header("Process Information", "#00d4ff")
        self.add_detail_row("PID:", str(p.pid), mono_font)
        proc_name = p.command.split()[0] if p.command else "Unknown"
        self.add_detail_row("Name:", proc_name, mono_font)
        self.add_detail_row(
            "Status:", p.status, mono_font, self.get_status_color(p.status)
        )
        user_color = "#ff6347" if p.user == "root" else "#e0e0e0"
        self.add_detail_row("User:", p.user, mono_font, user_color)
        self.add_detail_row("Parent PID:", str(p.ppid), mono_font, "#00d4ff")

        # Resource Usage Section
        self.add_section_header("Resource Usage", "#ffd93d")
        self.add_detail_row(
            "CPU:", f"{p.cpu:.1f}%", mono_font, self.get_cpu_color(p.cpu)
        )
        self.add_progress_bar(p.cpu, self.get_cpu_color(p.cpu))
        self.add_detail_row("Memory:", f"{p.mem:.1f}%", mono_font)
        mem_color = "#ff6b6b" if p.mem > 10 else "#51cf66"
        self.add_progress_bar(p.mem, mem_color)
        self.add_detail_row("Memory RSS:", format_bytes(p.rss), mono_font)
        self.add_detail_row("Memory VSZ:", format_bytes(p.vsz), mono_font)
        self.add_detail_row("Threads:", str(p.threads), mono_font)

        # Timing Section
        self.add_section_header("Timing", "#51cf66")
        self.add_detail_row("Created:", p.created, mono_font)
        cpu_time_text = f"user={p.cpu_time_user:.1f}s sys={p.cpu_time_sys:.1f}s"
        self.add_detail_row("CPU Time:", cpu_time_text, mono_font)

        # Command Section
        self.add_section_header("Command", "#7c3aed")
        cmd_label = QLabel(p.command)
        cmd_label.setWordWrap(True)
        cmd_label.setStyleSheet(
            "background-color: #1a1a1a; padding: 8px; border-radius: 4px; "
            "color: #e0e0e0; font-family: monospace; font-size: 10px;"
        )
        self.details_layout.addWidget(cmd_label)

        # Working Directory
        self.add_section_header("Working Directory", "#00d4ff")
        cwd_label = QLabel(p.cwd)
        cwd_label.setWordWrap(True)
        cwd_label.setStyleSheet(
            "color: #a0a0a0; font-family: monospace; font-size: 10px;"
        )
        self.details_layout.addWidget(cwd_label)

        # Files & Connections
        self.add_section_header("Files & Connections", "#ffa500")
        self.add_detail_row("Open files:", str(p.open_files), mono_font)
        self.add_detail_row("Network connections:", str(p.network_conns), mono_font)

        self.details_layout.addStretch()

    def add_section_header(self, text, color):
        """Add a colored section header"""
        label = QLabel(f"=== {text} ===")
        label.setStyleSheet(f"color: {color}; font-size: 11px; margin-top: 4px;")
        self.details_layout.addWidget(label)

    def add_detail_row(self, label_text, value_text, font=None, value_color="#e0e0e0"):
        """Add a detail row with label and value"""
        row_widget = QWidget()
        row_layout = QHBoxLayout(row_widget)
        row_layout.setContentsMargins(0, 2, 0, 2)

        label = QLabel(label_text)
        label.setStyleSheet("color: #a0a0a0; font-size: 11px;")
        if font:
            label.setFont(font)
        row_layout.addWidget(label)

        value = QLabel(value_text)
        value.setStyleSheet(f"color: {value_color}; font-size: 11px;")
        if font:
            value.setFont(font)
        value.setAlignment(Qt.AlignmentFlag.AlignRight)
        row_layout.addWidget(value, 1)

        self.details_layout.addWidget(row_widget)

    def add_progress_bar(self, value, color):
        """Add a progress bar"""
        bar = QProgressBar()
        bar.setRange(0, 100)
        bar.setValue(min(int(value), 100))
        bar.setFixedHeight(8)
        bar.setTextVisible(False)
        bar.setStyleSheet(
            f"""
            QProgressBar {{
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                background-color: #1a1a1a;
            }}
            QProgressBar::chunk {{
                background-color: {color};
                border-radius: 3px;
            }}
        """
        )
        self.details_layout.addWidget(bar)

    def get_cpu_color(self, cpu):
        """Get color for CPU usage"""
        if cpu > 70:
            return "#ff6b6b"
        elif cpu > 40:
            return "#ffd93d"
        else:
            return "#51cf66"

    def get_status_color(self, status):
        """Get color for process status"""
        status_colors = {
            "running": "#51cf66",
            "sleeping": "#4ecdc4",
            "zombie": "#ff6b6b",
            "stopped": "#ffd93d",
            "dead": "#ff6b6b",
            "disk-sleep": "#4ecdc4",
            "idle": "#a0a0a0",
        }
        return status_colors.get(status, "#e0e0e0")
