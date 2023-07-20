# TODO здесь писать код
while True:
    password = input('Придумайте пароль: ')
    upper = [1 for char in password if char.isupper()]
    digital = [1 for char in password if char.isdigit()]

    if len(password) >= 8 and len(upper) > 0 and sum(digital) >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

