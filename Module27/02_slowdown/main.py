# TODO здесь писать код
import time
from typing import Callable, Any


def slowdown(func) -> Callable:
    """Декоратор, замедляющий декорируемую функцию."""
    def wrapped_func(*args, **kwargs) -> Callable:
        """ Вариант задержки с помощью разницы времени страта и текущего времени"""
        # start_time = time.time()
        # while time.time() - start_time <= 2:
        #    pass
        # print('Время задержки - {} сек'.format(round(time.time() - start_time)))
        """ Вариант задержки с помощью метода sleep()"""
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapped_func


@slowdown
def my_func(number: int) -> list:
    my_list = [idx for idx in range(number + 1)]
    return my_list


print(my_func(10))
