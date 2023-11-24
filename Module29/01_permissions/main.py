# TODO здесь писать код
from typing import Callable


def check_permission(required: str, status: list[str]) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            res = None
            try:
                if required not in status:
                    raise PermissionError
                else:
                    res = func(*args, **kwargs)
            except PermissionError:
                print('PermissionError: У пользователя {} недостаточно прав, чтобы выполнить функцию {}'.format(
                    status, func.__name__))
            return res
        return wrapper
    return decorator


user_permissions = ['user_1']


@check_permission('admin', user_permissions)
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1', user_permissions)
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
