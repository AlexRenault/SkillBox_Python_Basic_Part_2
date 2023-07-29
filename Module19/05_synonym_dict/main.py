# TODO здесь писать код
pair_words = int(input('Введите количество пар слов: '))
synonyms = dict()

for index in range(pair_words):
    text = input(f'{index + 1} пара: ').lower()
    pair = text.split()
    for i_pair in pair:
        if not i_pair.isalpha():
            pair.remove(i_pair)
    synonyms[pair[0]] = pair[1]
    synonyms[pair[1]] = pair[0]

print(synonyms)

print('\nПоиск синонимов. Для завершения введите "стоп".')
user_word, synonim = '', ''

while user_word != 'стоп':
    user_word = input('Введите слово: ').lower()
    if user_word in synonyms.keys():
        synonim = 'Синоним: ' + synonyms[user_word].title()
#    elif user_word in synonyms.values():
#        key_print = [key for key, value in synonyms.items() if user_word == value]
#        synonim = 'Синоним: ' + key_print[0].title()
    elif user_word != 'стоп':
       synonim = 'Такого слова в словаре нет.'
    print(synonim)
