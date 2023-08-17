# TODO здесь писать код
def count_letter(user_str, abc):
    count_sorted = {}
    count = {letter: user_str.count(letter) for letter in abc if user_str.count(letter) > 0}

    num_letters = sum(count.values())
    for key, val in count.items():
        count[key] = round(val / num_letters, 3)

    for i in sorted(count, key=count.get, reverse=True):
        count_sorted[i] = count[i]

    str_to_file = ''
    for key, val in count_sorted.items():
        str_to_file += ''.join([key, ' ', str(val), '\n'])

    return str_to_file


abc_low = 'abcdefghijklmnopqrstuvwxyz'

file_read = open('text.txt', 'r', encoding='utf-8')
string_from_file = file_read.read().lower()
analys_str = count_letter(string_from_file, abc_low)
file_read.close()

file_save = open('analysis.txt', 'w')
file_save.write(analys_str)
file_save.close()
