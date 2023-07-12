# TODO здесь писать код
abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#index_abc = 0
text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

#new_text = ''
#for letter in text:
#    if letter in abc:
#        if abc.index(letter) + shift >= len(abc) - 1:
#            index_abc = abc.index(letter) + shift - len(abc)
#        else:
#            index_abc = abc.index(letter) + shift
#        new_text += abc[index_abc]
#    else:
#        new_text += letter

#print('Зашифрованное сообщение: ', new_text)

new_text = [abc[(abc.find(letter) + shift) % 33] if letter in abc else letter for letter in text]
encrypt_text = ''
for letter in new_text:
    encrypt_text += letter

print('Зашифрованное сообщение: ', encrypt_text)