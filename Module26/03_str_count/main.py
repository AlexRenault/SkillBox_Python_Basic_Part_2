# TODO здесь писать код
import os
from collections.abc import Iterable


def search_file(folder=None) -> Iterable:
    """Функция поиска файлов *.py в указанной папке.
        Папка должна находиться в текущей директории
        :rtype: int
    """
    ignore = '#'
    if not folder is None:
        folder = ' ' + folder  # Без добавления пробела выдает ошибку
    # FileNotFoundError: [WinError 2] Не удается найти указанный
    #  файл: 'test'
    else:
        folder = os.getcwd()
    os.chdir(folder)
    items = os.listdir()
    for item in items:
        item.lower()
        if os.path.isfile(item) and item[-3::] == '.py':
            print('\nФайл - ', item)
            count = 0
            with open(item, 'r', encoding='UTF - 8') as file_read:
                for line in file_read:
                    clear_line = line.strip()
                    if len(clear_line) > 0 and clear_line[:1:] != ignore:
                        count += 1
                yield count


count_string = search_file('test')
for i_count in count_string:
    print('Количество строк кода - ', i_count)
