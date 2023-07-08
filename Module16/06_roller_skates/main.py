# TODO здесь писать код
skate_size = []
foot_size = []
user_list = []

num_skate = int(input('Количество коньков: '))
for i_skate in range(num_skate):
    skate_size.append(int(input(f'Размер {i_skate + 1}-й пары: ')))

num_human = int(input('\nКоличество людей: '))
for i_human in range(num_human):
    foot_size.append(int(input(f'Размер ноги {i_human + 1}-го человека: ')))

for i_human in foot_size:
    i_skate = 0
    while i_skate < len(skate_size):
        if i_human == skate_size[i_skate]:
            user_list.append(i_human)
            skate_size.remove(skate_size[i_skate])
        i_skate += 1

print('Наибольшее количество людей, которые могут взять ролики: ', len(user_list))



