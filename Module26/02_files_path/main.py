# TODO здесь писать код
import os
from collections.abc import Iterable


def gen_files_path(find_dir: str, start_path = None) -> Iterable:
    """
    Функция поиска заданной директории и генерации путей ко всем встреченным файлам.
    :param find_dir[str]: папка для поиска
    :param start_path[str]: папка, с которой следует начинать поиск
    :return: путь к очередному файлу или путь к искомой папке.
    """
    if start_path is None:
        start_path = os.sep
    for dirs_path, dirs_name, files in os.walk(start_path):
        for folder in dirs_name:
            if folder == find_dir:
                print(f'папка {find_dir} найдена. Путь к папке - {os.path.join(dirs_path)}')
                os.chdir(os.path.join(dirs_path, folder))
                print('\nТекушая папка - ', os.getcwd())
                return
        for file in files:
            print(f'Файл - {file}. \n\tПуть к файлу - ', end='')
            yield os.path.join(dirs_path, folder)
    else:
        print('Папка не найдена.')


def menu() -> None:
    """Предлагает пользователю выбор возможных действий."""

    print('Меню:')
    print('1. Задать начальный путь.')
    print('2. Начальный путь по умолчанию (корень диска).')
    user_choice = int(input('Ваш выбор 1 или 2? '))
    while user_choice not in (1, 2):
        user_choice = int(input('Ваш выбор 1 или 2? '))
    if user_choice == 2:
        os.chdir(os.sep)
    else:
        user_path = input('Задайте директорию с которой начинаем поиск: ')
        start_path = gen_files_path(user_path)
        print_path(start_path)


def print_path(gen) -> None:
    """Выводит на экран сгенерированные пути"""
    for path in gen:
        print(path)


menu()
search_folder = input('Какую папку ищем?')
find_paths = gen_files_path(search_folder, os.getcwd())
print_path(find_paths)
