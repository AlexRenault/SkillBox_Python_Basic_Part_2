from random import choice


class Warrior:
    def __init__(self, name):
        self.name = '-'.join(['Воин', name])
        self.health = 100

    def info(self):
        print('{} ------> здоровье {}'.format(
            self.name, self.health)
        )

    def damage(self):
        self.health -= 20
        print(self.name, ' - здоровье: ', self.health)

    def death(self):
        if self.health == 0:
            print('\n{} - погиб. Бой окончен.'.format(self.name))
            return True
        else:
            return False


class Battle:

    def __init__(self, count):
        self.warriors = [Warrior(str(idx)) for idx in range(count)]

    def attack(self):
        attack_warrior = choice(self.warriors)
        print('\nАтакует ', attack_warrior.name)
        for warrior in self.warriors:
            if warrior != attack_warrior:
                warrior.damage()

    def print_info(self):
        print('INFO:')
        for warrior in self.warriors:
            warrior.info()

    def end(self):
        for warrior in self.warriors:
            if warrior.death():
                return False
        else:
            return True
