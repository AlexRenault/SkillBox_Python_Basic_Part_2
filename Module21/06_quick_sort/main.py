# TODO здесь писать код
nice_list = [29, 19, 47, 11, 6, 19, 24, 12, 17, 23, 11, 71, 41, 36, 71, 13, 18, 32, 26]


def partition(lst):
    list_less, list_more, list_eq = [], [], []
    support = lst[len(lst) - 1]
    for elem in lst:
        if elem == support:
            list_eq.append(elem)
        elif elem < support:
            list_less.append(elem)
        else:
            list_more.append(elem)
    return list_less, list_eq, list_more


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        less, eq, more = partition(lst)
        return quick_sort(less) + eq + quick_sort(more)


print('Исходный список: ', nice_list)
list_sorted = quick_sort(nice_list)
print('Отсортированный список', list_sorted)
