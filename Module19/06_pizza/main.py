# TODO здесь писать код

num_orders = int(input('Введите количество заказов: '))

#order = [
#    'Иванов Пепперони 1', 'Петров Де-Люкс 2', 'Иванов Мясная 3',
#    'Иванов Мексиканская 2', 'Иванов Пепперони 2', 'Петров Интересная 5',
#    'Сидоров Маргарита 4', 'Сидоров Сырная 1'
#]
#num_orders = 8
orders = []
orders_dict = {}

print('Информацию о заказе вводите через пробел - Фамилия Название_пиццы Количество')

for i_order in range(num_orders):
    order, pizza, count = input(f'Введите {i_order + 1} заказ: ').split()

    if order not in orders_dict:
        orders_dict[order] = {pizza: int(count)}
    else:
        if pizza not in orders_dict[order]:
            orders_dict[order].update({pizza: int(count)})
        else:
            orders_dict[order][pizza] += int(count)

sorted(orders_dict)
for surname in orders_dict:
    #pizza_list = sorted((value, key) for (key, value) in orders_dict[surname].items())
    #pizza_sorted = dict([(key, value) for value, key in pizza_list])
    #orders_dict[surname] = pizza_sorted
    print(surname, ':')
    for order in orders_dict[surname]:
        print('\t\t', order, orders_dict[surname][order])

for surname in orders_dict.keys():
    print(f'{surname} :')
    for pizza in orders_dict[surname].keys():
        print('\t\t{}: {}'.format(pizza, orders_dict[surname][pizza]))

