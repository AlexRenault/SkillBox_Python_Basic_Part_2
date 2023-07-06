violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
num_songs = int(input('Сколько песен выбрать? '))
sound_time = 0
play_list = []

for i_song in range(num_songs):
    print(f'Название {i_song + 1}-й песни: ', end='')
    name_song = input()

    for song in violator_songs:
        if name_song == song[0]:
            play_list.append(song)
            sound_time += song[1]
            break
    else:
        print('Такой песни нет в списке.')

print('Ваш плейлист: ', play_list)
print('Общее время звучания песен: ', round(sound_time, 2))