# TODO здесь писать код
elements_list = []
number = int(input('Введите количество элементов списка: '))
for index in range(number):
    print('Введите ', index + 1, 'элемент списка (целые числа): ', end='')
    element = int(input())
    elements_list.append(element)

shift = int(input('Сдвиг: '))

print('Изначальный список: ', elements_list)

if shift >= 0:
    #Сдвиг элементов вправо
    start_shift, stop_shift = shift, 0
    first_element = len(elements_list) - 1
    start_list, stop_list, step_list = len(elements_list) - 1, 0, -1
    add_index = -1
    end_element = 0
else:
    #Сдвиг элементов списка влево
    start_shift, stop_shift = 0, shift
    first_element = 0
    start_list, stop_list, step_list = 0, len(elements_list) - 1, 1
    add_index = 1
    end_element = len(elements_list) - 1

for i_shift in range(start_shift, stop_shift, -1):          #
    shift_element = elements_list[first_element]            #
    for index in range(start_list, stop_list, step_list):      #
        elements_list[index] = elements_list[index + add_index]     #
    elements_list[end_element] = shift_element

print('Сдвинутый список: ', elements_list)

