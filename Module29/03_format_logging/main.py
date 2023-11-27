# TODO здесь писать код
import datetime
from typing import Callable
import time
import functools


def log_methods(date_format: str) -> Callable:
    def decorator(cls: Callable) -> Callable:
        @functools.wraps(cls)
        def wrapper(*args, **kwargs) -> Callable:
            start = time.time()
            start_time = datetime.datetime.now().strftime(date_format)
            res = cls(*args, **kwargs)
            print('Класс - {}, функция - {}'.format(args[0].__class__.__name__, cls.__name__))
            print('Выполнено за {}, Запущено - {}'.format(time.time() - start, start_time))
            return res
        return wrapper
    return decorator


def for_all_methods(decorator: Callable) -> Callable:
    """
    Декоратор класса.
    Получает другой декоратор и применяет его ко всем методам класса
    """
    @functools.wraps(decorator)
    def decorate(cls):
        for method_name in dir(cls):
            if not method_name.startswith("__"):
                cur_method = getattr(cls, method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, method_name, decorated_method)
        return cls
    return decorate


@for_all_methods(log_methods("%b %d %Y - %H:%M:%S"))
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@for_all_methods(log_methods("%b %d %Y - %H:%M:%S"))
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
