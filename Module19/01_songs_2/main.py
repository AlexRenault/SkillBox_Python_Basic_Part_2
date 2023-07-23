violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код
count_song = int(input('Сколько песен выбрать? '))
songs_time = 0

for i_song in range(count_song):
    print('Название {} песни: '.format(i_song + 1), end='')
    song = input()
    if song in violator_songs.keys():
        songs_time += violator_songs[song]
    else:
        print('Извините. Песни {} в нашем списке нет.'.format(song))

print('Общее время звучания песен: ', round(songs_time, 2))