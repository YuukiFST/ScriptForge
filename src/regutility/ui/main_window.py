import os
import sys
import ctypes
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

DWMWA_USE_IMMERSIVE_DARK_MODE = 20
DWMWA_CAPTION_COLOR = 35
TITLE_BAR_COLOR = 0x000000


def get_icon_path() -> str:
    """
    Get the absolute path to the icon file, handling both development
    and PyInstaller frozen states.
    """
    if getattr(sys, 'frozen', False):
        base_path = os.path.join(sys._MEIPASS, 'regutility')
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return os.path.join(base_path, 'assets', 'anvil.ico')


class ScriptForgeApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self._setup_window()
        self._apply_dark_title_bar()
        self._setup_ui()

    def _setup_window(self) -> None:
        self.setWindowTitle(APP_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        icon_path = get_icon_path()
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

    def _apply_dark_title_bar(self) -> None:
        """
        Applies a dark title bar to the window using the Windows DWM API.
        This forces the title bar to be black (or dark) to match the dark theme.
        """
        try:
            set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
            hwnd = int(self.winId())

            dark_mode = ctypes.c_int(2)
            set_window_attribute(
                hwnd,
                DWMWA_USE_IMMERSIVE_DARK_MODE,
                ctypes.byref(dark_mode),
                ctypes.sizeof(dark_mode),
            )

            caption_color = ctypes.c_int(TITLE_BAR_COLOR)
            set_window_attribute(
                hwnd,
                DWMWA_CAPTION_COLOR,
                ctypes.byref(caption_color),
                ctypes.sizeof(caption_color),
            )
        except Exception:
            pass

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(LAYOUT_SPACING)
        main_layout.setContentsMargins(
            WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN
        )

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        self.compare_tab = CompareTab()
        self.tabs.addTab(self.compare_tab, 'Compare Registry')

        self.backup_tab = BackupTab()
        self.tabs.addTab(self.backup_tab, 'Generate Backup')

        self.convert_tab = ConvertTab()
        self.tabs.addTab(self.convert_tab, '.reg to .bat')

        self.ps1_convert_tab = Ps1ConvertTab()
        self.tabs.addTab(self.ps1_convert_tab, '.ps1 to .bat')

        self.statusBar().showMessage(APP_CREDITS)
