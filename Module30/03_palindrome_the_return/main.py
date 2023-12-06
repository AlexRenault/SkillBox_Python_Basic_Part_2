# TODO здесь писать код
import collections


def can_be_poly(string: str) -> bool:
    count = collections.Counter(string)
    odd = len(list(filter(lambda x: x % 2 != 0, list(count.values()))))
    if (len(string) % 2 == 0 and odd == 0) or (len(string) % 2 != 0 and odd == 1):
        return True
    else:
        return False


print('abcba - ', can_be_poly('abcba'))
print('abbbc - ', can_be_poly('abbbc'))
