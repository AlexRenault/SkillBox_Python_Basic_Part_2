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
    # Устанавливаем текущую папку.
    os.chdir(folder)
    items = os.listdir()  # Список объектов в текущей папке
    # Перебираем все объекты в текущей папке
    for item in items:
        item.lower()  # Переводим название объекта в нижний регистр

        if os.path.isfile(item) and item[-3::] == '.py':
            print('\nФайл - ', item)
            count = 0
            # Если объект является файлом и имеет расширение .py открываем его для чтения
            with open(item, 'r', encoding='UTF - 8') as file_read:
                for line in file_read:
                    # Удаляем пробелы в начале и конце очередной строки файла
                    clear_line = line.strip()
                    if len(clear_line) > 0 and clear_line[:1:] != ignore:
                        # Если длина строки больше 0 и не содержит символ
                        # комментария, то увеличиваем счетчик.
                        count += 1
                # После проверки всех строк файла, возвращаем количество строк с кодом.
                yield count


count_string = search_file('test')
for i_count in count_string:
    print('Количество строк кода - ', i_count)
