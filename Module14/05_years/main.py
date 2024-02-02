# TODO здесь писать код

def find(year):
    work = year
    digit = work % 10
    count = 1
    work //= 10
    while work > 0:
        if digit == work % 10:
            count += 1
        work //= 10
    if count == 3:
        print(year)


start_year = int(input('Введите первый год: '))
end_year = int(input('Введите последний год: '))

for index in range(start_year, end_year + 1):
    find(index)
