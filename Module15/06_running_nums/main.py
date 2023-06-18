# TODO здесь писать код
elements_list = []
number = int(input('Введите количество элементов списка: '))
for index in range(number):
    print('Введите ', index + 1, 'элемент списка (целые числа):', end='')
    element = int(input())
    elements_list.append(element)

shift = int(input('Сдвиг: '))

print('Изначальный список: ', elements_list)

for i_shift in range(shift, 0, -1):
    shift_element = elements_list[len(elements_list) - 1]
    for index in range(len(elements_list) - 1, - 1, -1):
        elements_list[index] = elements_list[index - 1]
    elements_list[0] = shift_element

print('Сдвинутый список: ', elements_list)

