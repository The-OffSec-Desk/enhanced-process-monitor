"""
Graphs view showing CPU and Memory usage over time
"""

import random
import math
from collections import deque
import psutil
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush, QLinearGradient, QFont


class GraphWidget(QFrame):
    """Custom widget for drawing line graphs"""
    
    def __init__(self, title, color, unit="%"):
        super().__init__()
        self.title = title
        self.color = QColor(color)
        self.unit = unit
        # Start with empty data - will be filled with real system data
        self.data_points = deque(maxlen=60)
        self.setMinimumHeight(250)
        self.setStyleSheet("background-color: #2d2d2d; border-radius: 8px;")
    
    def add_data_point(self, value):
        """Add a new data point"""
        self.data_points.append(value)
        self.update()
    
    def paintEvent(self, event):
        """Paint the graph"""
        super().paintEvent(event)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Margins
        margin_left = 50
        margin_right = 20
        margin_top = 60
        margin_bottom = 40
        
        graph_width = self.width() - margin_left - margin_right
        graph_height = self.height() - margin_top - margin_bottom
        
        if graph_width <= 0 or graph_height <= 0:
            return
        
        # Draw title
        painter.setPen(QColor("#e0e0e0"))
        painter.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        painter.drawText(20, 30, self.title)
        
        # Draw current value
        current_value = self.data_points[-1] if self.data_points else 0
        painter.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        painter.setPen(self.color)
        value_text = f"{current_value:.1f}{self.unit}"
        painter.drawText(self.width() - 150, 40, value_text)
        
        # Draw grid lines
        painter.setPen(QPen(QColor("#3a3a3a"), 1, Qt.PenStyle.DashLine))
        for i in range(5):
            y = margin_top + (graph_height * i / 4)
            painter.drawLine(margin_left, int(y), margin_left + graph_width, int(y))
            
            # Y-axis labels
            value = 100 - (i * 25)
            painter.setPen(QColor("#a0a0a0"))
            painter.setFont(QFont("Segoe UI", 9))
            painter.drawText(5, int(y + 5), f"{value}%")
            painter.setPen(QPen(QColor("#3a3a3a"), 1, Qt.PenStyle.DashLine))
        
        # Draw X-axis labels
        painter.setPen(QColor("#a0a0a0"))
        painter.setFont(QFont("Segoe UI", 9))
        for i in range(0, 60, 10):
            x = margin_left + (graph_width * i / 59)
            label = f"-{60-i}s"
            painter.drawText(int(x - 15), self.height() - 15, label)
        
        # Draw gradient fill
        if len(self.data_points) > 1:
            gradient = QLinearGradient(0, margin_top, 0, margin_top + graph_height)
            gradient_color = QColor(self.color)
            gradient_color.setAlpha(80)
            gradient.setColorAt(0, gradient_color)
            gradient_color.setAlpha(0)
            gradient.setColorAt(1, gradient_color)
            
            painter.setBrush(QBrush(gradient))
            painter.setPen(Qt.PenStyle.NoPen)
            
            # Create polygon for fill
            from PyQt6.QtGui import QPolygonF
            from PyQt6.QtCore import QPointF
            
            points = [QPointF(margin_left, margin_top + graph_height)]
            for i, value in enumerate(self.data_points):
                x = margin_left + (graph_width * i / max(1, len(self.data_points) - 1))
                y = margin_top + graph_height - (graph_height * value / 100)
                points.append(QPointF(x, y))
            points.append(QPointF(margin_left + graph_width, margin_top + graph_height))
            
            painter.drawPolygon(QPolygonF(points))
        
        # Draw line
        if len(self.data_points) > 1:
            painter.setPen(QPen(self.color, 2))
            for i in range(len(self.data_points) - 1):
                x1 = margin_left + (graph_width * i / max(1, len(self.data_points) - 1))
                y1 = margin_top + graph_height - (graph_height * self.data_points[i] / 100)
                x2 = margin_left + (graph_width * (i + 1) / max(1, len(self.data_points) - 1))
                y2 = margin_top + graph_height - (graph_height * self.data_points[i + 1] / 100)
                painter.drawLine(int(x1), int(y1), int(x2), int(y2))
            
            # Draw dots
            for i, value in enumerate(self.data_points):
                x = margin_left + (graph_width * i / max(1, len(self.data_points) - 1))
                y = margin_top + graph_height - (graph_height * value / 100)
                painter.setBrush(QBrush(self.color))
                painter.drawEllipse(int(x - 2), int(y - 2), 4, 4)


class StatsPanel(QFrame):
    """Statistics panel showing avg, max, min"""
    
    def __init__(self, label, color):
        super().__init__()
        self.label = label
        self.color = color
        self.avg_value = 0
        self.max_value = 0
        self.min_value = 0
        self.setFixedHeight(60)
        self.setStyleSheet("background-color: #2d2d2d; border-radius: 8px;")
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Label
        label_widget = QLabel(f"{self.label}:")
        label_widget.setStyleSheet("color: #a0a0a0; font-size: 12px;")
        layout.addWidget(label_widget)
        
        layout.addStretch()
        
        # Stats
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(24)
        
        self.avg_label = QLabel("Avg: 0.0%")
        self.avg_label.setStyleSheet(f"color: {self.color}; font-family: monospace; font-size: 12px;")
        stats_layout.addWidget(self.avg_label)
        
        self.max_label = QLabel("Max: 0.0%")
        self.max_label.setStyleSheet("color: #ff6b6b; font-family: monospace; font-size: 12px;")
        stats_layout.addWidget(self.max_label)
        
        self.min_label = QLabel("Min: 0.0%")
        self.min_label.setStyleSheet("color: #51cf66; font-family: monospace; font-size: 12px;")
        stats_layout.addWidget(self.min_label)
        
        layout.addLayout(stats_layout)
    
    def update_stats(self, avg, max_val, min_val):
        """Update statistics"""
        self.avg_value = avg
        self.max_value = max_val
        self.min_value = min_val
        self.avg_label.setText(f"Avg: {avg:.1f}%")
        self.max_label.setText(f"Max: {max_val:.1f}%")
        self.min_label.setText(f"Min: {min_val:.1f}%")


