# TODO здесь писать код
import os

dirs_count = 0
files_count = 0
size_folder = 0

# use_path = '/Users/domasnij//SkillBox/Основы Python. Часть 2/Python_Basic/Python_Basic'
use_path = input('Введите путь: ')
os.chdir(use_path)
print()
print(os.getcwd())
elem = []

for dirs_path, dirs_name, files in os.walk(use_path):
    for folder in dirs_name:
        dirs_count += 1
    for file in files:
        files_count += 1
        size_folder += os.path.getsize(os.path.join(dirs_path, file))
        elem.append(os.path.join(dirs_path, folder, file))

print()
print('Количество подкаталогов: ', dirs_count)
print('Количество файлов: ', files_count)
print('Размер каталога в килобайтах: ', size_folder / 1024)

for i_elem in elem:
    print(i_elem)
