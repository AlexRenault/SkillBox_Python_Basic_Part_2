# TODO здесь писать код
import time
from typing import Callable
import functools


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func
        self.start = time.time()

    def __call__(self, *args, **kwargs):
        print('Вызов функции {}'.format(self.func.__name__))
        print('Аргументы - ', *args, **kwargs)
        print('Результат - ', self.func(*args, **kwargs))
        time_exec = time.time() - self.start
        print('время выполнения - ', time_exec)
        return self.func(*args, **kwargs)


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            result += i + j
    with open('test.txt', 'w', encoding='utf8') as file:
        file.write(str(i + j))
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)