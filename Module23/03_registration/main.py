# TODO здесь писать код
def check_count(user_lst):
    if len(user_lst) < 3:
        raise IndexError('\t Строка содержит не все данные.')


def check_name(name):
    if not name.isalpha():
        raise NameError('\t В имени содержаться не только буквы.')


def check_mail(mail):
    if not (mail.count('@') and mail.count('.')):
        raise SyntaxError('\t Не верный формат адреса электронной почты (отсутствует @ и/или ".").')


def check_age(age):
    if age.isnumeric():
        if not 10 < int(age) <= 99:
            raise ValueError('\t Возраст НЕ является числом от 0 до 99.')


with open('registrations.txt', 'r', encoding='utf-8') as open_file:
    with open('registration_good.log', 'w', encoding='utf-8') as good_file:
        with open('registration_bad.log', 'w', encoding='utf-8') as bad_file:
            for i_line in open_file:
                file = good_file
                user = i_line.split()
                try:
                    if len(user) < 3:
                        raise IndexError(''.join([i_line.rstrip(), '\t Строка содержит не все данные.']))
                    if not user[0].isalpha():
                        raise NameError(''.join([i_line.rstrip(), '\t В имени содержаться не только буквы.']))
                    if not (user[1].count('@') and user[1].count('.')):
                        raise SyntaxError(''.join([i_line.rstrip() + '\t Не верный формат адреса электронной почты '
                                                            '(отсутствует @ и/или ".").']))
                    if user[2].isnumeric():
                        if not 10 < int(user[2]) <= 99:
                            raise ValueError(''.join([i_line.rstrip(), '\t Возраст НЕ является числом от 0 до 99.']))

                except (IndexError, NameError, SyntaxError, ValueError) as err:
                    bad_file.write(str(err) + '\n')
                else:
                    good_file.write(i_line)
