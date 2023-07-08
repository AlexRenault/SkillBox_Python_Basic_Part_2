# TODO здесь писать код
klass_1 = list(range(160, 178, 2))
klass_2 = list(range(162, 183, 3))
klass = []

print('Класс 1: ', klass_1)
print('Класс 2: ', klass_2)

klass.extend(klass_1)
klass.extend(klass_2)

klass.sort()

print('\nОтсортированный список учеников: ', klass)