# TODO здесь писать код
def summ_f(*args):
    data_sum = 0

    for item in args:
        if isinstance(item, (int, float)):
            data_sum += item
        elif isinstance(item, (list, tuple)):
            data_sum += summ_f(*item)
    return data_sum


# [[1, 2, [3]], [1], 3]
# 1, 2, 3, 4, 5

print('Ответ в консоли: ', summ_f(1, 2, 3, 4, 5))
