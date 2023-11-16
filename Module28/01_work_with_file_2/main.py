# TODO здесь писать код
import os

class File:
    def __init__(self, name: str) ->None:
        self.file_name = name
        self.file = None

    def __enter__(self):
        if self.file_name in os.listdir(os.getcwd()):
            mode = 'r'
        else:
            mode = 'w'
        self.file = open(self.file_name, mode, encoding='utf-8')
        if mode == 'r':
            print(self.file.read())
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt') as file:
    file.write('Всем привет!')
