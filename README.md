# Move Latest Downloaded File(s)/Folder(s)

This script moves the latest downloaded file(s)/folder(s) from the "Downloads" folder to a target folder (or subfolder) located on the Desktop. If no target folder is specified, the files will be moved directly to the Desktop. You can specify the number of items to move, and the script will confirm the action if more than 5 items are to be moved.

## Usage:

1. Navigate to the root of the project.
2. Run the script using the following command:

python move.py [target_folder] [num_items]

- `[target_folder]`: (Optional) The name of the folder on your Desktop where the files will be moved. If omitted, the files will be moved directly to the Desktop.
- `[num_items]`: (Optional) The number of items you want to move. If omitted, only the latest file will be moved.
