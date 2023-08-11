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
            if i_key == 'title':
                value = value.replace('телефон', brand)
            elif i_key == 'h2':
                value = value.replace('iphone', brand)
        if value != '':
            if i_key != 'title' and i_key != 'p':
                string += ' ' * (space + 2) + "'" + i_key + "' : '" + value + "',\n"
            else:
                string += ' ' * (space + 2) + "'" + i_key + "' : '" + value + "'\n"
    string += ' ' * (space + 2) + '}\n'
    return string


# TODO здесь писать код
site_count = int(input('Сколько сайтов? '))

for _ in range(site_count):
    product = input('Введите название продукта для нового сайта: ')
    print('Сайт для ', product, ':')
    site_string = print_site(site, brand=product)
    print(site_string)
