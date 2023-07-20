# TODO здесь писать код

string = input('Введите строку: ')
coding = []
idx = 0
count_list = []
char_list = []

while idx <= len(string) - 1:
    count = 0
    while idx + count < len(string) and string[idx] == string[idx + count]:
        count += 1
    count_list.append(str(count))
    char_list.append(string[idx])
    idx += count

for index in range(len(char_list)):
    coding.extend([char_list[index], count_list[index]])

coding_str = ''.join(coding)
print('Закодированная строка: ', coding_str)
