# TODO здесь писать код
import functools
from typing import Callable, Any


def count(func: Callable) -> Any:
    """
        Декоратор - считает количество вызовов декорируемой функции
    """
    @functools.wraps(func)
    def wrapping_func(*args, **kwargs) -> Any:
        wrapping_func.count += 1
        func(*args, **kwargs)
    wrapping_func.count = 0
    return wrapping_func


@count
def function(number: int) -> None:
    """
    Функция - формирует и печатает список квадратов чисел от 1 до number
    :arg number [int]
    """
    my_list = [idx ** 2 for idx in range(number + 1)]
    print(my_list)


for idx in range(10):
    function(idx)
print('Функция {} была вызвана {}'.format(function.__name__, function.count))
