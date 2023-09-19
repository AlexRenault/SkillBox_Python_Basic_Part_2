class Cell:
    #   - занята клетка или нет
    #   - номер клетки
    #   - символ, который клетка хранит (пустая, крестик, нолик).
    def __init__(self, num, sym):
        self.occupied = False   # Клетка свободна
        self.number = num       # Номер клетки
        self.symbol = sym       # Символ Х, О, пусто

    def change_cell(self, sym):
        self.occupied = True    # Клетка занята
        self.symbol = sym       # Символ
