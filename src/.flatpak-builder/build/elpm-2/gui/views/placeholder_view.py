"""
Placeholder view for unimplemented tabs
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt


class PlaceholderView(QWidget):
    """Placeholder view for tabs under development"""
    
    def __init__(self, icon, title, subtitle):
        super().__init__()
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Icon
        icon_label = QLabel(self.icon)
        icon_label.setStyleSheet("font-size: 48px; color: #a0a0a0; opacity: 0.5;")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)
        
        # Title
        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-size: 14px; color: #a0a0a0; margin-top: 12px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Subtitle
        subtitle_label = QLabel(self.subtitle)
        subtitle_label.setStyleSheet("font-size: 11px; color: #a0a0a0; margin-top: 4px;")
        subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(subtitle_label)
