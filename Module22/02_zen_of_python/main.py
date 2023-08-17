# TODO здесь писать код
from_file = open('zen.txt', 'r', encoding='utf-8')
rev_str = ''

for line in from_file:
    if not ('\n' in line):
        line += '\n'
    rev_str = line + rev_str

print(rev_str)
