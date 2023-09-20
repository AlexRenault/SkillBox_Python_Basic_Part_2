# TODO здесь писать код
from matrix_class import Matrix

# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
m1.print()

print("Матрица 2:")
m2.print()

print("Сложение матриц:")
m1.add(m2).print()


print("Вычитание матриц:")
m1.subtract(m2).print()

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]
print('Матрица 3:')
m3.print()

print("Умножение матриц:")
m1.multiply(m3).print()

print("Транспонирование матрицы 1:")
m1.transpose().print()