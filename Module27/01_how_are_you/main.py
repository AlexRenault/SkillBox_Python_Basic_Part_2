# TODO здесь писать код
from typing import Callable, Any


def how_are_you(func) -> Any:
    """ Функция декоратор."""
    def wrapped_func(*args, **kwargs) -> Any:
        input('Как твои дела? ')
        print('А у меня не очень.')
        return func
    return wrapped_func()


@how_are_you
def test():
    print('Это была шутка.')


test()
