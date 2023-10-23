import random


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нет кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить
        # выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    def __init__(self, name):
        super().__init__(name)
        self.magic_power = self.get_power() * 3

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

    # Методы:

    def attack(self, target):
        # - атака - может атаковать врага, но атакует только в половину силы self.__power
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
        self.set_hp(self.get_hp() - damage * 1.2)
        super().take_damage(damage)

    def healing(self, friend):
        # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
        friend.set_hp(friend.get_hp() + self.magic_power)

    def make_a_move(self, friends, enemies):
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из
        # действий (атака, исцеление) на выбранную им цель

        # Поиск героя с минимальным HP
        target_of_hp = friends[0]
        min_health = target_of_hp.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_hp = friend
                min_health = target_of_hp.get_hp()
        # Исцеление героя с минимальным значением HP
        # Если HP меньше или равно 100 и есть магическая сила, то к HP героя добавляем магическую силу
        if min_health <= 100 and self.magic_power > 0:
            print(self.name, "- исцеляю - ", target_of_hp.name)
            self.healing(target_of_hp)
        else:
            # Если монстров нет, то возвращаемся не атакуя
            if not enemies:
                return
            # Атакуем слабейшего монстра
            target_attack = attack_min_hp(self.name, enemies)
            self.attack(target_attack)
            super().make_a_move(friends, enemies)
            print('\n')


class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.shield = False

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

    # Методы:

    def attack(self, target):
        # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом
        # отнимается от здоровья
        damage /= self.defense
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def shield_up(self):
        # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает
        # показатель силы в 2 раза.
        if not self.shield:
            self.shield = True
            self.defense *= 2
            self.set_power(self.get_power() / 2)

    def shield_down(self):
        # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает
        # показатель силы в 2 раза.
        if self.shield:
            self.shield = False
            self.defense /= 2
            self.set_power(self.get_power() * 2)

    def make_a_move(self, friends, enemies):
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из
        # действий (атака, поднять щит/опустить щит) на выбранную им цель
        # Если НР уменьшилось до 50% - поднимаем щит
        if self.get_hp() <= 75 and not self.shield:
            print('Здоровья осталось меньше 50%. Поднимаю щит.')
            self.shield_up()
            return
        # Если НР больше 50% - опускаем щит.
        if self.get_hp() > 75 and self.shield:
            print('здоровье достаточно. Опускаю щит.')
            self.shield_down()
            return
        # Если монстров нет, то возвращаемся не атакуя
        if not enemies:
            return
        # Атакуем слабейшего монстра
        target_attack = attack_min_hp(self.name, enemies)
        self.attack(target_attack)
        super().make_a_move(friends, enemies)


class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 2

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

    # Методы:

    def attack(self, target):
        # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона
        # (self.power_multiply)
        # после нанесения урона - вызывается метод ослабления power_down.
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_multiply = self.power_down()
    def take_damage(self, damage):
        # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления
        # урона - damage * (self.power_multiply / 2)
        self.set_hp(self.get_hp() - damage * (self.power_multiply / 2))

    def power_up(self):
        # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
        return self.power_multiply * 2

    def power_down(self):
        # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
        return self.power_multiply / 2

    def make_a_move(self, friends, enemies):
        print('{} - HP:{}, множитель:{} '.format(
            self.name, self.get_hp(), self.power_multiply)
        )
        # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет
        # ОДНО из действий (атака, усиление, ослабление) на выбранную им цель
        # Если коэффициент усиления урона меньше 2 - увеличиваем его в 2 раза
        if self.power_multiply < 2:
            self.power_multiply = self.power_up()
            print('Увеличиваю силу до - ', self.power_multiply)
        # Если коэффициент усиления урона больше 10 - уменьшаем
        elif self.power_multiply > 6:
            self.power_multiply = self.power_down()
            print('Уменьшаю силу до - ', self.power_multiply)
        else:
            # Если монстров нет, то возвращаемся не атакуя
            if not enemies:
                return
            # Атакуем слабейшего монстра
            target_attack = attack_min_hp(self.name, enemies)
            self.attack(target_attack)
            print('После атаки: {} - HP:{}, множитель:{} '.format(
                self.name, self.get_hp(), self.power_multiply)
            )
            super().make_a_move(friends, enemies)


def attack_min_hp(name, enemies):
    # выбор слабейшего монстра для атаки
    idx = 0
    # За слабейшего монстра берем первого в списке
    min_hp_enemy = enemies[0].get_hp()
    target_attack = enemies[0]
    # Проверка НР монстров на равенство 0. Если 0, то не атакуем,
    for idx, enemy in enumerate(enemies):
        # Ищем по списку монстра, НР которого не равно 0, выбираем его как монстра с наименьшим НР
        if enemy.is_alive():
            min_hp_enemy = enemy.get_hp()
            target_attack = enemy
            break
    # Начиная с выбранного монстра, в списке монстров ищем наименьшее значение НР и
    # выбираем этого монстра как цель для атаки
    for i_enemy in range(idx, len(enemies) - 1):
        if enemies[i_enemy].get_hp() < min_hp_enemy:
            min_hp_enemy = enemies[i_enemy].get_hp()
            target_attack = enemies[i_enemy]
    print(name, ' - атакую - ', target_attack.name)
    return target_attack
