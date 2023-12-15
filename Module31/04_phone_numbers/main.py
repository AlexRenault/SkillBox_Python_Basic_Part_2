# TODO здесь писать код
import re


phone_list = ['9999999999', '999999-999', '99999x9999', '8123456789']
pattern = r'\b[89]\d{9}\b'

for idx, phone in enumerate(phone_list):
    print(idx + 1, f'номер {phone}', end=': ')
    if re.match(pattern, phone):
        print('все в порядке.')
    else:
        print('не подходит.')
