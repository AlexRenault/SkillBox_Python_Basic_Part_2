a_list = [1, 5, 3]
b_list = [1, 5, 1, 5]
c_list = [1, 3, 1, 5, 3, 3]

a_list.extend(b_list)
print('Количество цифр "5" при первом объединении', a_list.count(5))
index = 0
while index < len(a_list):
    if a_list[index] == 5:
        a_list.remove(5)
    index += 1

a_list.extend(c_list)
print('Количество цифр "3" после второго объединения', a_list.count(3))

print(a_list)

# TODO переписать программу
