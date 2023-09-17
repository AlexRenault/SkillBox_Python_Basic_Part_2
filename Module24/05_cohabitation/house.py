from random import randint
class House:
    def __init__(self, meal, money):
        self.meal = meal
        self.money = money

    def house_info(self):
        print('Еды в холодильнике - {}, денег в тумбочке - {}\n'.format(
            self.meal, self.money))

    def meal_add(self):
        self.meal += randint(5, 30)

    def money_add(self):
        self.money += randint(5, 30)

    def meal_use(self):
        self.meal -= randint(5, 30)

    def money_use(self):
        self.money -= randint(5, 30)

    def check_meal(self):
        if self.meal < 10:
            return True
        else:
            return False

    def check_money(self):
        if self.money < 50:
            return True
        else:
            return False
