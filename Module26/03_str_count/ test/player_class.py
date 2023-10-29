class Player:
    #  У игрока может быть:
    #  имя,
    #  количество побед.

    def __init__(self, num_player, sym):
        self.name = 'Игрок_' + str(num_player + 1)
        self.symbol = sym
        self.wins = 0

    #  Класс должен содержать метод:
    #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки).
    #   Введённый номер нужно обязательно проверить.
    def move(self, name):
        move = 0
        while move <= 0 or move > 9:
            print('Введите цифру от 1 до 9.')
            try:
                move = int(input(f'{name} укажите номер клетки игрового поля: '))
            except (TypeError, ValueError):
                print('\nВведено некорректное значение. Попробуйте еще раз.\n')
        return move

