# TODO здесь писать код
from typing import Callable, Any
import functools
import time


def cache(func: Callable) -> Callable:
    """ Декоратор - кэширует результаты вызова функции """

    @functools.lru_cache()
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped


def cache_1(func: Callable) -> Callable:
    """ Декоратор - кэширует результаты вызова функции. Вариант 2"""
    my_dict = dict()

    # @functools.wraps(func)
    def wrapped(number, *args, **kwargs):
        if number not in my_dict:
            my_dict[number] = func(number, *args, **kwargs)
        print(my_dict)
        return my_dict[number]

    return wrapped


# @cache
@cache_1
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
start_time = time.time()
print(fibonacci(10))  # Результат будет кеширован
end_time = time.time()
print(end_time - start_time)

# Повторное вычисление числа Фибоначчи с теми же аргументами
start_time = time.time()
print(fibonacci(10))  # Результат будет взят из кеша
end_time = time.time()
print(end_time - start_time)


# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
