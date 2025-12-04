from PyQt6.QtWidgets import QLabel, QTextEdit
from PyQt6.QtCore import Qt


def create_title_label(text: str) -> QLabel:
    label = QLabel(text)
    label.setObjectName("title")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return label


def create_instructions_label(text: str) -> QLabel:
    label = QLabel(text)
    label.setObjectName("instructions")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return label


def create_file_selection_label() -> QLabel:
    label = QLabel("No file selected.")
    label.setObjectName("selected_file")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return label


def create_log_label(text: str) -> QLabel:
    label = QLabel(text)
    label.setObjectName("log_label")
    return label


def create_readonly_text_edit(object_name: str) -> QTextEdit:
    text_edit = QTextEdit()
    text_edit.setObjectName(object_name)
    text_edit.setReadOnly(True)
    return text_edit
