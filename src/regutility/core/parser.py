from typing import Dict, Tuple, Optional
from regutility.utils.constants import REG_FILE_HEADER, REG_FILE_ENCODINGS

def read_file_with_encoding_fallback(file_path: str) -> str:
    for encoding in REG_FILE_ENCODINGS:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            continue
    raise IOError(f'Could not read file with any supported encoding: {file_path}')

def validate_reg_file_format(content: str) -> None:
    lines = content.splitlines()
    if not lines or REG_FILE_HEADER not in lines[0]:
        raise ValueError('Invalid or unsupported .reg file format.')

def parse_registry_line(line: str) -> Tuple[Optional[str], Optional[str]]:
    if '=' not in line:
        return (None, None)
    try:
        key, value = line.split('=', 1)
        return (key.strip().strip('"'), value.strip())
    except ValueError:
        return (None, None)

def is_registry_path_line(line: str) -> bool:
    return line.startswith('[') and line.endswith(']')

def extract_registry_path(line: str) -> str:
    return line[1:-1]

def parse_reg_file(file_path: str) -> Dict[str, Dict[str, str]]:
    content = read_file_with_encoding_fallback(file_path)
    validate_reg_file_format(content)
    registry_settings: Dict[str, Dict[str, str]] = {}
    current_path = ''
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith(';'):
            continue
        if is_registry_path_line(line):
            current_path = extract_registry_path(line)
            registry_settings[current_path] = {}
        elif current_path:
            key, value = parse_registry_line(line)
            if key and value:
                registry_settings[current_path][key] = value
    return registry_settings