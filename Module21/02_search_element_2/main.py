# TODO здесь писать код
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find(struct, key):
    if key in struct:
        return struct[key]
    else:
        for sub in struct.values():
            if isinstance(sub, dict):
                res = find(sub, key)
                if res:
                    break
        else:
            res = None
    return res


def find_vol(structure, key, dpt=None):
    res = None
    if dpt is None or dpt >= 1:
        if key in structure:
            return structure[key]
    for sub in structure.values():
        if isinstance(sub, dict):
            res = find_vol(sub, key, dpt - 1)
            if res:
                break

    return res


find_key = input('Введите искомый ключ: ')

user_answer = ''
item = None
while user_answer not in ('y', 'n'):
    user_answer = input('Хотите ввести максимальную глубину? Y/N ').lower()
    if user_answer == 'y':
        depth = 0
        while depth <= 0:
            depth = int(input('Введите максимальную глубину > 0: '))
        item = find_vol(site, find_key, depth)
    else:
        item = find(site, find_key)

print('Значение ключа: ', item)
