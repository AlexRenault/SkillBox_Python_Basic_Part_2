# TODO здесь писать код
number = int(input('Количество человек: '))
humans = list(range(1, number + 1))

remove = int(input('Какое число в считалке? '))

remove_human = 0

while len(humans) != 1:
    print('\nТекущий круг людей: ', humans)
    index = remove_human % len(humans)
    remove_human = (index + remove - 1) % len(humans)
    print('начало отсчета с номера ', humans[index])
    print('Выбывает человек под номером ', humans[remove_human])
    humans.remove(humans[remove_human])

print('Остался человек под номером ', humans[0])