import pprint, copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def print_site(struct, string='', space=0, brand=''):
    value = ''
    if string == '':
        string = 'site = {'
        space = len(string)
        string += '\n'
    for i_key, i_value in struct.items():
        if isinstance(i_value, dict):
            temp_string = ' ' * space + "'" + i_key + "'"
            string += temp_string + ': {\n'
            string = print_site(i_value, string, len(temp_string), brand)
        else:
            value = i_value
        if value != '':
            if i_key != 'title' and i_key != 'p':
                string += ' ' * (space + 2) + "'" + i_key + "' : '" + value + "',\n"
            else:
                string += ' ' * (space + 2) + "'" + i_key + "' : '" + value + "'\n"
    string += ' ' * (space + 2) + '}\n'
    return string


def change_site(struct, key_lst, brand):
    new_site = struct
    for _ in key_lst:
        for i_key, i_volume in struct.items():
            if isinstance(i_volume, dict):
                change_site(i_volume, key_lst, brand)
            else:
                if i_key == key_lst[0]:
                    new_site[i_key] = i_volume.replace('телефон', brand)
                if i_key == key_lst[1]:
                    new_site[i_key] = i_volume.replace('iphone', brand)
                return

    return new_site


# TODO здесь писать код
site_count = int(input('Сколько сайтов? '))
site_list, product_list = [], []
key_list = ['title', 'h2']

for idx in range(site_count):
    product = input('Введите название продукта для нового сайта: ')
    product_list.append(product)
    site_list.append(change_site(copy.deepcopy(site), key_list, product))
    for i_site in range(len(site_list)):
        print('Сайт для ', product_list[i_site], ':')
        print(print_site(site_list[i_site]))
        print()

for i_site in range(len(site_list)):
    print('Сайт для ', product_list[i_site], ':')
    pprint.pprint(site_list[i_site])
    print()
