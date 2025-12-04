# ScriptForge

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/PyQt6-6.4+-green.svg" alt="PyQt6">
  <img src="https://img.shields.io/badge/platform-Windows-lightgrey.svg" alt="Windows">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="MIT License">
</p>

A Windows scripting toolkit with a modern dark interface for registry management and script conversion.

## Features

### Registry Tools
- **Compare Registry**: Compare `.reg` files with system registry values
- **Generate Backup**: Create rollback files before applying registry changes

### Script Converters
- **.reg to .bat**: Convert registry files to batch scripts using `REG ADD/DELETE` commands
- **.ps1 to .bat**: Convert PowerShell scripts to standalone batch files with Base64 encoding

### Conversion Options
| Option | Description |
|--------|-------------|
| `@echo off` | Hide command output |
| Status messages | Show processing progress |
| Pause at end | Wait for keypress |
| Base64 encoding | Safe embedding of complex scripts |
| Run as Admin | Auto-elevate with UAC prompt |
| Bypass execution policy | Run without restrictions |

## Installation

### From Source
```bash
git clone https://github.com/YuukiFST/RegUtility.git
cd RegUtility
pip install -r requirements.txt
python -m regutility
```

### Standalone Executable
Download `ScriptForge.exe` from [Releases](https://github.com/YuukiFST/RegUtility/releases).

## Usage

```bash
# Run from source
cd src
python -m regutility

# Or build executable
pip install pyinstaller pillow
pyinstaller --onefile --windowed --name "ScriptForge" --icon "src\regutility\assets\icon.ico" src\regutility\__main__.py
```

## Result Icons

| Icon | Meaning |
|------|---------|
| ✅ | Match - values are identical |
| 📄 | Different in file |
| 🖥️ | Different in system |
| ❌ | Missing from system |
| ⚠️ | Error accessing value |

## Project Structure

```
src/regutility/
├── core/           # Business logic
│   ├── parser.py       # .reg file parsing
│   ├── registry.py     # Registry operations
│   ├── comparison.py   # Value comparison
│   ├── backup.py       # Backup generation
│   ├── converter.py    # .reg to .bat
│   └── ps1_converter.py # .ps1 to .bat
├── ui/             # PyQt6 interface
├── models/         # Data structures
├── styles/         # Dark theme
└── assets/         # App icon
```

## Requirements

- Python 3.9+
- Windows OS
- PyQt6

## Author

**Fausto Yuuki** - Discord: yuuki_0711

## License

MIT License - see [LICENSE](LICENSE)
