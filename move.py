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

def move_downloads_to_target_folder(target_folder, num_items=1):
    downloads_folder = Path.home() / "Downloads"

    if not downloads_folder.exists():
        print(f"Error: The Downloads folder '{downloads_folder}' does not exist.")
        return

    # Get the list of downloaded files and folders (excluding hidden ones)
    downloaded_items = [f for f in downloads_folder.iterdir() if not f.name.startswith(".")]

    if not downloaded_items:
        print("No downloaded items found.")
        return

    # Sort items by modification time (most recent first)
    downloaded_items.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    target_folder = find_target_folder_on_desktop(target_folder)

    if not target_folder:
        print(f"Error: The folder '{target_folder}' was not found on the Desktop or its subfolders.")
        return

    # Confirm the action if more than 5 items are to be moved
    if num_items > 5:
        confirm = input(f"Warning: You are about to move {num_items} items. Are you sure you want to continue? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Action aborted.")
            return

    # Attempt to move the latest 'num_items' items
    items_moved = 0
    for i in range(min(num_items, len(downloaded_items))):
        try:
            shutil.move(str(downloaded_items[i]), target_folder)
            items_moved += 1
        except Exception as e:
            print(f"Error while moving the item '{downloaded_items[i]}': {e}")

    if items_moved > 0:
        print(f"Successfully moved {items_moved} item(s) to '{target_folder}'.")
    else:
        print("No items were moved.")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python move.py <target_folder> [num_items]")
    else:
        target_folder = sys.argv[1]
        num_items = int(sys.argv[2]) if len(sys.argv) == 3 else 1
        move_downloads_to_target_folder(target_folder, num_items)
