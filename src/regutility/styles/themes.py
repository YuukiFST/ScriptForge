MODERN_DARK_STYLESHEET = """
* {
    margin: 0;
    padding: 0;
    font-family: "Iosevka", "Segoe UI", "Arial", sans-serif;
}

QMainWindow {
    background-color: #000000;
}

QWidget {
    background-color: #000000;
    color: #E0E0E0;
    font-family: "Iosevka", "Segoe UI", "Arial", sans-serif;
    font-size: 10pt;
}

QPushButton {
    background-color: #1A1A1A;
    color: #E0E0E0;
    border: 1px solid #333333;
    border-radius: 4px;
    padding: 8px 20px;
    font-family: "Iosevka", "Segoe UI", "Arial", sans-serif;
    font-size: 10pt;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #252525;
    border: 1px solid #404040;
}

QPushButton:pressed {
    background-color: #151515;
}

QPushButton:disabled {
    background-color: #141414;
    color: #505050;
    border: 1px solid #252525;
}

QTextEdit {
    background-color: #0A0A0A;
    border: 1px solid #252525;
    border-radius: 4px;
    padding: 10px;
    color: #C0C0C0;
    font-family: "Iosevka", "Consolas", "Monaco", monospace;
    font-size: 9pt;
    selection-background-color: #404040;
}

QTextEdit[objectName="reg_file_output"] {
    background-color: #0A0A0A;
    border-left: 3px solid #4A7C9B;
}

QTextEdit[objectName="system_output"] {
    background-color: #0A0A0A;
    border-left: 3px solid #7C4A4A;
}

QTextEdit[objectName="log_output"] {
    background-color: #0A0A0A;
    border-left: 3px solid #333333;
}

QLabel {
    background-color: transparent;
    color: #B0B0B0;
    font-family: "Iosevka", "Segoe UI", "Arial", sans-serif;
    font-size: 10pt;
    border: none;
    padding: 0;
}

QLabel[objectName="title"] {
    font-size: 16pt;
    font-weight: 600;
    color: #FFFFFF;
    padding: 8px 0;
    letter-spacing: 0.5px;
}

QLabel[objectName="instructions"] {
    font-size: 9pt;
    color: #707070;
    padding: 4px 0 12px 0;
}

QLabel[objectName="selected_file"] {
    font-size: 9pt;
    color: #606060;
    padding: 2px 0;
}

QLabel[objectName="log_label"] {
    font-size: 9pt;
    font-weight: 600;
    color: #909090;
    padding: 8px 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 1px;
}

QStatusBar {
    background-color: #0A0A0A;
    color: #505050;
    font-size: 8pt;
    border-top: 1px solid #1A1A1A;
    padding: 4px;
}

QTabWidget::pane {
    border: 1px solid #1A1A1A;
    border-radius: 0;
    background-color: #000000;
    top: -1px;
}

QTabBar::tab {
    background-color: #0A0A0A;
    color: #707070;
    padding: 10px 24px;
    border: 1px solid #1A1A1A;
    border-bottom: none;
    margin-right: 2px;
    font-size: 9pt;
    font-weight: 500;
}

QTabBar::tab:selected {
    background-color: #000000;
    color: #E0E0E0;
    border-bottom: 2px solid #000000;
}

QTabBar::tab:hover:!selected {
    background-color: #121212;
    color: #A0A0A0;
}

QGroupBox {
    background-color: transparent;
    border: 1px solid #1A1A1A;
    border-radius: 4px;
    margin-top: 12px;
    padding: 12px;
    font-size: 9pt;
    font-weight: 600;
    color: #808080;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 8px;
    color: #808080;
    background-color: #000000;
}

QCheckBox {
    spacing: 8px;
    color: #A0A0A0;
    font-size: 9pt;
}

QCheckBox::indicator {
    width: 14px;
    height: 14px;
    border-radius: 2px;
    border: 1px solid #404040;
    background-color: #0A0A0A;
}

QCheckBox::indicator:checked {
    background-color: #505050;
    border: 1px solid #606060;
}

QCheckBox::indicator:hover {
    border: 1px solid #505050;
}

QScrollBar:vertical {
    background-color: #0A0A0A;
    width: 8px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #303030;
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background-color: #404040;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar:horizontal {
    background-color: #0A0A0A;
    height: 8px;
    border: none;
}

QScrollBar::handle:horizontal {
    background-color: #303030;
    border-radius: 4px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #404040;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}
"""