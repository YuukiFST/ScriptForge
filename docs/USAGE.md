# Usage Guide

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YuukiFST/RegUtility.git
cd RegUtility

# Install dependencies
pip install -r requirements.txt

# Run the application
python -m regutility
```

## Features

### Compare Registry Tab

The Compare Registry tab allows you to compare values from a `.reg` file with the current Windows system registry.

1. **Select a .reg file** - Click "1. Select .reg File" and choose your registry file
2. **Run comparison** - Click "2. Compare Registry Values"
3. **View results** - Results appear side-by-side:
   - Left panel: Values from your .reg file
   - Right panel: Current system values
4. **Filter results** - Use the filter buttons to show:
   - All results
   - Matches only (✅)
   - Differences only (🔄)
   - Missing only (❌)

### Generate Backup Tab

The Generate Backup tab creates a rollback file before applying registry changes.

1. **Select the .reg file** - Choose the file you plan to apply
2. **Generate backup** - Click "2. Generate Backup"
3. **Choose save location** - Select where to save the backup
4. **Apply changes safely** - If needed, apply the backup to restore original values

## Result Icons

| Icon | Meaning |
|------|---------|
| ✅ | Value matches between file and system |
| 📄 | Value in file differs from system |
| 🖥️ | Value in system differs from file |
| ❌ | Key/value not found in system |
| ⚠️ | Error accessing the registry |

## Tips

- Always create a backup before applying registry changes
- Run as Administrator for access to protected registry keys
- Use the filter buttons to focus on differences
