# TODO здесь писать код
import math
# Здесь создайте функцию get_sage_sqrt


def get_sage_sqrt(num):
    res = None
    try:
        if not isinstance(num, (int, float)):
            raise TypeError
        elif num < 0:
            raise ValueError
        elif isinstance(num, (int, float)):
            res = math.sqrt(num)
        else:
            raise Exception
    except ValueError:
        print(f'SQRT({num}) - Передано отрицательное число')
    except TypeError:
        print(f'SQRT({num}) - Не соответствие типов. Попытка вычислить квадратный корень из None или строки.')
    except Exception as err:
        print(f'SQRT({num}). Ошибка.', err, type(err))
    finally:
        return res


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc", None, '']
for number in numbers:
    result = get_sage_sqrt(number)
    if result:
        print(f"Квадратный корень {number}: {result}")
