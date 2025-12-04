import os

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PyQt6.QtGui import QIcon

from regutility.ui.compare_tab import CompareTab
from regutility.ui.backup_tab import BackupTab
from regutility.ui.convert_tab import ConvertTab
from regutility.ui.ps1_convert_tab import Ps1ConvertTab
from regutility.utils.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_MARGIN,
    LAYOUT_SPACING,
    APP_TITLE,
    APP_CREDITS,
)


def get_icon_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "..", "assets", "icon.png")


class ScriptForgeApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_ui()

    def _setup_window(self) -> None:
        self.setWindowTitle(APP_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        icon_path = get_icon_path()
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(LAYOUT_SPACING)
        main_layout.setContentsMargins(WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN)

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        self.compare_tab = CompareTab()
        self.tabs.addTab(self.compare_tab, "Compare Registry")

        self.backup_tab = BackupTab()
        self.tabs.addTab(self.backup_tab, "Generate Backup")

        self.convert_tab = ConvertTab()
        self.tabs.addTab(self.convert_tab, ".reg to .bat")

        self.ps1_convert_tab = Ps1ConvertTab()
        self.tabs.addTab(self.ps1_convert_tab, ".ps1 to .bat")

        self.statusBar().showMessage(APP_CREDITS)
