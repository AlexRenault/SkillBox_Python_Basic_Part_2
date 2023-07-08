# TODO здесь писать код
num_list = []
append_list = []

number = int(input('Количество чисел: '))
for _ in range(number):
    num_list.append(int(input('Число: ')))

print('Последовательность: ', num_list)

i_num = len(num_list) - 1
while num_list != num_list[::-1]:
    num_list.append(num_list[i_num - 1])
    append_list.append(num_list[i_num - 1])
    i_num -=1

if len(append_list) == 0:
    print('Последовательность симметрична. Приписывать числа не нужно.')
else:
    print('Нужно приписать чисел', len(append_list))
    print('Сами числа: ', append_list)