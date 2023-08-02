def user_action():
    print('\nВыберите номер действия: ')
    print('1. Добавить контакт.')
    print('2. Найти человека.')
    print('3. Выход.')
    act = ''
    while act not in ('1', '2', '3'):
        act = input('Ваш выбор: ')
    return int(act)


def add_contact(cont):
    subscriber = ''
    while subscriber == '' or subscriber.count(' ') < 1 or len(subscriber) < 3:
        subscriber = input('\nВведите Имя и Фамилию нового контакта (через пробел): ')
    human = list(subscriber.split())
    human[0] = human[0].title()
    human[1] = human[1].title()
    human = tuple(human)
    if human not in cont:
        phone = ''
        while not phone.isdigit():
            phone = input('Введите номер телефона: ')
        cont[human] = int(phone)
    else:
        print('Такой человек уже есть в контактах.')
    return cont


def find_contact(cont):
    flag = False
    surname = input('\nВведите фамилию для поиска: ').lower()
    for subscriber, phone in cont.items():
        subscriber_list = list(subscriber)
        subscriber_list[1] = subscriber_list[1].lower()
        if surname in subscriber_list:
            print(subscriber[0], surname.title(), phone, end='\n')
            subscriber_list = []
            flag = True
    if not flag:
        print('Такого человека нет в Ваших контактах.')


# TODO здесь писать код
contact = dict()

action = 0
while True:
    action = user_action()
    if action == 1:
        contact = add_contact(contact)
    elif action == 2:
        find_contact(contact)
    else:
        break

    print('\nТекущий словарь контактов:\n', contact)
