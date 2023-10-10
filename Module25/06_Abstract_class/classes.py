import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def check(num):
        while num <= 0:
            if num > 0:
                return num
            else:
                raise ValueError(f'Введено не корректное значение: {num}.')

    def __init__(self, num_1=None, num_2=None):
        self.set_number_1(num_1)
        if num_2 is not None:
            self.set_number_2(num_2)

    def set_number_1(self, num_1):
        return self.check(num_1)

    def set_number_2(self, num_2):
        return self.check(num_2)



class Circle(Shape):

    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, side_1, side_2):
        super().__init__(side_1, side_2)
        self.side_1 = side_1
        self.side_2 = side_2

    def area(self):
        return (self.side_1 * self.side_2) / 2
