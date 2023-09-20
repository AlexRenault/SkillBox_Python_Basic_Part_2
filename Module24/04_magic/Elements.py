class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return 'Вода'


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        else:
            return 'Воздух'


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        if isinstance(other, Air):
            return Dust()
        if isinstance(other, Fire):
            return Lava()
        else:
            return 'Земля'

class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        if isinstance(other, Water):
            return Steam()
        if isinstance(other, Air):
            return Lightning()
        else:
            return 'Огонь'


class Storm:
    def __str__(self):
        return 'Шторм'



class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'
