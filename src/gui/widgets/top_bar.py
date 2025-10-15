"""
Top bar widget with branding, search, and controls
"""

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QPixmap, QPainter, QColor, QLinearGradient


class TopBar(QFrame):
    """Top bar containing logo, search, and control buttons"""
    
    search_changed = pyqtSignal(str)
    refresh_clicked = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setObjectName("topBar")
        self.setFixedHeight(60)
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI components"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(24, 0, 24, 0)
        layout.setSpacing(24)
        
        # Left - Branding
        branding_layout = QHBoxLayout()
        branding_layout.setSpacing(12)
        
        # Logo/Icon
        logo_label = QLabel()
        logo_pixmap = self.create_gradient_icon(32, 32)
        logo_label.setPixmap(logo_pixmap)
        branding_layout.addWidget(logo_label)
        
        # Title and version
        title_layout = QHBoxLayout()
        title_layout.setSpacing(8)
        
        title_label = QLabel("ELPM")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #e0e0e0;")
        title_layout.addWidget(title_label)
        
        version_label = QLabel("v1.0")
        version_label.setStyleSheet("font-size: 11px; color: #666666;")
        version_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        title_layout.addWidget(version_label)
        
        branding_layout.addLayout(title_layout)
        layout.addLayout(branding_layout)
        
        # Center - Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Filter processes by name, PID, or command...")
        self.search_input.setMaximumWidth(400)
        self.search_input.textChanged.connect(self.search_changed.emit)
        layout.addWidget(self.search_input)
        
        # Spacer
        layout.addStretch()
        
        # Right - Controls
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(8)
        
        # Refresh button
        self.refresh_btn = QPushButton("🔄")
        self.refresh_btn.setObjectName("iconButton")
        self.refresh_btn.setToolTip("Refresh")
        self.refresh_btn.clicked.connect(self.refresh_clicked.emit)
        controls_layout.addWidget(self.refresh_btn)
        
        # Settings button
        self.settings_btn = QPushButton("⚙")
        self.settings_btn.setObjectName("iconButton")
        self.settings_btn.setToolTip("Settings")
        controls_layout.addWidget(self.settings_btn)
        
        # Minimize button
        self.minimize_btn = QPushButton("−")
        self.minimize_btn.setObjectName("iconButton")
        self.minimize_btn.setToolTip("Minimize")
        controls_layout.addWidget(self.minimize_btn)
        
        # Close button
        self.close_btn = QPushButton("✕")
        self.close_btn.setObjectName("closeButton")
        self.close_btn.setToolTip("Close")
        controls_layout.addWidget(self.close_btn)
        
        layout.addLayout(controls_layout)
    
    def create_gradient_icon(self, width, height):
        """Create a gradient icon for the logo"""
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Create gradient
        gradient = QLinearGradient(0, 0, width, height)
        gradient.setColorAt(0, QColor("#00d4ff"))
        gradient.setColorAt(1, QColor("#7c3aed"))
        
        # Draw rounded rectangle
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, width, height, 6, 6)
        
        # Draw activity symbol (simple bars)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor("#ffffff"))
        bar_width = 3
        bar_spacing = 4
        start_x = 8
        
        # Draw simple activity bars
        for i, height_pct in enumerate([0.4, 0.7, 0.5, 0.8]):
            x = start_x + i * (bar_width + bar_spacing)
            bar_height = int(height * height_pct)
            y = (height - bar_height) // 2
            painter.drawRect(x, y, bar_width, bar_height)
        
        painter.end()
        return pixmap
