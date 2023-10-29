# TODO здесь писать код
import os


def error_log_generator(file) -> str:
    with open(file, 'r', encoding='utf-8') as read_file:  # Открываем файл для чтения
        for line in read_file:  # построчно считываем информацию из файла
            clear_line = line.strip()  # Удаляем из строки лишние символы
            if clear_line[:5] == 'ERROR':  # Если строка начинается с ERROR, то возвращаем эту строку
                yield ''.join((clear_line, '\n'))


# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
if not os.path.exists(input_file_path):
    print(f'{input_file_path} - не существует.')
    raise FileNotFoundError

output_file_path = os.path.abspath(os.path.join('data', 'err_log.txt'))
# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/

with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")