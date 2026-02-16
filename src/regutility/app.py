import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from regutility.core.registry import is_windows_system
from regutility.ui.main_window import ScriptForgeApp
from regutility.styles import MODERN_DARK_STYLESHEET


def main() -> None:
    # Set AppUserModelID for proper taskbar icon handling
    try:
        from ctypes import windll
        myappid = 'yuukifst.scriptforge.regutility.1.0'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass

    app = QApplication(sys.argv)
    app.setStyleSheet(MODERN_DARK_STYLESHEET)

    if not is_windows_system():
        QMessageBox.critical(
            None,
            'Compatibility Error',
            'This program requires the Windows Registry and can only be run on a Windows OS.',
        )
        sys.exit(1)

    window = ScriptForgeApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()