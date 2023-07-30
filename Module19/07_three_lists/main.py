# TODO здесь писать код

def without_task1(arr_1, arr_2, arr_3):
    in_array = []
    for i_arr_1 in arr_1:
        if i_arr_1 in arr_2 and i_arr_1 in arr_3:
            in_array.append(i_arr_1)
    return in_array


def without_task2(arr_1, arr_2, arr_3):
    no_array = []
    for i_arr_1 in arr_1:
        if i_arr_1 not in arr_2 and i_arr_1 not in arr_3:
            no_array.append(i_arr_1)
    return no_array


def with_task1(arr_1, arr_2, arr_3):
    return set(arr_1) & set(arr_2) & set(arr_3)


def with_task2(arr_1, arr_2, arr_3):
    return set(arr_1) - set(arr_2) - set(arr_3)


array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1: ')
print('\t. Решение без множеств: ', without_task1(array_1, array_2, array_3))
print('\t. Решение c множествами: ', sorted(with_task1(array_1, array_2, array_3)))

print('Задача 2: ')
print('\t. Решение без множеств: ', without_task2(array_1, array_2, array_3))
print('\t. Решение c множествами: ', sorted(with_task2(array_1, array_2, array_3)))
