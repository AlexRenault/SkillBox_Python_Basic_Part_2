# TODO здесь писать код
import random

number = int(input('Введите количество участников в командах: '))

first_team = [round(random.triangular(5, 10), 2) for _ in range(number)]
second_team = [round(random.triangular(5, 10), 2) for _ in range(number)]

print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)

winner = [first_team[index] if first_team[index] > second_team[index] else second_team[index]
          for index in range(number)]

print('Победители тура: ', winner)