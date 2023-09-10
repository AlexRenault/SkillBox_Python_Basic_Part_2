# TODO здесь писать код
from family import Parent


def print_info(lst):
    for fam in lst:
        fam.parent_info()


parent_lst = ['Андрей', 'Маргарита', 'Иван', 'Елена']
parent_age = [30, 26, 34, 28]
children_lst = ['Петя', 'Вова', 'Маша', 'Даша', 'Коля', 'Саша', 'Аня', 'Сережа']

family_lst = [Parent(parent_lst, parent_age, children_lst) for _ in range(len(parent_lst))]
print_info(family_lst)

for family in family_lst:
    family.calm_hunger()

print_info(family_lst)
