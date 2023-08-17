# TODO здесь писать код
import zipfile

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
      'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def extract(arh_name):
    name_pos = arh_name.index('.')
    file_name = ''.join([arh_name[:name_pos], '.txt'])
    with zipfile.ZipFile(arh_name, 'r') as zip_file:
        zip_file.extract(file_name)
    zip_file.close()
    return file_name


def count_letter(text):
    dict_letter = {letter: text.count(letter)
                   for letter in abc if text.count(letter) > 0}
    return dict_letter


def sort_dict(l_dict):
    n_dict = dict()
    for key in sorted(l_dict, key=l_dict.get, reverse=True):
        n_dict[key] = l_dict[key]
    return n_dict


def open_file(file_name):
    file_read = open(file_name, 'r', encoding='utf-8')
    text = file_read.read()
    file_read.close()
    return text


def save_file(file_name, l_dict):
    file_to_save = open(file_name, 'w')
    for key, val in l_dict.items():
        str_to_file = ''.join([key, '-', str(val), '\n'])
        file_to_save.write(str_to_file)
        print(str_to_file, end='')
    file_to_save.close()


file_to_open = extract('voyna-i-mir.zip')
voyna_i_mir = open_file(file_to_open)
letter_dict = count_letter(voyna_i_mir)
new_dict = sort_dict(letter_dict)

file_save = 'stat.txt'
save_file(file_save, new_dict)

not_in_file = [letter for letter in abc if letter not in new_dict.keys()]
print(not_in_file)
