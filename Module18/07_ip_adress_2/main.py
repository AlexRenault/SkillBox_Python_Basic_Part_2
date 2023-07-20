# TODO здесь писать код
while True:
    ip_input = input('Введите IP: ')
    ip = ip_input.split('.')

    err = ''
    if len(ip) != 4:
        err = 'Ошибка. IP адрес должен состоять из 4 целых чисел от 0 до 255, ' \
              'разделенных точками (например - 192.168.1.12).'
    else:
        for item_ip in ip:
            if not item_ip.isdigit():
                err = ''.join([item_ip, ' — это не целое число.'])
            elif int(item_ip) < 0:
                err = 'Ошибка. IP адрес - состоит из целых чисел от 0 до 255.'
            elif int(item_ip) > 255:
                    err = ''.join(['Ошибка. ', item_ip, ' > 255.'])

    if err == '':
        print('IP-адрес корректен.')
        break
    else:
        print(''.join([err, 'Попробуйте еще раз.']))
        print()