class Child:
    def __init__(self, name, age, calm_state, hunger_state):
        self.name = name
        self.age = age
        self.calm = calm_state
        self.hunger = hunger_state

    def info(self):
        print('Имя - {},\tВозраст - {},\tСостояние - {},\tАппетит - {}.'.format(
            self.name, self.age, self.calm, self.hunger
        ))
