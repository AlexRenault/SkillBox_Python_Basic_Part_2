# TODO здесь писать код
def zip_function(string, tpl):
    new_tpl = ((string[item], tpl[item]) for item in range(min(len(string), len(tpl))))
    return new_tpl


def dict_to_tuple(user_obj):
    new_tpl = ((key, vol) if str(key).isalpha() else (vol, key) for key, vol in user_obj.items())
    return new_tpl


user_str = 'abcde'
user_tuple = (10, 20, 30, 40, 50, 60)
# user_str = {'a': 1, 'b': 2, 'c': 3}
# user_str = {1: 'a', 2: 'b', 3: 'c'}

if isinstance(user_str, dict):
    new_tuple = dict_to_tuple(user_str)
elif isinstance(user_tuple, dict):
    new_tuple = dict_to_tuple(user_tuple)
else:
    new_tuple = zip_function(user_str, user_tuple)

print('Результат: ')
print(zip_function(user_str, user_tuple))
for idx in new_tuple:
    print(idx)
