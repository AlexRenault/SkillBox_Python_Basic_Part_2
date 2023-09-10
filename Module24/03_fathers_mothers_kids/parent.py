class Parent:

    def __init__(self, name, age, child_lst):
        self.name = name
        self.age = age
        self.children = child_lst

    def parent_info(self):
        print('\nИнформация о родителе:')
        print('Имя - {}\nВозраст - {}\nДети - {}\n'.format(
            self.name, self.age, self.children))

    def calm_child(self):
        pass

    def feed_child(self):
        pass
