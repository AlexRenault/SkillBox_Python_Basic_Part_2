# TODO здесь писать код
vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']

user_text = input('Введите Ваш текст: ')

user_list = [i_letter for i_letter in user_text if i_letter in vowel_letters]

print('Список гласных букв: ', user_list)
print('Длина списка: ', len(user_list))