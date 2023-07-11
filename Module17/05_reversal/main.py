# TODO здесь писать код
user_string = input('Введите строку, в которой буква h встречается как минимум два раза: ')

new_string = user_string[user_string.find('h') + 1:user_string.rfind('h')]

print('Развернутая последовательность между первым и последним h: ', new_string[::-1])


