goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
cost = {}

for goods_key in goods.keys():
    if goods[goods_key] in store.keys():
        summ_cost, num_goods = 0, 0
        for i_goods in range(len(store[goods[goods_key]])):
            summ_cost += store[goods[goods_key]][i_goods]['quantity'] * store[goods[goods_key]][i_goods]['price']
            num_goods += store[goods[goods_key]][i_goods]['quantity']
            cost[goods_key] = [num_goods, summ_cost]

for item in cost.keys():
    cost_item = '{:,}'.format(cost[item][1]).replace(',', ' ')
    print('{} -  {} штук, стоимость {} рублей.'.format(item, cost[item][0], cost_item))