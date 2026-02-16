from typing import Tuple
from regutility.models import ComparisonStatus, SystemStatus
from regutility.utils.constants import (
    STATUS_MATCH,
    STATUS_DIFFERENT_FILE,
    STATUS_DIFFERENT_SYSTEM,
    STATUS_NOT_FOUND,
)


def create_comparison_displays(
    file_value: str,
    system_value: str,
    status: ComparisonStatus,
) -> Tuple[str, str]:
    display_map = {
        ComparisonStatus.MATCH: (
            f'{STATUS_MATCH} {file_value}',
            f'{STATUS_MATCH} {system_value}',
        ),
        ComparisonStatus.DIFFERENT: (
            f'{STATUS_DIFFERENT_FILE} {file_value}',
            f'{STATUS_DIFFERENT_SYSTEM} {system_value}',
        ),
        ComparisonStatus.MISSING: (
            file_value,
            f'{STATUS_NOT_FOUND} KEY/VALUE NOT FOUND',
        ),
        ComparisonStatus.ERROR: (file_value, system_value),
        ComparisonStatus.NOT_WINDOWS: (file_value, system_value),
    }
    return display_map.get(status, (file_value, system_value))


def determine_comparison_status(
    file_value: str,
    system_value: str,
    system_status: str,
) -> ComparisonStatus:
    if system_status == SystemStatus.NOT_FOUND.value:
        return ComparisonStatus.MISSING
    elif system_status == SystemStatus.ERROR.value:
        return ComparisonStatus.ERROR
    elif system_status == SystemStatus.NOT_WINDOWS.value:
        return ComparisonStatus.NOT_WINDOWS
    elif file_value.strip() == system_value.strip():
        return ComparisonStatus.MATCH
    else:
        return ComparisonStatus.DIFFERENT


def compare_values(
    file_value: str,
    system_value: str,
    system_status: str,
) -> Tuple[str, str, str]:
    comparison_status = determine_comparison_status(file_value, system_value, system_status)
    file_display, system_display = create_comparison_displays(file_value, system_value, comparison_status)
    return (comparison_status.value, file_display, system_display)