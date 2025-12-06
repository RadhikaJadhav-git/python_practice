import os
import shutil

path = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Docs": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1]

        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, folder_path)
                print(f"Moved: {file} → {folder}")
                break
