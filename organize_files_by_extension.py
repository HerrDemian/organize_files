#!/usr/bin/env python3
import argparse
import os
import re
import shutil

DISC_PATTERN = re.compile(r"\s*\(Disc\s*\d+\)$", flags=re.IGNORECASE)


def normalize_extension(ext: str) -> str:
    ext = ext.strip()
    if not ext:
        raise ValueError("Extension must not be empty")
    if not ext.startswith("."):
        ext = "." + ext
    return ext.lower()


def disc_folder_name(filename: str) -> str:
    name, _ = os.path.splitext(filename)
    match = DISC_PATTERN.search(name)
    if match:
        return name[: match.start()].rstrip()
    return name


def organize_files(directory: str, extension: str) -> int:
    extension = normalize_extension(extension)
    directory = os.path.abspath(directory)

    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    moved_count = 0
    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if not os.path.isfile(path):
            continue

        _, ext = os.path.splitext(entry)
        if ext.lower() != extension:
            continue

        target_folder_name = disc_folder_name(entry)
        if not target_folder_name:
            target_folder_name = entry[: -len(extension)]

        target_folder_path = os.path.join(directory, target_folder_name)
        os.makedirs(target_folder_path, exist_ok=True)

        destination = os.path.join(target_folder_path, entry)
        if os.path.abspath(path) == os.path.abspath(destination):
            continue

        shutil.move(path, destination)
        moved_count += 1
        print(f"Moved: {entry} -> {target_folder_name}/")

    return moved_count


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Organize files by extension into per-file folders, grouping disc sets together."
    )
    parser.add_argument("directory", help="Directory containing files to organize")
    parser.add_argument("extension", help="File extension to process, e.g. mp4 or .mp4")
    args = parser.parse_args()

    try:
        count = organize_files(args.directory, args.extension)
        print(f"Done. {count} file(s) moved.")
    except Exception as exc:
        print(f"Error: {exc}")
        raise


if __name__ == "__main__":
    main()
