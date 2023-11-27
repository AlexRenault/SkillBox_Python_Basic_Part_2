# TODO здесь писать код
from typing import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """ Декоратор декораторов. Можно передавать любые аргументы."""
    def wrap_decor(*args, **kwargs):
        def decor(func: Callable) -> Callable:
            print("Переданные арги и кварги в декоратор: ", *args, **kwargs)
            return func
        return decor
    return wrap_decor


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)