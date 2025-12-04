import os
from typing import Dict, List, Optional, Callable

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QApplication, QFileDialog, QMessageBox
)

from regutility.ui.widgets import (
    create_title_label,
    create_instructions_label,
    create_file_selection_label,
    create_log_label,
    create_readonly_text_edit,
)
from regutility.models import ComparisonResult, ComparisonStatus
from regutility.core import parse_reg_file, get_current_registry_value, compare_values
from regutility.utils.constants import (
    WINDOW_MARGIN,
    LAYOUT_SPACING,
    STATUS_MATCH,
    STATUS_NOT_FOUND,
    STATUS_ERROR,
)


class CompareTab(QWidget):

    def __init__(self):
        super().__init__()
        self.input_file_path: Optional[str] = None
        self.comparison_results: List[ComparisonResult] = []
        self.filter_buttons: List[QPushButton] = []
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setSpacing(LAYOUT_SPACING)
        layout.setContentsMargins(WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN, WINDOW_MARGIN)

        layout.addWidget(create_title_label("Registry File vs. System Comparison"))
        layout.addWidget(create_instructions_label(
            "1. Select a .reg file.\n2. Click 'Compare' to see values from the file and your system."
        ))

        file_selection_layout = self._create_file_selection_layout()
        layout.addLayout(file_selection_layout)

        self.btn_compare = QPushButton("2. Compare Registry Values")
        self.btn_compare.setEnabled(False)
        self.btn_compare.clicked.connect(self._compare_registry)
        layout.addWidget(self.btn_compare)

        filter_layout = self._create_filter_buttons_layout()
        layout.addLayout(filter_layout)

        comparison_layout = self._create_comparison_output_layout()
        layout.addLayout(comparison_layout)

        layout.addWidget(create_log_label("Operation Log:"))
        self.log_output = create_readonly_text_edit("log_output")
        layout.addWidget(self.log_output)

        self._log("Ready to start. Please select a .reg file.")

    def _create_file_selection_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()

        self.btn_select_file = QPushButton("1. Select .reg File")
        self.btn_select_file.clicked.connect(self._select_file)
        layout.addWidget(self.btn_select_file)

        self.selected_file_label = create_file_selection_label()
        layout.addWidget(self.selected_file_label)

        return layout

    def _create_filter_buttons_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()

        filter_buttons = [
            ("Show All", "all"),
            ("Show Matches Only", "matches"),
            ("Show Differences Only", "differences"),
            ("Show Missing Only", "missing")
        ]

        for text, filter_type in filter_buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, ft=filter_type: self._filter_results(ft))
            button.setEnabled(False)
            layout.addWidget(button)
            self.filter_buttons.append(button)

        return layout

    def _create_comparison_output_layout(self) -> QHBoxLayout:
        layout = QHBoxLayout()

        reg_file_group = QVBoxLayout()
        reg_file_group.addWidget(create_log_label("Values from .reg File:"))
        self.reg_file_output = create_readonly_text_edit("reg_file_output")
        reg_file_group.addWidget(self.reg_file_output)
        layout.addLayout(reg_file_group)

        system_group = QVBoxLayout()
        system_group.addWidget(create_log_label("Current System Values:"))
        self.system_output = create_readonly_text_edit("system_output")
        system_group.addWidget(self.system_output)
        layout.addLayout(system_group)

        return layout

    def _log(self, message: str) -> None:
        self.log_output.append(message)
        QApplication.processEvents()

    def _select_file(self) -> None:
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select the .reg file to compare", "", "Registry Files (*.reg);;All Files (*.*)"
        )
        if file_path:
            self.input_file_path = file_path
            self.selected_file_label.setText(f"Selected: {os.path.basename(file_path)}")
            self.btn_compare.setEnabled(True)
            self._log(f"Input file selected: {file_path}")
        else:
            self.selected_file_label.setText("File selection cancelled.")
            self.btn_compare.setEnabled(False)

    def _filter_results(self, filter_type: str) -> None:
        if not self.comparison_results:
            return

        self.reg_file_output.clear()
        self.system_output.clear()

        current_path = None
        for result in self.comparison_results:
            if self._should_show_result(result, filter_type):
                if current_path != result.path:
                    if current_path is not None:
                        self.reg_file_output.append("")
                        self.system_output.append("")
                    self.reg_file_output.append(f"[{result.path}]")
                    self.system_output.append(f"[{result.path}]")
                    current_path = result.path

                self.reg_file_output.append(f'  "{result.key_name}"={result.file_display}')
                self.system_output.append(f'  "{result.key_name}"={result.system_display}')

    def _should_show_result(self, result: ComparisonResult, filter_type: str) -> bool:
        filter_map = {
            "all": True,
            "matches": result.match_status == ComparisonStatus.MATCH.value,
            "differences": result.match_status == ComparisonStatus.DIFFERENT.value,
            "missing": result.match_status == ComparisonStatus.MISSING.value,
        }
        return filter_map.get(filter_type, False)

    def _compare_registry(self) -> None:
        if not self.input_file_path:
            self._log("Error: No input file has been selected.")
            return

        self._log("\nStarting registry comparison...")
        self._clear_comparison_outputs()

        try:
            parsed_settings = self._parse_input_file()
            comparison_stats = self._perform_comparison(parsed_settings)
            self._enable_filter_buttons()
            self._show_comparison_summary(comparison_stats)
            self._show_completion_dialog(comparison_stats)
        except Exception as e:
            self._handle_error(str(e))

    def _clear_comparison_outputs(self) -> None:
        self.reg_file_output.clear()
        self.system_output.clear()
        self.comparison_results = []

    def _parse_input_file(self) -> Dict[str, Dict[str, str]]:
        self._log("Step 1: Parsing .reg file...")
        parsed_settings = parse_reg_file(self.input_file_path)
        self._log(f"Parsing complete. Found {len(parsed_settings)} key sections.")
        return parsed_settings

    def _perform_comparison(self, parsed_settings: Dict[str, Dict[str, str]]) -> Dict[str, int]:
        self._log("Step 2: Comparing values...")

        stats = {"total": 0, "matches": 0, "differences": 0, "missing": 0, "errors": 0}

        for path, keys in parsed_settings.items():
            self._add_path_headers(path)

            for key_name, file_value in keys.items():
                result = self._compare_single_value(path, key_name, file_value)
                self.comparison_results.append(result)
                self._update_stats(stats, result.match_status)
                self._add_comparison_output(result)

            self._add_section_separator()

        return stats

    def _add_path_headers(self, path: str) -> None:
        self.reg_file_output.append(f"[{path}]")
        self.system_output.append(f"[{path}]")

    def _compare_single_value(self, path: str, key_name: str, file_value: str) -> ComparisonResult:
        full_key_path = f'{path}\\{key_name}'
        system_value, system_status = get_current_registry_value(full_key_path, self._log)
        match_status, file_display, system_display = compare_values(file_value, system_value, system_status)

        return ComparisonResult(
            path=path,
            key_name=key_name,
            file_value=file_value,
            system_value=system_value,
            file_display=file_display,
            system_display=system_display,
            match_status=match_status,
            system_status=system_status
        )

    def _update_stats(self, stats: Dict[str, int], match_status: str) -> None:
        stats["total"] += 1
        if match_status == ComparisonStatus.MATCH.value:
            stats["matches"] += 1
        elif match_status == ComparisonStatus.DIFFERENT.value:
            stats["differences"] += 1
        elif match_status == ComparisonStatus.MISSING.value:
            stats["missing"] += 1
        elif match_status == ComparisonStatus.ERROR.value:
            stats["errors"] += 1

    def _add_comparison_output(self, result: ComparisonResult) -> None:
        self.reg_file_output.append(f'  "{result.key_name}"={result.file_display}')
        self.system_output.append(f'  "{result.key_name}"={result.system_display}')

    def _add_section_separator(self) -> None:
        self.reg_file_output.append("")
        self.system_output.append("")

    def _enable_filter_buttons(self) -> None:
        for button in self.filter_buttons:
            button.setEnabled(True)

    def _show_comparison_summary(self, stats: Dict[str, int]) -> None:
        self._log(f"\n📊 COMPARISON SUMMARY:")
        self._log(f"  Total keys compared: {stats['total']}")
        self._log(f"  {STATUS_MATCH} Matches: {stats['matches']}")
        self._log(f"  🔄 Differences: {stats['differences']}")
        self._log(f"  {STATUS_NOT_FOUND} Missing from system: {stats['missing']}")
        self._log(f"  {STATUS_ERROR} Errors: {stats['errors']}")
        self._log("Comparison complete.")

    def _show_completion_dialog(self, stats: Dict[str, int]) -> None:
        message = (
            f"Registry comparison finished!\n\n"
            f"Total: {stats['total']} keys\n"
            f"Matches: {stats['matches']}\n"
            f"Differences: {stats['differences']}\n"
            f"Missing: {stats['missing']}\n"
            f"Errors: {stats['errors']}"
        )
        QMessageBox.information(self, "Comparison Complete", message)

    def _handle_error(self, error_message: str) -> None:
        formatted_error = f"{STATUS_ERROR} ERROR: {error_message}"
        self._log("\n----")
        self._log(formatted_error)
        self._log("----")
        QMessageBox.critical(self, "Operation Error", error_message)
