# TODO здесь писать код
special_char = '@№$%^&\*()'

file_name = input('Название файла: ').lower()

# Вариант 1
print('Ошибка: название начинается на один из специальных символов.')\
    if file_name[0] in special_char else\
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')\
    if not (file_name.endswith('.txt') or file_name.endswith('.docx')) else print('Файл назван верно.')

# Вариант 2
ext_file = ['.txt', '.docx']
flag = False
flag_1 = True

print()
for char in special_char:
    if file_name.startswith(char):
        flag = True
        break

for item in ext_file:
    if file_name.endswith(item):
        flag_1 = False

if flag_1:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
elif flag:
    print('Ошибка: название начинается на один из специальных символов.')
else:
    print('Файл назван верно.')