# TODO здесь писать код
def check_count(user_lst):
    if len(user_lst) < 3:
        raise IndexError


def check_name(name):
    if not name.isalpha():
        raise NameError


def check_mail(mail):
    if not (mail.count('@') and mail.count('.')):
        raise SyntaxError


def check_age(age):
    if age.isnumeric():
        if not 10 < int(age) <= 99:
            raise ValueError


with open('registrations.txt', 'r', encoding='utf-8') as open_file:
    with open('registration_good.log', 'w', encoding='utf-8') as good_file:
        with open('registration_bad.log', 'w', encoding='utf-8') as bad_file:
            for i_line in open_file:
                file = good_file
                user = i_line.split()
                try:
                    check_count(user)
                    check_name(user[0])
                    check_mail(user[1])
                    check_age(user[2])
                except IndexError:
                    user.append('\t Не корректное количество полей.')
                    file = bad_file
                except NameError:
                    user.append('\t Поле "Имя" содержит цифры.')
                    file = bad_file
                except SyntaxError:
                    user.append('\t Не корректно указан адрес электронной почты.')
                    file = bad_file
                except ValueError:
                    user.append('\t Возраст не является числом щт 10 до 99.')
                    file = bad_file
                finally:
                    file.write(' '.join(user) + '\n')
