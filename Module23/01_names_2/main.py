# TODO здесь писать код
total_sym = 0
num_line = 1
err_list = []
with open('people.txt', 'r', encoding='utf - 8') as file_read:
    for i_line in file_read:
        total_sym += len(i_line.rstrip())

        try:
            if len(i_line.rstrip()) <= 2:
                raise ValueError('Количество символов в имени меньше или равно 2')
        except ValueError:
            err_list += ''.join(['Ошибка: менее трёх символов в строке ', str(num_line), '\n'])
            print('Ошибка: менее трёх символов в строке ' + str(num_line))
        num_line += 1

print('Общее количество символов: ', total_sym)

with open('errors.log', 'w', encoding='utf - 8') as file_save:
    for i_line in err_list:
        file_save.write(i_line)
