import os
import shutil
import sys
from pathlib import Path

def find_target_folder_on_desktop(target_folder):
    """Recursively searches for a target folder within the Desktop directory."""
    desktop_path = Path.home() / "Desktop"
    for root, dirs, _ in os.walk(desktop_path):
        if target_folder.lower() in [dir.lower() for dir in dirs]:
            return os.path.join(root, target_folder)
    return None

def move_latest_download_to_target_folder(target_folder):
    downloads_folder = Path.home() / "Downloads"

    if not downloads_folder.exists():
        print(f"Error: The Downloads folder '{downloads_folder}' does not exist.")
        return

    # Get the list of downloaded files (excluding hidden files)
    downloaded_files = [f for f in downloads_folder.iterdir() if f.is_file() and not f.name.startswith(".")]

    if not downloaded_files:
        print("No downloaded files found.")
        return

    latest_file = max(downloaded_files, key=lambda f: f.stat().st_mtime)
    target_folder = find_target_folder_on_desktop(target_folder)

    if not target_folder:
        print(f"Error: The folder '{target_folder}' was not found on the Desktop or its subfolders.")
        return

    try:
        shutil.move(str(latest_file), target_folder)
        print(f"Moved '{latest_file}' to '{target_folder}'.")
    except Exception as e:
        print(f"Error while moving the file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python move.py <target_folder>")
    else:
        target_folder = sys.argv[1]
        move_latest_download_to_target_folder(target_folder)
