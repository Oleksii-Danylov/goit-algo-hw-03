#!/usr/bin/python3
'''
Завдання 1

Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, назви яких базуються на розширенні файлів.



Також візьміть до уваги наступні умови:



1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).



2. Рекурсивне читання директорій:

Має бути написана функція, яка приймає шлях до директорії як аргумент.
Функція має перебирати всі елементи у директорії.
Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
Якщо елемент є файлом, він має бути доступним для копіювання.


3. Копіювання файлів:

Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
Файл з відповідним типом має бути скопійований у відповідну піддиректорію.


4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.

'''

import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help)
    parser.add_argument("destination", nargs="?", default="dist", help="(default: dist)")
    return parser.parse_args()

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {path}: {e}")
        raise

def copy_and_sort_files(src_dir, dst_dir):
    #Рекурсивно виконуємо копіювання і сортування файлів
    try:
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = os.path.join(root, file)

                # Витягуємо розширення файлу та створюємо відповідний підкаталог
                file_ext = os.path.splitext(file)[-1].lower().lstrip('.') or "no_extension"
                dst_subdir = os.path.join(dst_dir, file_ext)
                create_directory(dst_subdir)

                 # Копіюємо файл до підкаталогу dst
                try:
                    shutil.copy2(file_path, dst_subdir)
                    print(f"Copied {file_path} to {dst_subdir}")
                except (OSError, shutil.Error) as e:
                    print(f"Error copying file {file_path}: {e}")

    except Exception as e:
        print(f"Error processing directory {src_dir}: {e}")
        raise

def main():
    args = parse_arguments()

    src_dir = args.source
    dst_dir = args.destination

    if not os.path.exists(src_dir):
        print(f"src dir {src_dir} does not exist.")
        return

    try:
        create_directory(dst_dir)
        copy_and_sort_files(src_dir, dst_dir)
        print(f"Files copied and sorted {dst_dir}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
     main()