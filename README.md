# DownloadSorter

A simple Python tool that automatically organizes files in your Downloads folder into categorized directories based on their file extensions.

## Features

- **Automatic file classification:** Identifies files based on their extensions.
- **Categorized organization:** Moves files into predefined directories.
- **Duplicate handling:** Avoids filename conflicts by adding a numeric suffix to duplicate files.
- **Dry-run mode:** Simulates file organization without actually moving files.
- **Customizable categories:** File categories and supported extensions can be modified in `config.py`.

## Project Structure

```text
DownloadSorter/
├── config.py
├── classifier.py
├── organizer.py
└── main.py
```

## Requirements

- Python 3.15 or later
- No external dependencies required.

The project uses Python's standard library.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/E-brinca64/DownloadSorter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd DownloadSorter
   ```

3. Run the program:

   ```bash
   python3 main.py
   ```

## Dry-run Mode

DownloadSorter includes a dry-run mode to preview file organization before making changes.

When enabled, the program displays where each file would be moved without actually moving files or creating destination directories.

To perform actual file organization, change the `DRY_RUN` variable in `main.py` to `False`.

**Recommendation:** Keep dry-run enabled when testing the program.

## Configuration

You can customize file categories and extensions in `config.py`.

For example:

```python
'Pictures/Geral': ['.jpg', '.jpeg', '.png', '.webp'],
'Documents/Pdf': ['.pdf'],
'Music/Geral': ['.mp3', '.wav', '.flac'],
```

Files that do not match any configured extension are placed in the `Geral` directory.

## Compatibility

Developed and tested on Linux. Windows and macOS compatibility have not been tested.

---

**Language:** [Português (Brasil)](README.pt.md)