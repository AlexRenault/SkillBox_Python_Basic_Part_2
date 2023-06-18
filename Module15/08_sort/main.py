# TODO здесь писать код
num_list = [1, 4, -3, 0, 10]

print('Изначальный список: ', num_list)

# Вариант 1
#for index in range(len(num_list) - 1):
#    for sort_index in range(len(num_list) - 1):
#        if num_list[sort_index] > num_list[index]:
#            num_list[sort_index], num_list[index] = num_list[index], num_list[sort_index]

# Вариант 2
for index in range(len(num_list) - 1):
    min_num = num_list[index]
    for number in range(index, len(num_list) - 1):
        if min_num > num_list[number]:
            min_num, num_list[number] = num_list[number], min_num
    num_list[index] = min_num

print('\nОтсортированный список: ', num_list)