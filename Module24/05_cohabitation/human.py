from house import House
from random import randint


class Human:
    def __init__(self, name, satiety, home):
        self.name = name
        self. satiety = satiety
        self.home = home

    def human_info(self):
        print(f'{self.name}: сытость - {self.satiety}')

    def eat(self):
        self.satiety += randint(5, 50)
        self.home.meal_use()
        print(f'{self.name} поел.')

    def work(self):
        self.satiety -= randint(5, 50)
        self.home.money_add()
        print(f'{self.name} работал.')

    def play(self):
        self.satiety -= randint(5, 50)
        print(f'{self.name} играл.')

    def shop(self):
        self.home.meal += randint(5,50)
        self.home.money_use()
        print(f'{self.name} ходил в магазин.')

    def check_death(self):
        if self.satiety < 0:
            return True
        else:
            return False

    def action(self, number):
        if self.satiety < 20:
            self.eat()
        elif self.home.check_meal():
            self.shop()
        elif self.home.check_money():
            self.work()
        elif number == 1:
            self.work()
        elif number == 2:
            self.eat()
        else:
            self.play()
        self.human_info()
        self.home.house_info()