# TODO здесь писать код
import datetime
import os
from typing import Callable, Any
from collections.abc import Generator


def logging(func) -> Any:
    """
        Декоратор - выводит информацию о декорируемой функции (имя, документацию)
        Если во время выполнения декорируемой функции происходит ошибка, то
        производится запись этой ошибки в файл
    """

    def wrapping_func(*args, **kwargs) -> Any:
        print('\nФункция {name}'.format(name=func.__name__))
        print(func.__doc__)
        try:
            return func(*args, **kwargs)
        except Exception as err:
            data_time = str(datetime.datetime.now())
            err_str = ''.join(['Ошибка:\n', 'Функция: ', func.__name__, '\nДата, время:', data_time,
                               '\nТип ошибки: ', str(type(err)), ' Ошибка: ',
                               str(err), '\n' * 2])
            print(err_str)
            with open('function_errors.log', 'a', encoding='utf-8') as err_file:
                err_file.write(err_str)

    return wrapping_func


@logging
def func_1(number):
    """
    Функция 1. формирует список квадратов чисел от 1 до number
    :arg number [int]
    """
    my_list = [idx ** 2 for idx in range(1, number + 1)]
    print(my_list)


@logging
def func_2(number: int) -> None:
    """
        Функция 2. формирует список чисел от 0 до number
        :arg number [int]
    """
    my_list = [idx for idx in range(number + 1)]
    print(my_list)


@logging
def func_3(num_1: int, num_2: int) -> float:
    """
    Функция деления числа num_1 на число num_2
    :param num_1: int
    :param num_2: int
    :return res: float
    """
    return num_1 / num_2

func_1('10')
func_2(10)
func_3(10,4)
func_3(15, 0)
