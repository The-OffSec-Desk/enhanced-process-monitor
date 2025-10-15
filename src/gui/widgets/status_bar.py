"""
Status bar widget showing system statistics
"""

import random
from datetime import datetime
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt


class StatusBar(QFrame):
    """Bottom status bar with system statistics"""
    
    def __init__(self):
        super().__init__()
        self.setObjectName("statusBar")
        self.setFixedHeight(35)
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI components"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(24, 0, 24, 0)
        layout.setSpacing(16)
        
        # Left side - System stats
        self.cpu_label = QLabel("CPU: 45.2%")
        self.cpu_label.setStyleSheet("color: #51cf66; font-size: 11px;")
        layout.addWidget(self.cpu_label)
        
        layout.addWidget(self.create_separator())
        
        self.memory_label = QLabel("Memory: 62.4% (10.0GB / 16GB)")
        self.memory_label.setStyleSheet("color: #a0a0a0; font-size: 11px;")
        layout.addWidget(self.memory_label)
        
        layout.addWidget(self.create_separator())
        
        self.disk_label = QLabel("Disk: 78.3%")
        self.disk_label.setStyleSheet("color: #a0a0a0; font-size: 11px;")
        layout.addWidget(self.disk_label)
        
        # Spacer
        layout.addStretch()
        
        # Right side - Process count and time
        self.process_count_label = QLabel("Processes: 287")
        self.process_count_label.setStyleSheet("color: #a0a0a0; font-size: 11px;")
        layout.addWidget(self.process_count_label)
        
        layout.addWidget(self.create_separator())
        
        self.time_label = QLabel(datetime.now().strftime("%H:%M:%S"))
        self.time_label.setStyleSheet("color: #a0a0a0; font-family: monospace; font-size: 11px;")
        layout.addWidget(self.time_label)
    
    def create_separator(self):
        """Create a vertical separator"""
        separator = QFrame()
        separator.setObjectName("separator")
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFixedWidth(1)
        separator.setStyleSheet("background-color: #3a3a3a;")
        return separator
    
    def update_stats(self, process_count=None):
        """Update status bar statistics with real system data"""
        import psutil
        
        # Get real system stats
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Format memory
        mem_used_gb = mem.used / (1024**3)
        mem_total_gb = mem.total / (1024**3)
        
        cpu_color = "#51cf66" if cpu < 70 else "#ffd93d" if cpu < 85 else "#ff6b6b"
        
        self.cpu_label.setText(f"💻 CPU: {cpu:.1f}%")
        self.cpu_label.setStyleSheet(f"color: {cpu_color}; font-size: 11px;")
        
        self.memory_label.setText(f"💾 Memory: {mem.percent:.1f}% ({mem_used_gb:.1f}GB / {mem_total_gb:.1f}GB)")
        
        self.disk_label.setText(f"💿 Disk: {disk.percent:.1f}%")
        
        # Update process count if provided
        if process_count is not None:
            self.process_count_label.setText(f"Processes: {process_count}")
        
        # Update time
        self.time_label.setText(datetime.now().strftime("%H:%M:%S"))
