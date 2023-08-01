# TODO здесь писать код
import random


def metod_1(user_list):
    new_list = [(user_list[idx], user_list[idx + 1]) for idx in range(0, len(user_list) - 1, 2)]
    print('Новый список: ', new_list)


def metod_2(user_list):
    new_list = [tuple(user_list[idx: idx + 2]) for idx in range(0, len(user_list) - 1, 2)]
    print('Новый список: ', new_list)


def metod_3(user_list):
    new_list = list(zip(user_list[::2], user_list[1::2]))
    print('Новый список: ', new_list)


original_list = [random.randint(0, 100) for idx in range(10)]

print('Оригинальный список: ', original_list)

metod_1(original_list)

metod_2(original_list)

metod_3(original_list)
