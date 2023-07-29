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
    order = input(f'Введите {i_order + 1} заказ: ')
    orders.append(order.split())
    orders[i_order][2] = int(orders[i_order][2])
    pizza = dict()
    pizza[orders[i_order][1]] = orders[i_order][2]
    if orders[i_order][0] not in orders_dict.keys():
        orders_dict[orders[i_order][0]] = pizza
    else:
        if orders[i_order][1] != orders_dict.get(orders[i_order][0]):
            orders_dict[orders[i_order][0]].update(pizza)
        else:
            orders_dict[orders[i_order][0]][orders[i_order][1]] += orders_dict[orders[i_order]][0][orders[i_order][1]]

sorted(orders_dict)
for surname in orders_dict:

    pizza_list = sorted((value, key) for (key, value) in orders_dict[surname].items())
    pizza_sorted = dict([(key, value) for value, key in pizza_list])
    orders_dict[surname] = pizza_sorted
    print(surname, ':')
    for order in orders_dict[surname]:
        print('\t\t', order, orders_dict[surname][order])

