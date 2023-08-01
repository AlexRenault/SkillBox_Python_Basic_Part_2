# TODO здесь писать код
def sort_tpl(user_tpl):
    if sum(list(user_tpl[:])) % 1 == 0:
        user_tpl = tuple(sorted(list(tuple(user_tpl))))
    return user_tpl


# user_tuple = (6, 3, -1, 8, 4, 2, 10, -5)
user_tuple = (6, 3, -1, 8.1, 4, 2, 10, -5)

print(sort_tpl(user_tuple))
