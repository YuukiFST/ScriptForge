import os
import winreg
from typing import Tuple, Optional, Callable
from regutility.models import RegistryKey, SystemStatus
from regutility.utils.constants import REGISTRY_ROOT_KEYS, STATUS_NOT_FOUND, STATUS_ERROR


def is_windows_system() -> bool:
    return os.name == 'nt'


def parse_registry_key_path(full_key_path: str) -> RegistryKey:
    parts = full_key_path.split('\\')
    root_key = parts[0]
    sub_key_path = '\\'.join(parts[1:-1])
    value_name = parts[-1]
    return RegistryKey(root_key, sub_key_path, value_name)


def get_registry_root_key(root_key_str: str) -> Optional[int]:
    return REGISTRY_ROOT_KEYS.get(root_key_str)


def format_registry_value_by_type(value, reg_type: int) -> str:
    formatters = {
        winreg.REG_SZ: lambda v: f'"{v}"',
        winreg.REG_EXPAND_SZ: lambda v: f"hex(2):{v.encode('utf-16-le').hex(',')}",
        winreg.REG_DWORD: lambda v: f'dword:{v:08x}',
        winreg.REG_QWORD: lambda v: f'hex(b):{v:016x}',
        winreg.REG_BINARY: lambda v: f"hex:{''.join([f'{b:02x},' for b in v]).rstrip(',')}",
        winreg.REG_MULTI_SZ: lambda v: f"hex(7):{','.join(s.encode('utf-16-le').hex(',') for s in v)}",
    }
    formatter = formatters.get(reg_type)
    if formatter:
        return formatter(value)
    return f'{value} (Type: {reg_type})'


def query_registry_value(
    registry_key: RegistryKey,
    log_callback: Callable[[str], None],
) -> Tuple[str, str]:
    if not is_windows_system():
        return ('N/A (Not on Windows)', SystemStatus.NOT_WINDOWS.value)
    root_key = get_registry_root_key(registry_key.root_key)
    if not root_key:
        log_callback(f'Warning: Unknown root key: {registry_key.root_key}')
        return (f'Unknown root key: {registry_key.root_key}', SystemStatus.ERROR.value)
    try:
        with winreg.OpenKey(root_key, registry_key.sub_key_path, 0, winreg.KEY_READ) as key_handle:
            value, reg_type = winreg.QueryValueEx(key_handle, registry_key.value_name)
            formatted_value = format_registry_value_by_type(value, reg_type)
            return (formatted_value, SystemStatus.FOUND.value)
    except FileNotFoundError:
        return (f'{STATUS_NOT_FOUND} KEY/VALUE NOT FOUND', SystemStatus.NOT_FOUND.value)
    except Exception as e:
        error_msg = f'Error querying value {registry_key.value_name}: {e}'
        log_callback(error_msg)
        return (f'{STATUS_ERROR} ERROR: {e}', SystemStatus.ERROR.value)


def get_current_registry_value(
    full_key_path: str,
    log_callback: Callable[[str], None],
) -> Tuple[str, str]:
    try:
        registry_key = parse_registry_key_path(full_key_path)
        return query_registry_value(registry_key, log_callback)
    except Exception as e:
        log_callback(f'Error processing key path {full_key_path}: {e}')
        return (f'{STATUS_ERROR} ERROR: {e}', SystemStatus.ERROR.value)