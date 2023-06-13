# TODO здесь писать код

# Сумма цифр введенного числа
def summ_digit (number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    print('Сумма цифр числа: ', summ)
    return summ


# Количество цифр в числе
def digit_count(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    print('Количество цифр в числе: ', count)
    return count


number = int(input('Введите целое положительное число: '))

print('\nРазность суммы и количества цифр: ', summ_digit(number) - digit_count(number))
