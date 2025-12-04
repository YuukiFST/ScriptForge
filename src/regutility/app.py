import sys

from PyQt6.QtWidgets import QApplication, QMessageBox

from regutility.core.registry import is_windows_system
from regutility.ui.main_window import ScriptForgeApp
from regutility.styles import MODERN_DARK_STYLESHEET


def validate_windows_system() -> None:
    if not is_windows_system():
        app = QApplication(sys.argv)
        app.setStyleSheet(MODERN_DARK_STYLESHEET)
        QMessageBox.critical(
            None,
            "Compatibility Error",
            "This program requires the Windows Registry and can only be run on a Windows OS."
        )
        sys.exit(1)


def main() -> None:
    validate_windows_system()

    app = QApplication(sys.argv)
    app.setStyleSheet(MODERN_DARK_STYLESHEET)

    window = ScriptForgeApp()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
