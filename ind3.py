# /usr/bin/env python3
# -*- coding: utf-8 -*-

import os


# Напишите скрипт на Python, который будет сканировать заданную
# директорию, считывать все файлы и папки в ней, создавать
# текстовый файл directory_contents.txt с этим списком.


def main(directory_path):
    directory_contents = os.listdir(directory_path)

    with open("directory_contents.txt", "w") as file:
        for item in directory_contents:
            file.write(f"{item}\n")

    print(
        f"Список содержимого директории '{directory_path}'"
        f" записан в файл 'directory_contents.txt'."
    )


if __name__ == "__main__":
    main(input())
