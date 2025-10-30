import os
import re
from mutagen.mp4 import MP4
from pathlib import Path

# --- Configuration ---
# Set the directory containing your video files.
# Use an absolute path or run the script from the correct directory.
DIRECTORY = "/home/franks/Videos/潜伏"


# --- Main Script ---
def rename_and_tag_files_no_leading_zeros(directory):
    """
    Renames files with a numeric prefix and updates their title metadata,
    removing any leading zeros from the number.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory not found at {directory}")
        return

    print(f"Processing directory: {directory}")
    for filename in os.listdir(directory):
        old_path = Path(directory) / filename

        if not old_path.is_file():
            continue

        match = re.match(r'^(\d+)\.(.*)', filename)
        if match:
            # Extract the number and the rest of the filename
            number_with_zeros = match.group(1)
            rest_of_name = match.group(2)

            # Remove leading zeros from the number string
            number = number_with_zeros.lstrip('0')
            if not number:  # Handle the special case where the number is just "0"
                number = "0"

            # Form the new filename and path
            new_filename = f"{number}{Path(filename).suffix}"
            new_path = Path(directory) / new_filename

            # 1) Rename the file
            try:
                # Only rename if the new filename is different
                if old_path.name != new_filename:
                    os.rename(old_path, new_path)
                    print(f"Renamed: '{filename}' -> '{new_filename}'")
                else:
                    print(f"No rename needed for: '{filename}'")
            except OSError as e:
                print(f"Error renaming {filename}: {e}")
                continue

            # 2) Edit the video metadata (for MP4 files)
            if new_path.suffix.lower() == '.mp4':
                try:
                    video = MP4(new_path)
                    video['\xa9nam'] = [number]  # Set the title tag
                    video.save()
                    print(f"Updated metadata title for '{new_filename}' to '{number}'")
                except Exception as e:
                    print(f"Error updating metadata for {new_filename}: {e}")
            else:
                print(f"Skipped metadata update for non-MP4 file: {new_filename}")


if __name__ == "__main__":
    # Remember to set this to your target directory
    rename_and_tag_files_no_leading_zeros(DIRECTORY)
