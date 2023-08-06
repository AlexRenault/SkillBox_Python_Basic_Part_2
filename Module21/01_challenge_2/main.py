# TODO здесь писать код
def out_numbers(num):
    if num == 0:
        return 0
    else:
        out_numbers(num - 1)
        print(num)
        num -= 1


number = int(input('Введите число: '))

out_numbers(number)