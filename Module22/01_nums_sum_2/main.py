# TODO здесь писать код
from_file = open('numbers.txt', 'r', encoding='utf-8')
summ = 0
for i_line in from_file:
    for sym in i_line:
        if sym.isdigit():
            summ += int(sym)
from_file.close()

to_file = open('answer.txt', 'w')
to_file.write(str(summ))
to_file.close()
