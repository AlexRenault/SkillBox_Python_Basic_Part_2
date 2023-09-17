# TODO здесь писать код
from random import randint
from house import House
from human import Human

names = ['Иван', 'Борис']
home = House(50, 0)
residents = [Human(names[idx], 50, home) for idx in range(2)]

day = 0
while day < 365:
    day += 1
    print(f'День - {day}')
    for human in residents:
        cube = randint(1, 6)
        print('На кубике выпало - ', cube)
        human.action(cube)
        if human.check_death():
            print(f'{human.name} - умер от голода.')
            residents.remove(human)
            if len(residents) == 0:
                day = 366
            else:
                break

