import json
from urllib.request import (Request, urlopen,)

API_URL = 'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9'
REGION_BOARD = [
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [1, 1, 1, 2, 2, 2, 3, 3, 3],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [4, 4, 4, 5, 5, 5, 6, 6, 6],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
    [7, 7, 7, 8, 8, 8, 9, 9, 9],
]


class Sudoku():
    def __init__(self):
        # self.initial_board = [[0 for x in range(9)] for y in range(9)]  # con los numeros random
        self.user_board = [[0 for x in range(9)] for y in range(9)]  # con los numeros que va poniendo el usuario
        self.initial_board = self.request_board()

    @property
    def in_progress(self):
        for row in range(9):
            for col in range(9):
                if self.user_board[row][col] + self.initial_board[row][col] == 0:
                    return True
        return False

    @property
    def board(self):
        result = 'Inicial \n'
        for row in range(9):
            for col in range(9):
                result += str(self.initial_board[row][col])
            result += '\n'
        result += '\nCompleto \n'
        for row in range(9):
            for col in range(9):
                result += str(self.user_board[row][col] + self.initial_board[row][col])
            result += '\n'
        return result

    def request_board(self):
        request = Request(API_URL, method='GET')
        with urlopen(request) as api_response:
            api_response_string = api_response.read()
            api_response_dict = json.loads(api_response_string)
        return self.parse_response_API(api_response_dict)

    def parse_response_API(self, api_response):
        result = [[0 for i in range(9)] for j in range(9)]
        squares = api_response['squares']
        for square in squares:
            row = square['x']
            col = square['y']
            result[row][col] = square['value']
        return result

    def set_value(self, row, col, value):
        i_row = row - 1
        i_col = col - 1
        if (
            self.validate_numbers(i_row, i_col, value) and
            self.validate_initial(i_row, i_col) and
            self.validate_rules(i_row, i_col, value)
        ):
            self.user_board[i_row][i_col] = value
            return True
        else:
            return False

    def validate_numbers(self, row, col, value):
        return (
            row >= 0 and row <= 8 and
            col >= 0 and col <= 8 and
            value >= 1 and value <= 9
        )

    def validate_initial(self, row, col):
        return self.initial_board[row][col] == 0

    def validate_rules(self, row, col, value):
        return (
            self.validate_row(row, value) and
            self.validate_col(col, value) and
            self.validate_region(row, col, value)
        )

    def validate_row(self, row, value):
        for col in range(9):
            if (
                self.initial_board[row][col] == value or
                self.user_board[row][col] == value
            ):
                return False
        return True

    def validate_col(self, col, value):
        for row in range(9):
            if (
                self.initial_board[row][col] == value or
                self.user_board[row][col] == value
            ):
                return False
        return True

    def calculate_region_number(self, row, col):
        return REGION_BOARD[row][col]

    def validate_region_with_bros(self, row, col, value):
        bros_region = self.calculate_region_number(row, col)
        for i_row in range(9):
            for i_col in range(9):
                if REGION_BOARD[i_row][i_col] == bros_region:
                    if (
                        value == self.initial_board[i_row][i_col] or
                        value == self.user_board[i_row][i_col]
                    ):
                        return False
        return True


    def calculate_region(self, row, col):
        return tuple((
            (   int_row + ((row // 3) * 3),
                int_col + ((col // 3) * 3))
            for int_row in range(3)
            for int_col in range(3)
        ))

    def validate_region(self, row, col, value):
        return not value in (
            self.user_board[i_row][i_col] + self.initial_board[i_row][i_col]
            for i_row, i_col in self.calculate_region(row, col)
        )


def program():

    game = Sudoku()  # esto crea un objeto de la clase...
    while game.in_progress:
        print(game.board)
        col = input('coordenada col (1 a 9)')
        row = input('coordenada fila (1 a 9)')
        value = input('numero (1 a 9)')
        try:
            if not game.set_value(int(row), int(col), int(value)):
                print('No pude!')
        except Exception as e:
            print('Error!')
            print(e)


if __name__ == '__main__':
    program()