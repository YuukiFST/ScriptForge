from enum import Enum


class ComparisonStatus(Enum):
    MATCH = "match"
    DIFFERENT = "different"
    MISSING = "missing"
    ERROR = "error"
    NOT_WINDOWS = "not_windows"


class SystemStatus(Enum):
    FOUND = "found"
    NOT_FOUND = "not_found"
    ERROR = "error"
    NOT_WINDOWS = "not_windows"
