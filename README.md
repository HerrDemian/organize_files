# File Organization Script

## Overview

`organize_files_by_extension.py` is a Python utility that organizes files by extension into individual folders. Each file is moved into a dedicated folder named after the file (without the extension).

## Features

- **Extension-based organization**: Move all files with a specific extension into separate folders
- **Disc set grouping**: Automatically groups multi-disc files (e.g., "Movie (Disc 1).mp4", "Movie (Disc 2).mp4") into a single folder
- **Safe operation**: Creates folders as needed; doesn't overwrite existing files
- **Recursive support**: Process files in the specified directory

## Requirements

- Python 3.x

## Usage

### Basic Command

```bash
python organize_files_by_extension.py <directory> <extension>
```

### Arguments

- `directory`: Path to the directory containing files to organize
- `extension`: File extension to process (with or without the leading dot)

### Examples

#### Example 1: Organize MP4 files

```bash
python organize_files_by_extension.py . mp4
```

This will move all `.mp4` files in the current directory into individual folders based on their filename.

**Before:**
```
Movie1.mp4
Movie2.mp4
Season1Episode1.mp4
```

**After:**
```
Movie1/
  Movie1.mp4
Movie2/
  Movie2.mp4
Season1Episode1/
  Season1Episode1.mp4
```

#### Example 2: Organize multi-disc files

```bash
python organize_files_by_extension.py /path/to/videos mkv
```

If you have multi-disc files like:
```
Documentary (Disc 1).mkv
Documentary (Disc 2).mkv
Documentary (Disc 3).mkv
```

They will be organized into a single folder:
```
Documentary/
  Documentary (Disc 1).mkv
  Documentary (Disc 2).mkv
  Documentary (Disc 3).mkv
```

#### Example 3: Using dot notation for extension

```bash
python organize_files_by_extension.py ./media .zip
```

Both `.mp4` and `mp4` formats are accepted for the extension parameter.

## Output

The script provides feedback as it processes files:

```
Moved: Movie1.mp4 -> Movie1/
Moved: Movie2.mp4 -> Movie2/
Done. 2 file(s) moved.
```

## Error Handling

The script will report errors for:
- Non-existent directories
- Invalid extensions
- File system issues

All errors are displayed with descriptive messages.

## Notes

- The script processes only files in the specified directory (non-recursive into subdirectories)
- Files are only moved if the source and destination paths are different
- Special handling for disc patterns: `(Disc #)` suffixes are recognized and grouped appropriately
- The script is safe to run multiple times on the same directory
