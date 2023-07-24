# TODO здесь писать код
def create_dict(txt):
    txt_dict = dict()
    for symbol in txt:
        if symbol in txt_dict:
            txt_dict[symbol] += 1
        else:
            txt_dict[symbol] = 1
    return txt_dict


def revers_dict(txt_dict):
    rev_dict = dict()
    for value in txt_dict.values():
        rev_dict[value] = [txt_dict_key for txt_dict_key in txt_dict.keys() if value == txt_dict[txt_dict_key]]
    return rev_dict


text = input('Введите текст: ')

text_dict = create_dict(text)

reverse_dict = revers_dict(text_dict)

for item in sorted(reverse_dict.keys()):
    print(item, ':', reverse_dict[item])
