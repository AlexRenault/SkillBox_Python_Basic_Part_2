# TODO здесь писать код
num_containers = int(input('Введите количество контейнеров: '))
containers = []

for i_cont in range(num_containers):
    print('Введите вес', i_cont + 1, ' контейнера: ', end='')
    weigth = int(input())
    while (weigth > 200) or (weigth <= 0):
        print('Ошибка! Вес контейнера должен быть больше 0 и меньше 200 кг. Повторите ввод.')
        print('Введите вес', i_cont + 1, ' контейнера: ', end='')
        weigth = int(input())
    containers.append(weigth)

new_cont = int(input('\nВведите вес нового контейнера: '))
while (new_cont > 200) or (new_cont <= 0):
    print('Ошибка! Вес контейнера должен быть больше 0 и меньше 200 кг. Повторите ввод.')
    new_cont = int(input('\nВведите вес нового контейнера: '))

count = len((containers))
index = -1
while (abs(index) <= len(containers)) and (new_cont > containers[index]):
    count -= 1
    index -= 1

if abs(index) <= len(containers):
    print('\nНомер, который получит новый контейнер: ', count + 1)
else:
    print('\nКонтейнер получит номер 1, т.к. он самый тяжелый.')

