class Student:

    def __init__(self, name_surname, group, lst):
        self.name_surname = name_surname
        self.group = group
        self.grade = lst
        self.avg_ball = sum(self.grade) / len(self.grade)

    def info(self):
        print('ФИ - {},\tГруппа - {},\tОценки - {}\tСредний балл - {}'.format(
            self.name_surname, self.group, self.grade, self.avg_ball)
        )


class Students:

    def __init__(self, name, group, lst, count):
        self.students = [Student(name[idx], group[idx], lst[idx]) for idx in range(count)]

    def print_info(self):
        for student in self.students:
            student.info()

    def sort_list(self):
        return self.students.sort(key=sort_key)


def sort_key(a):
    return a.avg_ball
