# TODO здесь писать код
players_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []

#Для ввода списка с клавиатуры:
#players_list = []

#players = int(input('Введите количество игроков: '))

#for i_player in range(players):
#    name = input('Введите имя ', i_player, 'игрока :')
#    players_list.append(name)

for i_player in range(0, len(players_list), 2):
        first_day.append(players_list[i_player])

print('Первый день: ', first_day)
