import base64
from typing import List
from dataclasses import dataclass


@dataclass
class Ps1ConversionOptions:
    use_base64_encoding: bool = True
    hide_window: bool = False
    run_as_admin: bool = False
    bypass_execution_policy: bool = True


def encode_ps1_to_base64(ps1_content: str) -> str:
    encoded_bytes = ps1_content.encode('utf-16-le')
    return base64.b64encode(encoded_bytes).decode('ascii')


def build_powershell_command(options: Ps1ConversionOptions) -> List[str]:
    cmd_parts = ['powershell', '-NoProfile']
    if options.bypass_execution_policy:
        cmd_parts.append('-ExecutionPolicy Bypass')
    if options.hide_window:
        cmd_parts.append('-WindowStyle Hidden')
    return cmd_parts


def generate_bat_from_ps1_inline(ps1_content: str, options: Ps1ConversionOptions) -> str:
    ps1_escaped = ps1_content.replace('"', '\\"').replace('%', '%%')
    ps1_escaped = ps1_escaped.replace('\r\n', '; ').replace('\n', '; ')
    cmd_parts = build_powershell_command(options)
    cmd_parts.append(f'-Command "{ps1_escaped}"')
    return '@echo off\r\n' + ' '.join(cmd_parts)


def generate_bat_from_ps1_base64(ps1_content: str, options: Ps1ConversionOptions) -> str:
    encoded = encode_ps1_to_base64(ps1_content)
    cmd_parts = build_powershell_command(options)
    cmd_parts.append(f'-EncodedCommand {encoded}')
    return '@echo off\r\n' + ' '.join(cmd_parts)


def generate_bat_from_ps1_admin(ps1_content: str, options: Ps1ConversionOptions) -> str:
    encoded = encode_ps1_to_base64(ps1_content)
    admin_check = [
        '@echo off',
        '',
        'net session >nul 2>&1',
        'if %errorLevel% neq 0 (',
        '    echo Requesting administrator privileges...',
        "    powershell -Command \"Start-Process -FilePath '%~f0' -Verb RunAs\"",
        '    exit /b',
        ')',
        '',
    ]
    cmd_parts = build_powershell_command(options)
    cmd_parts.append(f'-EncodedCommand {encoded}')
    return '\r\n'.join(admin_check) + ' '.join(cmd_parts)


def convert_ps1_to_bat(ps1_content: str, options: Ps1ConversionOptions) -> str:
    if options.run_as_admin:
        return generate_bat_from_ps1_admin(ps1_content, options)
    if options.use_base64_encoding:
        return generate_bat_from_ps1_base64(ps1_content, options)
    return generate_bat_from_ps1_inline(ps1_content, options)


def convert_ps1_file_to_bat(file_path: str, options: Ps1ConversionOptions) -> str:
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        ps1_content = f.read()
    return convert_ps1_to_bat(ps1_content, options)