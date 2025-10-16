"""
Application-wide stylesheet definitions
"""

STYLESHEET = """
/* Main Window */
QMainWindow {
    background-color: #1a1a1a;
    color: #e0e0e0;
}

/* Tab Widget */
QTabWidget::pane {
    border: none;
    background-color: #1a1a1a;
}

QTabWidget#mainTabs > QTabBar::tab {
    background-color: #2d2d2d;
    color: #a0a0a0;
    border: none;
    border-bottom: 2px solid transparent;
    padding: 12px 20px;
    margin-right: 4px;
    font-size: 13px;
}

QTabWidget#mainTabs > QTabBar::tab:selected {
    color: #00d4ff;
    border-bottom: 2px solid #00d4ff;
}

QTabWidget#mainTabs > QTabBar::tab:hover {
    color: #e0e0e0;
    background-color: rgba(58, 58, 58, 0.3);
}

/* Buttons */
QPushButton {
    background-color: #2d2d2d;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    padding: 8px 16px;
    border-radius: 4px;
    font-size: 12px;
}

QPushButton:hover {
    background-color: #3a3a3a;
    border-color: #00d4ff;
}

QPushButton:pressed {
    background-color: #1a1a1a;
}

QPushButton#iconButton {
    padding: 8px;
    min-width: 36px;
    max-width: 36px;
}

QPushButton#iconButton:hover {
    background-color: #3a3a3a;
    color: #00d4ff;
}

QPushButton#closeButton:hover {
    color: #ff6b6b;
}

/* Action Buttons */
QPushButton#sigterm {
    background-color: #51cf66;
    color: #1a1a1a;
    border: none;
    padding: 10px;
    font-weight: bold;
}

QPushButton#sigterm:hover {
    background-color: rgba(81, 207, 102, 0.9);
}

QPushButton#sigkill {
    background-color: #ff6b6b;
    color: #1a1a1a;
    border: none;
    padding: 10px;
    font-weight: bold;
}

QPushButton#sigkill:hover {
    background-color: rgba(255, 107, 107, 0.9);
}

QPushButton#sigstop {
    background-color: #ffd93d;
    color: #1a1a1a;
    border: none;
    padding: 10px;
    font-weight: bold;
}

QPushButton#sigstop:hover {
    background-color: rgba(255, 217, 61, 0.9);
}

QPushButton#sigcont {
    background-color: #4ecdc4;
    color: #1a1a1a;
    border: none;
    padding: 10px;
    font-weight: bold;
}

QPushButton#sigcont:hover {
    background-color: rgba(78, 205, 196, 0.9);
}

/* Line Edit / Search */
QLineEdit {
    background-color: #1a1a1a;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 12px;
}

QLineEdit:focus {
    border-color: #00d4ff;
}

/* ComboBox */
QComboBox {
    background-color: #1a1a1a;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 11px;
    min-width: 100px;
}

QComboBox:hover {
    border-color: #00d4ff;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
}

QComboBox QAbstractItemView {
    background-color: #2d2d2d;
    color: #e0e0e0;
    selection-background-color: #00d4ff;
    selection-color: #1a1a1a;
    border: 1px solid #3a3a3a;
}

/* CheckBox */
QCheckBox {
    color: #a0a0a0;
    spacing: 8px;
    font-size: 11px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 1px solid #3a3a3a;
    border-radius: 3px;
    background-color: #1a1a1a;
}

QCheckBox::indicator:checked {
    background-color: #51cf66;
    border-color: #51cf66;
}

QCheckBox::indicator:hover {
    border-color: #00d4ff;
}

/* Table Widget */
QTableWidget {
    background-color: #1a1a1a;
    alternate-background-color: #1e1e1e;
    gridline-color: #3a3a3a;
    border: none;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 11px;
}

QTableWidget::item {
    padding: 4px 8px;
    border: none;
}

QTableWidget::item:selected {
    background-color: rgba(0, 212, 255, 0.2);
    color: #e0e0e0;
}

QTableWidget::item:hover {
    background-color: #3a3a3a;
}

QHeaderView::section {
    background-color: #2d2d2d;
    color: #e0e0e0;
    padding: 8px;
    border: none;
    border-bottom: 1px solid #3a3a3a;
    font-size: 11px;
    font-weight: bold;
}

/* Scrollbar */
QScrollBar:vertical {
    background-color: #1a1a1a;
    width: 12px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background-color: #3a3a3a;
    min-height: 20px;
    border-radius: 6px;
    margin: 2px;
}

QScrollBar::handle:vertical:hover {
    background-color: #4a4a4a;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background-color: #1a1a1a;
    height: 12px;
    margin: 0;
}

QScrollBar::handle:horizontal {
    background-color: #3a3a3a;
    min-width: 20px;
    border-radius: 6px;
    margin: 2px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #4a4a4a;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}

/* Labels */
QLabel {
    color: #e0e0e0;
    background: transparent;
}

/* Frames */
QFrame#topBar {
    background-color: #2d2d2d;
    border-bottom: 1px solid #3a3a3a;
}

QFrame#statusBar {
    background-color: #2d2d2d;
    border-top: 1px solid #3a3a3a;
}

QFrame#detailsPanel {
    background-color: #2d2d2d;
    border-left: 1px solid #3a3a3a;
}

QFrame#separator {
    background-color: #3a3a3a;
}

/* Text Edit / Read Only */
QTextEdit {
    background-color: #1a1a1a;
    color: #e0e0e0;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 8px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 10px;
}

/* Progress Bar */
QProgressBar {
    background-color: #1a1a1a;
    border: none;
    border-radius: 3px;
    height: 6px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #51cf66;
    border-radius: 3px;
}

/* Scroll Area */
QScrollArea {
    border: none;
    background-color: transparent;
}
"""
