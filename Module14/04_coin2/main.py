# TODO здесь писать код
import math

def distance (x, y):
    dist = math.sqrt(x ** 2 + y ** 2)
    return dist


print('Введите координаты монетки: ')
x_coordinate = float(input('X: '))
y_coordinate = float(input('Y: '))
radius = int(input('Введите радиус: '))

if distance(x_coordinate, y_coordinate) <= radius:
    print('Монетка где-то рядом.')
else:
    print('Монетки в области нет.')