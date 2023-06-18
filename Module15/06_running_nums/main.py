# TODO здесь писать код
elements_list = [1, 2, 3, 4, 5, 6]

shift = int(input('Сдвиг: '))
while shift > len(elements_list):
    print('В списке всего ', len(elements_list), 'элементов.')
    shift = int(input('Задайте величину сдвига, меньше длины списка: '))

print('Изначальный список: ', elements_list)

for i_shift in range(shift, 0, -1):
    shift_element = elements_list[len(elements_list) - 1]
    for index in range(len(elements_list) - 1, - 1, -1):
        elements_list[index] = elements_list[index - 1]
    elements_list[0] = shift_element

print('Сдвинутый список: ', elements_list)

