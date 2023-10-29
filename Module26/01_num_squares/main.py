# TODO здесь писать код
from collections.abc import Iterable


class SquaresIter:
    """Генерация с помощью класса-итератора """

    def __init__(self, num: int) -> None:
        """
        :arg
            num - число, до которого включительно вычисляются квадраты чисел
        :param
            self.cur - текущее число, возводимое в квадрат
            self.stop - определяет окончание вычислений
        """
        self.curr = 1
        self.stop = num

    def __iter__(self) -> Iterable[int]:
        """возвращает итератор объекта"""
        return self

    def __next__(self) -> int:
        """Вычисляет и возвращает следующее значение итератора"""
        if self.curr <= self.stop:
            self.curr += 1
            return (self.curr - 1) ** 2
        else:
            """Если текущее число превышает заданное пользователем - вызывается исключение StopIteration"""
            raise StopIteration


def squares_def(count: int) -> int:
    """Генерация с помощью функции-генератора """
    for idx in range(1, count + 1):
        yield idx ** 2


def print_result(num: int, number: int) -> None:
    """Функция печати результата"""
    if num < number ** 2:
        print(num, end='; ')
    else:
        print(num)


number = int(input('Введите целое число N:'))

"""Генерация с помощью генераторного выражения"""
print('Генерация с помощью генераторного выражения')
squares_nums = (idx ** 2 for idx in range(1, number + 1))
for num in squares_nums:
    print_result(num, number)

print('\nГенерация с помощью класса-итератора')
"""Генерация с помощью класса-итератора """
squares_nums = SquaresIter(number)
for num in squares_nums:
    print_result(num, number)

print('\nГенерация с помощью функции-генератора ')

"""Генерация с помощью функции-генератора """
squares_nums = squares_def(number)
for num in squares_nums:
    print_result(num, number)