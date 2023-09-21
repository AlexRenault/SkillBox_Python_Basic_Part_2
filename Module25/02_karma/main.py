# TODO здесь писать код
from random import randint, choice


class KillError(Exception):
    def __str__(self):
        return 'Грех убийства. Карма уменьшается на -'


class DrunkError(Exception):
    def __str__(self):
        return 'Грех пьянства. Карма уменьшается на -'


class CarCrashError(Exception):
    def __str__(self):
        return 'Автомобильная авария. Карма уменьшается на -'


class GluttonyError(Exception):
    def __str__(self):
        return 'Грех обжорства. Карма уменьшается на -'


class DepressError(Exception):
    def __str__(self):
        return 'Депрессия. Карма уменьшается на -'


def one_day(lst):
    karma = randint(1, 7)
    if choice(range(1, 10)) == 1:
        excep = choice(lst)
    else:
        excep = False
    return karma, excep


class_lst = [KillError, DrunkError, CarCrashError, GluttonyError, DepressError]

karma_max = 500
current_karma = 0
days = 1

with open('karma.log', 'w', encoding='utf-8') as save_file:
    while True:
        print('День - ', days)
        try:
            day_karma, excep_random = one_day(class_lst)
            current_karma += day_karma
            if excep_random:
                raise excep_random
        except excep_random as err:
            dec = choice(range(5, 10))
            info = ' '.join((str(err), str(dec), '\n'))
            print(info)
            save_file.write(info)
            current_karma -= dec

        if current_karma >= karma_max:
            print('Вы достигли просветления.')
            break
        print('Накоплено кармы - ', current_karma)
        days += 1
        print()
