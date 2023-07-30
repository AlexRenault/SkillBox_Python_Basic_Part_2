# TODO здесь писать код
user_str = input('Введите строку: ')
out_str = user_str.lower()
print(out_str)


str_dict = dict()

flag = False
for letter in out_str:
    if letter.isalpha():
        str_dict[letter] = out_str.count(letter)

print(str_dict)

for letter in str_dict.keys():
    if flag and str_dict[letter] % 2 == 1:
        flag = False
        break
    elif str_dict[letter] % 2 == 1:
        flag = True

if flag:
    print(f'Сторку "{user_str}" можно сделать палиндромом')
else:
    print(f'Сторку "{user_str}" нельзя сделать палиндромом')



