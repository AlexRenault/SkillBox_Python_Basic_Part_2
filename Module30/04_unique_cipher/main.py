# TODO здесь писать код
from collections import Counter


def count_unique_characters(string):
    string = string.lower()
    char_count_list = Counter(string)
    print(char_count_list)
    unique = sum(filter(lambda char_count: char_count == 1, char_count_list.values()))
    return unique


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
