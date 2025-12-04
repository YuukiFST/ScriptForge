import os
from typing import Optional

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox,
    QApplication, QFileDialog, QMessageBox, QGroupBox
)

from regutility.ui.widgets import (
    create_title_label,
    create_instructions_label,
    create_file_selection_label,
    create_log_label,
    create_readonly_text_edit,
)
from regutility.core.ps1_converter import Ps1ConversionOptions, convert_ps1_file_to_bat
from regutility.utils.constants import (
    WINDOW_MARGIN,
    LAYOUT_SPACING,
    STATUS_MATCH,
    STATUS_ERROR,
)


class Ps1ConvertTab(QWidget):

    def __init__(self):
        super().__init__()
        self.input_file_path: Optional[str] = None
        self.generated_bat: str = ""
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(LAYOUT_SPACING)
        layout.setContentsMargins(WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN)

        layout.addWidget(create_title_label("Convert .ps1 to .bat"))
        layout.addWidget(create_instructions_label(
            "Convert PowerShell scripts to standalone batch files.\n"
            "The .bat embeds your PowerShell code using Base64 encoding."
        ))

        file_layout = QHBoxLayout()
        self.btn_select_file = QPushButton("1. Select .ps1 File")
        self.btn_select_file.clicked.connect(self._select_file)
        file_layout.addWidget(self.btn_select_file)

        self.selected_file_label = create_file_selection_label()
        file_layout.addWidget(self.selected_file_label)
        layout.addLayout(file_layout)

        options_group = QGroupBox("Options")
        options_layout = QVBoxLayout(options_group)

        self.chk_base64 = QCheckBox("Use Base64 encoding (recommended for complex scripts)")
        self.chk_base64.setChecked(True)
        self.chk_base64.stateChanged.connect(self._update_preview)
        options_layout.addWidget(self.chk_base64)

        self.chk_bypass_policy = QCheckBox("Bypass execution policy")
        self.chk_bypass_policy.setChecked(True)
        self.chk_bypass_policy.stateChanged.connect(self._update_preview)
        options_layout.addWidget(self.chk_bypass_policy)

        self.chk_hidden = QCheckBox("Hide PowerShell window")
        self.chk_hidden.setChecked(False)
        self.chk_hidden.stateChanged.connect(self._update_preview)
        options_layout.addWidget(self.chk_hidden)

        self.chk_admin = QCheckBox("Run as Administrator (auto-elevate)")
        self.chk_admin.setChecked(False)
        self.chk_admin.stateChanged.connect(self._update_preview)
        options_layout.addWidget(self.chk_admin)

        layout.addWidget(options_group)

        self.btn_convert = QPushButton("2. Generate Preview")
        self.btn_convert.setEnabled(False)
        self.btn_convert.clicked.connect(self._generate_preview)
        layout.addWidget(self.btn_convert)

        layout.addWidget(create_log_label("Preview:"))
        self.preview_output = create_readonly_text_edit("log_output")
        layout.addWidget(self.preview_output)

        self.btn_save = QPushButton("3. Save as .bat File")
        self.btn_save.setEnabled(False)
        self.btn_save.clicked.connect(self._save_bat_file)
        layout.addWidget(self.btn_save)

    def _get_options(self) -> Ps1ConversionOptions:
        return Ps1ConversionOptions(
            use_base64_encoding=self.chk_base64.isChecked(),
            hide_window=self.chk_hidden.isChecked(),
            run_as_admin=self.chk_admin.isChecked(),
            bypass_execution_policy=self.chk_bypass_policy.isChecked()
        )

    def _select_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select the .ps1 file to convert", "", "PowerShell Files (*.ps1);;All Files (*.*)"
        )
        if file_path:
            self.input_file_path = file_path
            self.selected_file_label.setText(f"Selected: {os.path.basename(file_path)}")
            self.btn_convert.setEnabled(True)
            self.btn_save.setEnabled(False)
            self.preview_output.clear()
            self.generated_bat = ""
        else:
            self.selected_file_label.setText("File selection cancelled.")
            self.btn_convert.setEnabled(False)

    def _generate_preview(self) -> None:
        if not self.input_file_path:
            return

        try:
            options = self._get_options()
            self.generated_bat = convert_ps1_file_to_bat(self.input_file_path, options)
            self.preview_output.setText(self.generated_bat)
            self.btn_save.setEnabled(True)
        except Exception as e:
            self.preview_output.setText(f"{STATUS_ERROR} ERROR: {e}")
            self.btn_save.setEnabled(False)
            QMessageBox.critical(self, "Conversion Error", str(e))

    def _update_preview(self) -> None:
        if self.generated_bat and self.input_file_path:
            self._generate_preview()

    def _save_bat_file(self) -> None:
        if not self.generated_bat:
            return

        default_name = f"{os.path.splitext(os.path.basename(self.input_file_path))[0]}.bat"
        output_path, _ = QFileDialog.getSaveFileName(
            self, "Save .bat file as", default_name, "Batch Files (*.bat);;All Files (*.*)"
        )

        if not output_path:
            return

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(self.generated_bat)
            
            QMessageBox.information(
                self, 
                "Success", 
                f"{STATUS_MATCH} Batch file saved successfully!\n\n{output_path}"
            )
        except Exception as e:
            QMessageBox.critical(self, "Save Error", str(e))
