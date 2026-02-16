import os
from typing import Dict, Optional
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QApplication,
    QFileDialog,
    QMessageBox,
)
from regutility.ui.widgets import (
    create_title_label,
    create_instructions_label,
    create_file_selection_label,
    create_log_label,
    create_readonly_text_edit,
)
from regutility.core import (
    parse_reg_file,
    get_current_registry_values_for_backup,
    generate_backup_reg,
)
from regutility.utils.constants import (
    WINDOW_MARGIN,
    LAYOUT_SPACING,
    STATUS_MATCH,
    STATUS_ERROR,
)


class BackupTab(QWidget):

    def __init__(self):
        super().__init__()
        self.input_file_path: Optional[str] = None
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(LAYOUT_SPACING)
        layout.setContentsMargins(
            WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN
        )
        layout.addWidget(create_title_label('Registry (.reg) File Backup Generator'))
        layout.addWidget(create_instructions_label(
            "1. Select the .reg file you intend to apply.\n"
            "2. Click 'Generate Backup' to create a rollback file."
        ))
        self.btn_select_file = QPushButton('1. Select .reg File')
        self.btn_select_file.clicked.connect(self._select_file)
        layout.addWidget(self.btn_select_file)
        self.selected_file_label = create_file_selection_label()
        layout.addWidget(self.selected_file_label)
        self.btn_generate_backup = QPushButton('2. Generate Backup')
        self.btn_generate_backup.setEnabled(False)
        self.btn_generate_backup.clicked.connect(self._generate_backup)
        layout.addWidget(self.btn_generate_backup)
        layout.addWidget(create_log_label('Operation Log:'))
        self.log_output = create_readonly_text_edit('log_output')
        layout.addWidget(self.log_output)
        self._log('Ready to start. Please select a .reg file.')

    def _log(self, message: str) -> None:
        self.log_output.append(message)
        QApplication.processEvents()

    def _select_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Select the .reg file to back up', '', 'Registry Files (*.reg);;All Files (*.*)'
        )
        if file_path:
            self.input_file_path = file_path
            self.selected_file_label.setText(f'Selected: {os.path.basename(file_path)}')
            self.btn_generate_backup.setEnabled(True)
            self._log(f'Input file selected: {file_path}')
        else:
            self.selected_file_label.setText('File selection cancelled.')
            self.btn_generate_backup.setEnabled(False)

    def _generate_backup(self) -> None:
        if not self.input_file_path:
            self._log('Error: No input file has been selected.')
            return
        self._log('\nStarting backup process...')
        self._set_ui_busy(True)
        try:
            parsed_settings = self._parse_input_file()
            current_values = self._get_current_values_for_backup(parsed_settings)
            output_path = self._get_backup_output_path()
            if output_path:
                self._create_backup_file(parsed_settings, current_values, output_path)
                self._show_backup_success(output_path)
        except Exception as e:
            self._handle_error(str(e))
        finally:
            self._set_ui_busy(False)

    def _parse_input_file(self) -> Dict[str, Dict[str, str]]:
        self._log('Step 1: Parsing .reg file...')
        parsed_settings = parse_reg_file(self.input_file_path)
        self._log(f'Parsing complete. Found {len(parsed_settings)} key sections.')
        return parsed_settings

    def _get_current_values_for_backup(
        self,
        parsed_settings: Dict[str, Dict[str, str]],
    ) -> Dict[str, str]:
        self._log('Step 2: Reading current values from the Windows Registry...')
        current_values = get_current_registry_values_for_backup(parsed_settings, self._log)
        self._log('Reading current values complete.')
        return current_values

    def _get_backup_output_path(self) -> Optional[str]:
        default_name = f'{os.path.splitext(os.path.basename(self.input_file_path))[0]}_backup.reg'
        output_path, _ = QFileDialog.getSaveFileName(
            self, 'Save backup .reg file as', default_name, 'Registry Files (*.reg);;All Files (*.*)'
        )
        if not output_path:
            self._log('Operation cancelled: No save location was selected.')
        return output_path

    def _create_backup_file(
        self,
        parsed_settings: Dict[str, Dict[str, str]],
        current_values: Dict[str, str],
        output_path: str,
    ) -> None:
        self._log('Step 3: Generating the backup file...')
        generate_backup_reg(parsed_settings, current_values, output_path)

    def _show_backup_success(self, output_path: str) -> None:
        success_msg = f'Backup file successfully generated at: {output_path}'
        self._log('\n----')
        self._log(f'{STATUS_MATCH} SUCCESS!')
        self._log(success_msg)
        self._log('----')
        QMessageBox.information(self, 'Success', success_msg)

    def _set_ui_busy(self, busy: bool) -> None:
        self.btn_select_file.setEnabled(not busy)
        self.btn_generate_backup.setEnabled(not busy and self.input_file_path is not None)

    def _handle_error(self, error_message: str) -> None:
        formatted_error = f'{STATUS_ERROR} ERROR: {error_message}'
        self._log('\n----')
        self._log(formatted_error)
        self._log('----')
        QMessageBox.critical(self, 'Operation Error', error_message)