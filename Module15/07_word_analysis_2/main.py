# TODO здесь писать код
word = input('Введите слово: ')
word_list = []

word_list.extend(word)

# С использование нарезки
reverse_word = word_list[:: -1]

# С использованием функции reversed
#reverse_word = list(reversed(word_list))

# С использование цикла for
#for index in range(len(word_list) - 1, -1, -1):
#    reverse_word.append(word_list[index])

if word_list == reverse_word:
    print('Слово является полиндромом.')
else:
    print('Слово не является полиндромом.')

print(word_list)
print(reverse_word)