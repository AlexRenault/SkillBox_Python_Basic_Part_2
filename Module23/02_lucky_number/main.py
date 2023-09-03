# TODO здесь писать код
import random

except_list = [ValueError, ZeroDivisionError, FileNotFoundError, TabError, TypeError, ArithmeticError]

summ = 0
lucky_number = 777

try:
    with open('out_file.txt', 'w', encoding='utf-8') as file_out:
        err_mess = 'Произошла ошибка. Выполнение программы прервано'
        while summ < lucky_number:
            number = int(input('Введите число: '))
            if random.randint(1, 13) == 13:
                name_except = random.choice(except_list)
                raise name_except
            summ += number
            file_out.write(''.join([str(number), '\n']))

    print('Вы успешно выполнили условие для выхода из порочного цикла!')

except ValueError as err:
    print('Обязательно нужно было ввести число.', err, type(err))
except name_except:
    print(err_mess)
finally:
    if not file_out.closed:
        file_out.close()
