# TODO здесь писать код
def summ_f(*args, lst=[]):
    data = []

    for item in args:
        if isinstance(item, list):
            data = item
        else:
            data = list(args)
            break

    for item in data:
        if isinstance(item, list):
            summ_f(item)
        else:
            lst.append(item)

    return sum(lst)


# [[1, 2, [3]], [1], 3]
# 1, 2, 3, 4, 5

print('Ответ в консоли: ', summ_f([[[[1, 2, [3]], [1]], 3]]))
