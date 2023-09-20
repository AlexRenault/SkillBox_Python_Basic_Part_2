from child import Child
import random


class Parent:
    def __init__(self, parent_lst, parent_age, children_lst):
        self.parent_name = random.choice(parent_lst)
        self.age = random.choice(parent_age)
        children_name = random.choices(children_lst, k=random.randint(1, 3))
        self.children = [Child(
            child, random.randint(1, (self.age - 16)), random.choice(['Возбужден', 'Спокоен']),
            random.choice(['Голоден', 'Сыт']))
            for child in children_name]

    def parent_info(self):
        print('\nИнформация о родителе:')
        print('Имя - {},\tВозраст - {}'.format(
            self.parent_name, self.age))
        print('Дети:')
        for child in self.children:
            child.info()

    def calm_hunger(self):
        for child in self.children:
            if child.calm == 'Возбужден':
                child.calm = 'Спокоен'
            if child.hunger == 'Голоден':
                child.hunger = 'Сыт'
