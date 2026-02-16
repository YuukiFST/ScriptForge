from dataclasses import dataclass

@dataclass
class ComparisonResult:
    path: str
    key_name: str
    file_value: str
    system_value: str
    file_display: str
    system_display: str
    match_status: str
    system_status: str

@dataclass
class RegistryKey:
    root_key: str
    sub_key_path: str
    value_name: str