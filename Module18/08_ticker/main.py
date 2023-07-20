# TODO здесь писать код
string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')

flag = True

if len(string_1) != len(string_2):
    print('Длины строк не равны. Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    for letter in string_2:
        if not letter in string_1:
            print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
            flag = false
            break
    if flag:
        shift = 0
        while string_2[0] != string_1[shift]:
            shift += 1
        print('Первая строка получается из второй со сдвигом ', shift, '.')
