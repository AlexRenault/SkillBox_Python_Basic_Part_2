# TODO здесь писать код
from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор декораторов. Можно передавать любые аргументы.
    :param: Декоратор, которому добавляется возможность принимать аргументы
    :return: Расширенный декоратор
    """
    def wrap_decor(*args, **kwargs):
        """
        Обертка над функцией-декоратором, передающая аргументы в передающую функцию.
        :param args: Позиционные аргументы для передачи в декоратор.
        :param kwargs: Именованные аргументы для передачи в декоратор.
        :return: Обертка декоратора
        """
        def decor(func: Callable) -> Callable:
            """
            Обертка над функцией-декоратором, передает аргументы в декорируемую функцию.
            :param func: Декорируемая функция
            :return: Результат работы декорируемой функции
            """
            return decorator(func, *args, **kwargs)
        return decor
    return wrap_decor


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *d_args, **d_kwargs) -> Callable:
    """
    Декоратор-шаблон.
    :param func: Декорируемая функция
    :param d_args: Позиционные аргументы, переданные декоратору
    :param d_kwargs: Именованные аргументы, переданные декоратору
    :return: Результат работы декорируемой функции
    """
    @functools.wraps(func)
    def wrapper(*f_args, **f_kwargs):
        """
        Обертка над декорируемой функцией, выводящая переданные аргументы
        :param f_args: позиционные аргументы декорируемой функции
        :param f_kwargs: именованные аргументы декорируемой функции
        :return: Результат работы декорируемой функции
        """
        print("Переданные арги и кварги в декоратор: ", d_args, d_kwargs)
        return func(*f_args, **f_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)