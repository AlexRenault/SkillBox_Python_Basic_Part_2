# TODO здесь писать код
def read_file(file):
    players = dict()
    for count, i_line in enumerate(file):
        if count == 0:
            ball = int(i_line)
        else:
            player = i_line.split()
            if int(player[2]) > ball:
                players[player[1][0] + '. ' + player[0]] = int(player[2])
    return players


count_strings = 0
players_dict = dict()


first_file = open('first_tour.txt', 'r', encoding='utf-8')
players_dict = read_file(first_file)
first_file.close()

players_dict = sorted(players_dict.items(), reverse=True)

file_out = open('second_tour.txt', 'w')
file_out.write(str(len(players_dict)) + '\n')
for idx, player in enumerate(players_dict):
    str_player = ''.join([str(idx + 1), ') ', player[0], ' ', str(player[1]), '\n'])
    file_out.write(str_player)
file_out.close()













