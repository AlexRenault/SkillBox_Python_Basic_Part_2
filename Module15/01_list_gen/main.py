# TODO здесь писать код
number = int(input('Введите целое число, больше 0: '))

num_list = []

for index in range(1, number + 1, 2):
    num_list.append(index)

print('Список из нечетных чисел от 1 до ', number, ':', end=' ')
print(num_list)