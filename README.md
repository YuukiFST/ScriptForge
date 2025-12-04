# Registry Utility

<p align="center">
  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/PyQt6-6.4+-green.svg" alt="PyQt6">
  <img src="https://img.shields.io/badge/platform-Windows-lightgrey.svg" alt="Windows">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="MIT License">
</p>

A comprehensive Python application with a modern graphical interface that combines registry comparison and backup generation functionalities for Windows `.reg` files.

## 🎯 Features

### Registry Comparison
- **Intelligent Comparison**: Compare values from `.reg` files with the current system registry
- **Difference Detection**: Identify values that match, differ, or are missing from the system
- **Visual Filters**: Filter results by type (all, matches, differences, missing)
- **Side-by-Side Display**: Easy visual comparison with color-coded panels

### Registry Backup Generation
- **Smart Backup Creation**: Generate rollback files based on proposed registry changes
- **Current Value Detection**: Automatically detect existing registry values
- **Missing Key Handling**: Handle keys that don't exist in the system
- **Rollback Safety**: Create safe restoration points before applying changes

### Modern Interface
- **Dark Theme**: Modern dark design with rounded corners and shadows
- **Tabbed Interface**: Organized functionality in separate tabs
- **Roboto Fonts**: Clean, modern typography
- **Visual Feedback**: Color-coded results and status indicators

## 📦 Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/YuukiFST/RegUtility.git
cd RegUtility

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Quick Install

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Running the Application

```bash
# Using the module
python -m regutility

# Or using the installed script
regutility
```

### Registry Comparison
1. **Select File**: Click "1. Select .reg File" in the Compare Registry tab
2. **Run Comparison**: Click "2. Compare Registry Values"
3. **View Results**: Results appear in side-by-side panels
4. **Filter Results**: Use filter buttons to focus on specific types

### Backup Generation
1. **Select File**: Click "1. Select .reg File" in the Generate Backup tab
2. **Generate Backup**: Click "2. Generate Backup"
3. **Choose Location**: Select where to save the backup file
4. **Confirmation**: Receive confirmation of successful backup creation

## 📊 Result Types

- ✅ **Matches**: Identical values between file and system
- 🔄 **Differences**: Values that exist but are different
- ❌ **Missing**: Keys/values that do not exist in the system
- ⚠️ **Errors**: Access or read problems

## 🛠️ Requirements

- **Python**: 3.9 or higher
- **OS**: Windows (for registry access)
- **Dependencies**: PyQt6 6.4+

## 📁 Project Structure

```
RegUtility/
├── src/
│   └── regutility/
│       ├── __init__.py           # Package initialization
│       ├── __main__.py           # Entry point
│       ├── app.py                # Application initialization
│       ├── core/                 # Core functionality
│       │   ├── parser.py         # .reg file parsing
│       │   ├── registry.py       # Registry operations
│       │   ├── comparison.py     # Comparison logic
│       │   └── backup.py         # Backup generation
│       ├── models/               # Data models
│       │   ├── enums.py          # Enum definitions
│       │   └── data.py           # Dataclass models
│       ├── ui/                   # User interface
│       │   ├── main_window.py    # Main window
│       │   ├── compare_tab.py    # Compare tab
│       │   ├── backup_tab.py     # Backup tab
│       │   └── widgets.py        # Reusable widgets
│       ├── styles/               # Styling
│       │   └── themes.py         # Theme definitions
│       └── utils/                # Utilities
│           └── constants.py      # Constants
├── tests/                        # Test suite
├── docs/                         # Documentation
├── pyproject.toml               # Package configuration
├── requirements.txt             # Dependencies
└── README.md
```

## 🔧 Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/
isort src/

# Type checking
mypy src/
```

## 🎨 Visual Characteristics

- **Modern Dark Theme**: Non-transparent dark background with shadow effects
- **Rounded Corners**: Smooth, modern interface elements
- **Color-Coded Panels**: Distinct colors for easy identification
- **Roboto Typography**: Professional, readable fonts
- **Depth Effects**: Subtle shadows for visual hierarchy

## 📝 Use Cases

### Registry Comparison
- Verify if registry modifications have been applied
- Compare configurations between systems
- Audit registry changes
- Debug configuration issues

### Backup Generation
- Create safety backups before applying registry changes
- Generate rollback files for system restoration
- Prepare for safe registry modifications
- Maintain system recovery options

## 👨‍💻 Author

**Fausto Yuuki**
- Discord: yuuki_0711

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
