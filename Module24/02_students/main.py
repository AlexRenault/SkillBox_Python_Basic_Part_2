# TODO здесь писать код
from random import randint
from students import Students

name_lst = ['Алексей Алексеев', 'Борис Борисов', 'Владимир Владимиров', 'Геннадий Горский', 'Дмитрий Дмитриев',
            'Евгений Евгеньев', 'Захар Прилепин', 'Иван Иванов', 'Константин Иевлев', 'Леонид Попов']
group_lst = [randint(1, 4) for _ in range(10)]
grade_list = [[randint(1, 5) for _ in range(5)] for _ in range(10)]

students_lst = Students(name_lst, group_lst, grade_list, 10)
students_lst.print_info()
print()
students_lst.sort_list()
students_lst.print_info()






