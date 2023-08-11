nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# TODO здесь писать код

def ext_list(user_lst, lst=[]):

    for item in user_lst:
        if isinstance(item, list):
            ext_list(item)
        else:
            lst.append(item)
    return lst


print('Исходный список: ', nice_list)
print('Ответ: ', ext_list(nice_list))
