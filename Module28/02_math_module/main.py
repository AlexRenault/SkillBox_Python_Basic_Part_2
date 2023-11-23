# TODO здесь писать код
import math


class MyMath:
    """
    Класс содержащий функции математических
    вычислений, связанных с фигурами.
    - вычисление длины окружности
    - вычисление площади окружности
    - вычисление объёма куба
    - вычисление площади трапеции
    - вычисление площади поверхности сферы.
    """
    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_square(cls, radius: float) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_vol(cls, edge: float) -> float:
        return edge ** 3

    @classmethod
    def trapezoid_square(cls, base_1: float, base_2: float, height: float) -> float:
        return (base_1 + base_2) / 2 * height

    @classmethod
    def sphere_square(cls, radius: float) -> float:
        return 4 * math.pi * radius ** 2


result = MyMath.circle_len(15)
print(result)
result = MyMath.circle_square(15)
print(result)
result = MyMath.trapezoid_square(15, 10, 2)
print(result)
result = MyMath.sphere_square(15)
print(result)
result = MyMath.cube_vol(15)
print(result)



