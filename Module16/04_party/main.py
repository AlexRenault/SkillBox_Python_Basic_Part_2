guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
answer = ''

while answer != 'пора спать':
    print(f'\nСейчас на вечеринке {len(guests)} человек: ', guests)
    answer = input('Гость пришел или ушел? ')

    while answer != 'пришел' and answer != 'ушел' and answer != 'пора спать':
        print('Возможны ответы - "пришел", "ушел", "пора спать".')
        answer = input('Гость пришел или ушел? ')

    if answer == 'пришел':
        name_guest = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name_guest)
            print(f'Привет, {name_guest}!')
        else:
            print(f'Прости, {name_guest}, но мест нет.')
    elif answer == 'ушел':
        name_guest = input('Имя гостя: ')
        if name_guest in guests:
            guests.remove(name_guest)
            print(f'Пока, {name_guest}!')
        else:
            print('Гостя с таким именем нет.')
    else:
        print('\nВечеринка закончилась, все легли спать.')