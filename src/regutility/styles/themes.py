MODERN_DARK_STYLESHEET = """
QMainWindow {
    background-color: #0A0A0A;
    border: 1px solid #2A2A2A;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
}

QWidget {
    background-color: #0A0A0A;
    color: #F5F5F5;
    font-family: "Roboto", "Segoe UI", "Arial", sans-serif;
    font-size: 11pt;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 #6A9DE8, stop:1 #5A7BC8);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 12px 24px;
    font-family: "Roboto", "Segoe UI", "Arial", sans-serif;
    font-weight: bold;
    font-size: 12pt;
    min-height: 20px;
}

QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 #7AADF8, stop:1 #6A8BD8);
    transform: translateY(-2px);
}

QPushButton:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
    stop:0 #5A8DD8, stop:1 #4A6BB8);
}

QPushButton:disabled {
    background: #404040;
    color: #808080;
}

QTextEdit {
    background-color: rgba(16, 16, 16, 220);
    border: 2px solid #2A2A2A;
    border-radius: 12px;
    padding: 15px;
    color: #F5F5F5;
    font-family: "Consolas", "Courier New", "Monaco", monospace;
    font-size: 10pt;
    selection-background-color: #6A9DE8;
}

QTextEdit[objectName="reg_file_output"] {
    background-color: rgba(16, 16, 32, 220);
    border: 2px solid #4A4A8A;
}

QTextEdit[objectName="system_output"] {
    background-color: rgba(32, 16, 16, 220);
    border: 2px solid #8A4A4A;
}

QTextEdit[objectName="log_output"] {
    background-color: rgba(16, 16, 16, 220);
    border: 2px solid #2A2A2A;
}

QLabel {
    background-color: transparent;
    color: #F5F5F5;
    font-family: "Roboto", "Segoe UI", "Arial", sans-serif;
    font-size: 11pt;
    border: none;
}

QLabel[objectName="title"] {
    font-size: 20pt;
    font-weight: bold;
    color: #6A9DE8;
    padding: 20px 0;
}

QLabel[objectName="instructions"] {
    font-size: 12pt;
    color: #CCCC;
    padding: 10px 0;
}

QLabel[objectName="selected_file"] {
    font-size: 10pt;
    color: #AAAA;
    font-style: italic;
    padding: 5px 0;
}

QLabel[objectName="log_label"] {
    font-size: 12pt;
    font-weight: bold;
    color: #F5F5F5;
    padding: 10px 0;
}

QStatusBar {
    background-color: #121212;
    color: #AAAA;
    font-family: "Roboto", "Segoe UI", "Arial", sans-serif;
    font-size: 9pt;
    border-top: 1px solid #2A2A2A;
    border-radius: 0 0 15px 15px;
}

QTabWidget::pane {
    border: 1px solid #2A2A2A;
    border-radius: 10px;
    background-color: #0A0A0A;
}

QTabBar::tab {
    background: #1A1A1A;
    color: #F5F5F5;
    padding: 10px 20px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    border: 1px solid #2A2A2A;
    border-bottom: none;
    margin-right: 2px;
}

QTabBar::tab:selected {
    background: #0A0A0A;
    border-bottom: 1px solid #0A0A0A;
}

QTabBar::tab:hover {
    background: #2A2A2A;
}
"""
