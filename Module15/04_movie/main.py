films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
count = int(input('Сколько фильмов хотите добавить? '))
favourites = []

for index in range(count):
    film_favour = input('Введите название фильма: ')
    i_film = 0
    while (i_film != len(films) and (films[i_film] != film_favour)):
        i_film += 1
    if i_film >= len(films):
        print('Ошибка: фильма', film_favour, 'у нас нет :(')
    else:
        favourites.append(film_favour)

print('Ваш список любимых фильмов: ', end='')
for i_film in range(len(favourites) - 1):
    print(favourites[i_film] + ', ', end='')
if len(favourites) == 0:
    print('Ваш список любимых фильмов пуст.')
else:
    print(favourites[len(favourites) - 1])

