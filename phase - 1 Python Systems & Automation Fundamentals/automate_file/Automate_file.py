import os
import shutil

folder_path = (
    "/Users/anujbiswas/Desktop/python_system_engineering_and_automation/"
    "phase - 1 Python Systems & Automation Fundamentals/automate_file/testing"
)
file_types = {
    "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isdir(file_path):
        continue  # Skip directories

    # Error in the original code: os.path.splittext() does not exist.
    # The correct function is os.path.splitext().
    ext = os.path.splitext(filename)[1].lower()

    for folder, extensions in file_types.items():
        if ext in extensions:
            # Error in the original code: this used filename as the folder.
            # The destination must be the matching category folder.
            target_folder = os.path.join(folder_path, folder)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
            break  # Move to the next file after moving the current one.
