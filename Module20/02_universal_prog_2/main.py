# TODO здесь писать код
def result(data):
    return [data[item] if isinstance(data, dict) else item for idx, item in enumerate(data) if is_prime(idx)]


def is_prime(number):
    if number >= 2:
        for i_num in range(2, number):
            if number % i_num == 0:
                return False
                break
        return True
    else:
        return False


# user_data = [100, 200, 300, 'буква', 0, 2, 'а']
# user_data = {1: 100, 2: 200, 3: 300, 4: 'буква', 5: 0, 6: 2, 7: 'a'}
#user_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# user_data = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# user_data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
user_data = 'О Дивный Новый мир!'

print(result(user_data))
