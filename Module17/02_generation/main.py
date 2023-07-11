# TODO здесь писать код
number = int(input('Введите длину списка: '))

num_list = [1 if num % 2 == 0 else num % 5 for num in range(number)]

print(num_list)