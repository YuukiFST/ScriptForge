import winreg
from typing import Dict, Optional, Callable

from regutility.models import RegistryKey
from regutility.utils.constants import REG_FILE_HEADER, REGISTRY_ROOT_KEYS
from regutility.core.registry import (
    is_windows_system,
    parse_registry_key_path,
    format_registry_value_by_type,
)


def get_registry_root_key(root_key_str: str) -> Optional[int]:
    return REGISTRY_ROOT_KEYS.get(root_key_str)


def create_backup_entry(value_name: str, value, reg_type: int) -> str:
    formatted_value = format_registry_value_by_type(value, reg_type)
    return f'"{value_name}"={formatted_value}\r\n'


def get_backup_registry_value(
    registry_key: RegistryKey, 
    log_callback: Callable[[str], None]
) -> Optional[str]:
    if not is_windows_system():
        return None

    root_key = get_registry_root_key(registry_key.root_key)
    if not root_key:
        log_callback(f"Warning: Unknown root key: {registry_key.root_key}")
        return None

    try:
        with winreg.OpenKey(root_key, registry_key.sub_key_path, 0, winreg.KEY_READ) as key_handle:
            value, reg_type = winreg.QueryValueEx(key_handle, registry_key.value_name)
            return create_backup_entry(registry_key.value_name, value, reg_type)
    except FileNotFoundError:
        return None
    except Exception as e:
        log_callback(f"Error querying value {registry_key.value_name}: {e}")
        return None


def get_current_registry_values_for_backup(
    parsed_settings: Dict[str, Dict[str, str]], 
    log_callback: Callable[[str], None]
) -> Dict[str, str]:
    current_values: Dict[str, str] = {}

    if not is_windows_system():
        log_callback("Warning: Not running on Windows. Backup will only contain deletion entries.")
        return {}

    for path, keys in parsed_settings.items():
        for key_name in keys.keys():
            full_key_path = f'{path}\\{key_name}'
            try:
                registry_key = parse_registry_key_path(full_key_path)
                backup_entry = get_backup_registry_value(registry_key, log_callback)
                if backup_entry:
                    current_values[full_key_path] = backup_entry
            except Exception as e:
                log_callback(f"Error processing key path {full_key_path}: {e}")

    return current_values


def write_backup_file(
    parsed_settings: Dict[str, Dict[str, str]], 
    current_values: Dict[str, str], 
    output_file_path: str
) -> None:
    with open(output_file_path, 'w', encoding='utf-16') as file:
        file.write(f'{REG_FILE_HEADER}\r\n\r\n')

        for path, keys in parsed_settings.items():
            file.write(f'[{path}]\r\n')
            for key_name in keys.keys():
                full_key_path = f'{path}\\{key_name}'
                if full_key_path in current_values:
                    file.write(current_values[full_key_path])
                else:
                    file.write(f'"{key_name}"=-\r\n')
            file.write('\r\n')


def generate_backup_reg(
    parsed_settings: Dict[str, Dict[str, str]], 
    current_values: Dict[str, str], 
    output_file_path: str
) -> None:
    write_backup_file(parsed_settings, current_values, output_file_path)
