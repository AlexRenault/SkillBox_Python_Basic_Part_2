# TODO здесь писать код
number_videocard = int(input('Введите количество видеокарт: '))
videocard_list = []
new_list = []

for index in range(number_videocard):
    print(index + 1, 'Видеокарта: ', end='')
    videocard = int(input())
    videocard_list.append(videocard)

max_video = max(videocard_list)

#max_video = videocard_list[0]
#for videocard in videocard_list:
#    if max_video < videocard:
#        max_video = videocard

for videocard in videocard_list:
    if max_video != videocard:
        new_list.append(videocard)

videocard_list.clear
videocard_list = new_list

print(videocard_list)


