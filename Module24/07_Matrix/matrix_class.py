class Matrix:
    def __init__(self, row, col):
        self.data = [[0 for _ in range(col)] for _ in range(row)]
        self.row = row
        self.column = col

    def print(self):
        for i_row in self.data:
            for i_col in i_row:
                print(i_col, end='\t')
            print()

    def add(self, matrix):
        result = Matrix(matrix.row, matrix.column)
        for i_row, row in enumerate(self.data):
            for i_col, col in enumerate(row):
                result.data[i_row][i_col] = col + matrix.data[i_row][i_col]
        return result

    def subtract(self, matrix):
        result = Matrix(matrix.row, matrix.column)
        for i_row, row in enumerate(self.data):
            for i_col, col in enumerate(row):
                result.data[i_row][i_col] = col - matrix.data[i_row][i_col]
        return result

    def multiply(self, matrix):
        result = Matrix(matrix.column, self.row)
        for i_row, row in enumerate(self.data):
            for i_col in range(matrix.column):
                for i_elem, elem in enumerate(row):
                    result.data[i_row][i_col] += elem * matrix.data[i_elem][i_col]
        return result

    def transpose(self):
        result = Matrix(self.column, self.row)
        for i_row, row in enumerate(self.data):
            for i_col, col in enumerate(row):
                result.data[i_col][i_row] = col
        return result

