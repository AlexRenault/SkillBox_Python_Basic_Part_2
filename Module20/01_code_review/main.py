def find_interests(st_dict):
    interests_list = []
    count = 0
    for id_student, info_student in st_dict.items():
        interests_list += info_student['interests']
        count += len(info_student['surname'])
    return interests_list, count


# TODO исправить код
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

pairs = [(student, student_age['age']) for student, student_age in students.items()]
interests_list, length_surname = find_interests(students)

print('Список пар "ID студента — возраст": ', pairs)
print('\nПолный список интересов всех студентов: ', interests_list)
print('\nОбщая длина всех фамилий студентов: ', length_surname)
