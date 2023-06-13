# TODO здесь писать код
def nod (number):
    div = 2
    while number % div != 0:
        div += 1
    return div



number = int(input('Введите натуральное число большее 1: '))

print('Наименьший делитель, отличный от единицы: ', nod(number))