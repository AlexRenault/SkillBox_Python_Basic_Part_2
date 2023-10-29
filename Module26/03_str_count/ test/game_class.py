from random import choice
from player_class import Player
from board_class import Board


def change_player(players_lst, current,flag):
    if flag:
        for player in players_lst:
            if player != current:
                current = player
                break
    return current
class Game:
    # Класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    def __init__(self):
        symbols = ('X', 'O')
        self.players = [Player(idx, symbols[idx]) for idx in range(2)]
        self.board = Board()
        self.game_state = None

    # А также методы:
    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
    # проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
    def one_move(self, player, moves):
        cell = player.move(player.name)
        while self.board.board[cell - 1].occupied:
            print('Эта клетка занята.', self.board.board[cell - 1].symbol)
            cell = player.move(player.name)
        print('Ходил игрок {}. Всего ходов - {}.'.format(player.name, moves))
        self.board.board[cell - 1].change_cell(player.symbol)

        if self.game_over(moves):
            if moves == 9:
                print('Ничья.')
            else:
                print('ИГРА ОКОНЧЕНА!')
                print('Победил игрок {}'.format(player.name))
                player.wins += 1
            self.game_state = False
            self.board.print_board()
            self.game_status()
            return False  # Признак завершения игры при победе игрока
        else:
            return True

    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков
    # или ничьей. Если игра завершена, метод возвращает True, иначе False.
    def one_game(self):
        self.board.clear()
        self.game_status()
        self.game_state = True
        current_player = self.first()
        move = 1
        flag = True
        while flag and move <= 9:
            flag = self.one_move(current_player, move)
            if flag and move < 9:
                current_player = change_player(self.players, current_player, flag)
                self.board.print_board()
                print('\nХод переходит к игроку {}'.format(current_player.name))
            move += 1

    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать
    # играть. После каждой игры выводится текущий счёт игроков.
    def start_game(self):
        new = Game()
        while True:
            print('МЕНЮ:')
            print('1. Играть.')
            print('2. Выход.')
            play = 0
            while play not in (1, 2):
                try:
                    print('Введите 1 или 2.', end=' ')
                    play = int(input())
                except (ValueError, TypeError):
                    print("Некорректное значение!")
            if play == 1:
                new.one_game()
            elif play == 2:
                break


# Вспомогательные методы
    def game_status(self):
        if self.game_state in (None, False):
            for idx in range(2):
                print(f'Игрок {idx + 1}: {self.players[idx].name},'
                      f' символ - {self.players[idx].symbol}, '
                      f'выиграл - {self.players[idx].wins} игр.')
            self.board.print_board()

    def first(self):
        first_player = self.players[choice([0, 1])]
        print('\nПраво первого хода у игрока {}. Символ - {}\n'.format(first_player.name,
                                                                       first_player.symbol))
        self.game_state = True
        return first_player

    def game_over(self, num):
        win_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]
        for comb in win_combo:
            if self.board.board[comb[0]].symbol == self.board.board[comb[1]].symbol == \
                    self.board.board[comb[2]].symbol:
                return True
        else:
            if num == 9:
                return True
            else:
                return False
