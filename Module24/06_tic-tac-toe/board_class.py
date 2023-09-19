from cell_class import Cell


class Board:
    #  Класс поля, который создаёт у себя экземпляры клетки
    def __init__(self):
        self.board = [Cell(idx, idx) for idx in range(1, 10)]

    def print_board(self):
        print()
        print('Игровое поле:\n')
        print('-' * 13)
        for idx in range(0, len(self.board), 3):
            str_print = f'| {self.board[idx].symbol} | {self.board[idx + 1].symbol}' \
                        f' | {self.board[idx + 2].symbol} |'
            if idx != 0:
                print('-' * 13)
            print(str_print)
        print('-' * 13)

    def change_cell(self, num, user_sym):
        self.board[num].occupied = user_sym

    def clear(self):
        self.board = [Cell(idx, idx) for idx in range(1, 10)]
