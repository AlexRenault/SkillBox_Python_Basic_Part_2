# TODO здесь писать код
class Property:
    def __init__(self, worth):
        self.worth = self.verify(worth)
        self.title = ''
        self.tax_obj = self.tax()

    def verify(self, number):
        while not isinstance(number, (int, float)):
            print('Стоимость не корректна.')
            number = float(input(f'Введите стоимость объекта {self.title}: '))
        return number

    def tax(self):
        return self.worth / 1

    def __str__(self):
        return '. Стоимость объекта {} - {}, налог {}'.format(self.title, self.worth, self.tax())


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.title = 'Квартира'
        self.tax_obj = self.tax()

    def tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.title = 'Машина'
        self.tax_obj = self.tax()

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.title = 'Дача'
        self.tax_obj = self.tax()

    def tax(self):
        return self.worth / 500


def verify(message):
    money = 0
    while money == 0 or not isinstance(money, (int, float)):
        try:
            money = float(input(message))
        except (TypeError, ValueError) as err:
            print('Не корректный ввод. ', err)
    return money


obj_title = ['Квартира', 'Машина', 'Дача']
name_obj = [Apartment, Car, CountryHouse]
objects = []

string = 'Какой суммой Вы располагаете: '
user_money = verify(string)

for idx, i_obj in enumerate(name_obj):
    string = f'Введите стоимость объекта {obj_title[idx]}: '
    cost = verify(string)
    objects.append(i_obj(cost))
    print(f'Налог на {obj_title[idx]} - {objects[idx].tax_obj}Р')
    user_money -= objects[idx].tax_obj
    if user_money < 0:
        print('Не хватает {}Р'.format(-user_money))
    else:
        print(f'После уплаты этого налога осталось - {user_money}Р\n')

for i_obj in objects:
    print(i_obj)
