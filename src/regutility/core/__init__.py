from regutility.core.parser import (
    parse_reg_file,
    read_file_with_encoding_fallback,
    validate_reg_file_format,
    parse_registry_line,
)
from regutility.core.registry import (
    is_windows_system,
    parse_registry_key_path,
    get_registry_root_key,
    format_registry_value_by_type,
    query_registry_value,
    get_current_registry_value,
)
from regutility.core.comparison import (
    create_comparison_displays,
    determine_comparison_status,
    compare_values,
)
from regutility.core.backup import (
    create_backup_entry,
    get_backup_registry_value,
    get_current_registry_values_for_backup,
    write_backup_file,
    generate_backup_reg,
)
from regutility.core.converter import (
    ConversionOptions,
    convert_reg_to_bat,
    convert_reg_file_to_bat,
)

__all__ = [
    "parse_reg_file",
    "read_file_with_encoding_fallback",
    "validate_reg_file_format",
    "parse_registry_line",
    "is_windows_system",
    "parse_registry_key_path",
    "get_registry_root_key",
    "format_registry_value_by_type",
    "query_registry_value",
    "get_current_registry_value",
    "create_comparison_displays",
    "determine_comparison_status",
    "compare_values",
    "create_backup_entry",
    "get_backup_registry_value",
    "get_current_registry_values_for_backup",
    "write_backup_file",
    "generate_backup_reg",
    "ConversionOptions",
    "convert_reg_to_bat",
    "convert_reg_file_to_bat",
]
