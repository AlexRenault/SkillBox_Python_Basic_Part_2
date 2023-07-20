# TODO здесь писать код
text = input('Введите строку: ').split()

len_word = [len(word) for word in text]
max_length = max(len_word)
long_word = text[len_word.index(max_length)]

print('Самое длинное слово: ', long_word)
print('Длина этого слова: ', max_length)

long_word = ''
max_length = 0

for word in text:
    if len(word) > max_length:
        long_word = word
        max_length = len(word)

print('Самое длинное слово: ', long_word)
print('Длина этого слова: ', max_length)