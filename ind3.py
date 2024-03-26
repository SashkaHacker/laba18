# /usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def main(directory):
    file_types = {
        ".docx": "Documents",
        ".pdf": "Documents",
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".mp3": "Audio",
        ".wav": "Audio",
        ".mp4": "Video",
        ".avi": "Video",
    }

    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension in file_types:
            new_dir = os.path.join(directory, file_types[file_extension])
            os.makedirs(new_dir, exist_ok=True)
            os.rename(
                os.path.join(directory, filename),
                os.path.join(new_dir, filename),
            )

    print("Файлы были успешно организованы по категориям.")


if __name__ == "__main__":
    main(input())
