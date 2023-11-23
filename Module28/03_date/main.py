# TODO здесь писать код
import datetime


class Date:
    def __init__(self, string):
        self.date = string

    def __str__(self):
        return "Число: {0}\t Месяц: {1}\t Год: {2}".format(
            self.date[0], self.date[1], self.date[2])

    @classmethod
    def is_date_valid(cls, string):
        try:
            dat = datetime.datetime.strptime(string, "%d-%m-%Y")
            if dat:
                return True
        except ValueError:
            return False

    @classmethod
    def from_string(cls, string):
        if cls.is_date_valid(string):
            dat = string.split("-")
            return Date(dat)


date = Date.from_string('10-12-2077')
print(date)
print('\nПроверка на корректность:')
print('10-12-2077 - ', Date.is_date_valid('10-12-2077'))
print('10-13-2077 - ', Date.is_date_valid('10-13-2077'))





