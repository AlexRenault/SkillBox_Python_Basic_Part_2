# TODO здесь писать код
from typing import Callable


def singleton(cls: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        inst = cls(*args, **kwargs)
        if wrapper.inst is None:
            wrapper.instance = inst
        return wrapper.inst
    wrapper.inst = None
    return wrapper


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)