class GraphsView(QWidget):
    """Graphs view showing CPU, Memory, Disk, and Network usage history"""
    
    def __init__(self):
        super().__init__()
        self.time_counter = 0
        self.prev_disk_io = psutil.disk_io_counters()
        self.prev_net_io = psutil.net_io_counters()
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI components"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(24)
        
        # CPU Graph
        self.cpu_graph = GraphWidget("CPU Usage History (60 seconds)", "#00d4ff")
        layout.addWidget(self.cpu_graph)
        
        # Memory Graph
        self.memory_graph = GraphWidget("Memory Usage History (60 seconds)", "#ffd93d")
        layout.addWidget(self.memory_graph)
        
        # Create bottom row for Disk and Network
        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(16)
        
        # Disk I/O Graph
        self.disk_graph = GraphWidget("Disk I/O (KB/s)", "#51cf66", "KB/s")
        self.disk_graph.setMinimumHeight(200)
        bottom_layout.addWidget(self.disk_graph)
        
        # Network I/O Graph
        self.network_graph = GraphWidget("Network I/O (KB/s)", "#7c3aed", "KB/s")
        self.network_graph.setMinimumHeight(200)
        bottom_layout.addWidget(self.network_graph)
        
        layout.addLayout(bottom_layout)
        
        # Stats Panel
        stats_container = QWidget()
        stats_layout = QHBoxLayout(stats_container)
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(16)
        
        self.cpu_stats = StatsPanel("CPU", "#00d4ff")
        stats_layout.addWidget(self.cpu_stats)
        
        self.mem_stats = StatsPanel("Memory", "#ffd93d")
        stats_layout.addWidget(self.mem_stats)
        
        self.disk_stats = StatsPanel("Disk I/O", "#51cf66")
        stats_layout.addWidget(self.disk_stats)
        
        self.net_stats = StatsPanel("Network I/O", "#7c3aed")
        stats_layout.addWidget(self.net_stats)
        
        layout.addWidget(stats_container)
    
    def update_graphs(self):
        """Update graphs with new data points from real system data"""
        # Get real CPU and memory usage
        cpu_value = psutil.cpu_percent(interval=0.1)
        mem_value = psutil.virtual_memory().percent
        
        # Add data points
        self.cpu_graph.add_data_point(cpu_value)
        self.memory_graph.add_data_point(mem_value)
        
        # Get disk I/O
        current_disk_io = psutil.disk_io_counters()
        if self.prev_disk_io:
            disk_read_kb = (current_disk_io.read_bytes - self.prev_disk_io.read_bytes) / 1024
            disk_write_kb = (current_disk_io.write_bytes - self.prev_disk_io.write_bytes) / 1024
            disk_total_kb = disk_read_kb + disk_write_kb
        else:
            disk_total_kb = 0
        self.prev_disk_io = current_disk_io
        self.disk_graph.add_data_point(disk_total_kb)
        
        # Get network I/O
        current_net_io = psutil.net_io_counters()
        if self.prev_net_io:
            net_sent_kb = (current_net_io.bytes_sent - self.prev_net_io.bytes_sent) / 1024
            net_recv_kb = (current_net_io.bytes_recv - self.prev_net_io.bytes_recv) / 1024
            net_total_kb = net_sent_kb + net_recv_kb
        else:
            net_total_kb = 0
        self.prev_net_io = current_net_io
        self.network_graph.add_data_point(net_total_kb)
        
        # Update statistics
        cpu_data = list(self.cpu_graph.data_points)
        mem_data = list(self.memory_graph.data_points)
        disk_data = list(self.disk_graph.data_points)
        net_data = list(self.network_graph.data_points)
        
        if cpu_data:
            cpu_avg = sum(cpu_data) / len(cpu_data)
            cpu_max = max(cpu_data)
            cpu_min = min(cpu_data)
            self.cpu_stats.update_stats(cpu_avg, cpu_max, cpu_min)
        
        if mem_data:
            mem_avg = sum(mem_data) / len(mem_data)
            mem_max = max(mem_data)
            mem_min = min(mem_data)
            self.mem_stats.update_stats(mem_avg, mem_max, mem_min)
            
        if disk_data:
            disk_avg = sum(disk_data) / len(disk_data)
            disk_max = max(disk_data)
            disk_min = min(disk_data)
            self.disk_stats.update_stats(disk_avg, disk_max, disk_min)
            
        if net_data:
            net_avg = sum(net_data) / len(net_data)
            net_max = max(net_data)
            net_min = min(net_data)
            self.net_stats.update_stats(net_avg, net_max, net_min)
        
        self.time_counter += 1
