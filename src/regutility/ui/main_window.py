from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTabWidget

from regutility.ui.compare_tab import CompareTab
from regutility.ui.backup_tab import BackupTab
from regutility.utils.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_MARGIN,
    LAYOUT_SPACING,
    APP_TITLE,
    APP_CREDITS,
)


class RegistryUtilityApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self._setup_window()
        self._setup_ui()

    def _setup_window(self) -> None:
        self.setWindowTitle(APP_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(LAYOUT_SPACING)
        main_layout.setContentsMargins(WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(
            "QTabWidget::pane { border: 0; } "
            "QTabBar::tab { font-size: 12pt; font-weight: bold; padding: 10px; }"
        )
        main_layout.addWidget(self.tabs)

        self.compare_tab = CompareTab()
        self.tabs.addTab(self.compare_tab, "Compare Registry")

        self.backup_tab = BackupTab()
        self.tabs.addTab(self.backup_tab, "Generate Backup")

        self.statusBar().showMessage(APP_CREDITS)
