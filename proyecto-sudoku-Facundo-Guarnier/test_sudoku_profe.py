import unittest
from unittest import mock
from sudoku_profe import Sudoku


def get_mock_response():
    return [[0 for x in range(9)] for y in range(9)]


@mock.patch.object(
    Sudoku, 'request_board',
    side_effect=get_mock_response,
)
class TestSudoku(unittest.TestCase):
    def test_init(self, mock_request):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertTrue(type(sudoku_obj.initial_board), list)
        self.assertTrue(type(sudoku_obj.user_board), list)
        self.assertEqual(len(sudoku_obj.initial_board), 9)
        self.assertEqual(len(sudoku_obj.user_board), 9)
        for col in range(9):
            self.assertEqual(len(sudoku_obj.initial_board[col]), 9)
            self.assertEqual(len(sudoku_obj.user_board[col]), 9)

    def test_validate_numbers_OK(self, mock_request):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertTrue(sudoku_obj.validate_numbers(1, 2, 5))

    def test_validate_numbers_row(self, mock_request):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertFalse(sudoku_obj.validate_numbers(-1, 5, 5))
        self.assertFalse(sudoku_obj.validate_numbers(10, 5, 5))

    def test_validate_numbers_col(self, mock_request):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertFalse(sudoku_obj.validate_numbers(5, -1, 5))
        self.assertFalse(sudoku_obj.validate_numbers(5, 10, 5))

    def test_validate_numbers_value(self, mock_request):
        sudoku_obj = Sudoku()  # Creo un objeto de la clase sudoku
        self.assertFalse(sudoku_obj.validate_numbers(5, 5, 0))
        self.assertFalse(sudoku_obj.validate_numbers(5, 5, 10))

    def test_verify_number_is_not_initials_OK(self, mock_request):
        sudoku_obj = Sudoku()
        # quiero probar que en fila, cola no era un valor initial del juego
        sudoku_obj.initial_board[3][2] = 0
        self.assertTrue(sudoku_obj.validate_initial(3, 2))

    def test_verify_number_is_initials_ERROR(self, mock_request):
        sudoku_obj = Sudoku()
        # quiero probar que en fila, cola si era un valor initial del juego
        sudoku_obj.initial_board[3][2] = 9
        self.assertFalse(sudoku_obj.validate_initial(3, 2))

    def test_validate_set_value_ok(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.set_value(1, 1, 9)
        self.assertEqual(sudoku_obj.user_board[0][0], 9)

    def test_validate_set_value_error_initial_board(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.initial_board[0][0] = 5
        sudoku_obj.set_value(1, 1, 9)
        self.assertEqual(sudoku_obj.initial_board[0][0], 5)
        self.assertEqual(sudoku_obj.user_board[0][0], 0)

    def test_validate_row_ok(self, mock_request):
        sudoku_obj = Sudoku()
        self.assertTrue(sudoku_obj.validate_row(1, 8))

    def test_validate_row_error_initial_board(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.initial_board[0][2] = 9
        self.assertFalse(sudoku_obj.validate_row(0, 9))

    def test_validate_row_error_user_board(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.user_board[0][2] = 9
        self.assertFalse(sudoku_obj.validate_row(0, 9))

    def test_validate_col_ok(self, mock_request):
        sudoku_obj = Sudoku()
        self.assertTrue(sudoku_obj.validate_col(0, 9))

    def test_validate_col_error_initial_board(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.initial_board[0][2] = 9
        self.assertFalse(sudoku_obj.validate_col(2, 9))

    def test_validate_col_error_user_board(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.user_board[0][2] = 9
        self.assertFalse(sudoku_obj.validate_col(2, 9))

    def test_calculate_region_north_west(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row, col),
                    (
                        (0, 0), (0, 1), (0, 2),
                        (1, 0), (1, 1), (1, 2),
                        (2, 0), (2, 1), (2, 2),
                    )
                )

    def test_calculate_region_west(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row + 3, col),
                    (
                        (3, 0), (3, 1), (3, 2),
                        (4, 0), (4, 1), (4, 2),
                        (5, 0), (5, 1), (5, 2),
                    )
                )

    def test_calculate_region_south_west(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row + 6, col),
                    (
                        (6, 0), (6, 1), (6, 2),
                        (7, 0), (7, 1), (7, 2),
                        (8, 0), (8, 1), (8, 2),
                    )
                )

    def test_calculate_region_north(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row, col + 3),
                    (
                        (0, 3), (0, 4), (0, 5),
                        (1, 3), (1, 4), (1, 5),
                        (2, 3), (2, 4), (2, 5),
                    )
                )

    def test_calculate_region_north_east(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row + 6, col + 3),
                    (
                        (6, 3), (6, 4), (6, 5),
                        (7, 3), (7, 4), (7, 5),
                        (8, 3), (8, 4), (8, 5),
                    )
                )

    def test_calculate_region_center(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row + 3, col + 3),
                    (
                        (3, 3), (3, 4), (3, 5),
                        (4, 3), (4, 4), (4, 5),
                        (5, 3), (5, 4), (5, 5),
                    )
                )

    def test_calculate_region_south(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row + 6, col + 3),
                    (
                        (6, 3), (6, 4), (6, 5),
                        (7, 3), (7, 4), (7, 5),
                        (8, 3), (8, 4), (8, 5),
                    )
                )

    def test_calculate_region_south_east(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(
                    sudoku_obj.calculate_region(row + 6, col + 6),
                    (
                        (6, 6), (6, 7), (6, 8),
                        (7, 6), (7, 7), (7, 8),
                        (8, 6), (8, 7), (8, 8),
                    )
                )

    def test_validate_region_nw(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.user_board[0][0] = 9
        self.assertFalse(sudoku_obj.validate_region(0, 0, 9))

    def test_region_bros_nw(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(sudoku_obj.calculate_region_number(row, col), 1)

    def test_region_bros_n(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(sudoku_obj.calculate_region_number(row, col + 3), 2)

    def test_region_bros_se(self, mock_request):
        sudoku_obj = Sudoku()
        for row in range(3):
            for col in range(3):
                self.assertEqual(sudoku_obj.calculate_region_number(row + 6, col + 6), 9)

    def test_validate_region_with_bros_nw_error(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.initial_board[2][2] = 9
        self.assertFalse(sudoku_obj.validate_region_with_bros(1, 1, 9))

    def test_parse_response_API(self, mock_request):

        mock_response = {
            "response": True,
            "size": "9",
            "squares": [
                {"x": 0, "y": 0, "value": 8}, {"x": 0, "y": 4, "value": 7},
                {"x": 0, "y": 7, "value": 9}, {"x": 1, "y": 1, "value": 5},
                {"x": 1, "y": 3, "value": 4}, {"x": 1, "y": 5, "value": 9},
                {"x": 1, "y": 7, "value": 7}, {"x": 2, "y": 0, "value": 7},
                {"x": 2, "y": 1, "value": 4}, {"x": 2, "y": 2, "value": 9},
                {"x": 2, "y": 4, "value": 6}, {"x": 2, "y": 6, "value": 5},
                {"x": 3, "y": 2, "value": 3}, {"x": 3, "y": 7, "value": 2},
                {"x": 3, "y": 8, "value": 9}, {"x": 4, "y": 1, "value": 7},
                {"x": 4, "y": 2, "value": 4}, {"x": 4, "y": 3, "value": 3},
                {"x": 4, "y": 4, "value": 2}, {"x": 4, "y": 6, "value": 8},
                {"x": 5, "y": 2, "value": 2}, {"x": 5, "y": 3, "value": 1},
                {"x": 5, "y": 5, "value": 5}, {"x": 5, "y": 7, "value": 3},
                {"x": 5, "y": 8, "value": 4}, {"x": 6, "y": 2, "value": 8},
                {"x": 6, "y": 4, "value": 3}, {"x": 6, "y": 6, "value": 1},
                {"x": 6, "y": 8, "value": 5}, {"x": 7, "y": 0, "value": 1},
                {"x": 7, "y": 1, "value": 6}, {"x": 7, "y": 3, "value": 9},
                {"x": 7, "y": 5, "value": 4}, {"x": 7, "y": 7, "value": 8},
                {"x": 7, "y": 8, "value": 2}, {"x": 8, "y": 0, "value": 2},
                {"x": 8, "y": 2, "value": 5}, {"x": 8, "y": 3, "value": 6},
                {"x": 8, "y": 4, "value": 8}, {"x": 8, "y": 5, "value": 1},
                {"x": 8, "y": 7, "value": 4}
            ]
        }
        sudoku_obj = Sudoku()
        self.assertEqual(
            sudoku_obj.parse_response_API(mock_response),
            [
                [8, 0, 0, 0, 7, 0, 0, 9, 0],
                [0, 5, 0, 4, 0, 9, 0, 7, 0],
                [7, 4, 9, 0, 6, 0, 5, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 2, 9],
                [0, 7, 4, 3, 2, 0, 8, 0, 0],
                [0, 0, 2, 1, 0, 5, 0, 3, 4],
                [0, 0, 8, 0, 3, 0, 1, 0, 5],
                [1, 6, 0, 9, 0, 4, 0, 8, 2],
                [2, 0, 5, 6, 8, 1, 0, 4, 0],
            ],
        )

    def test_in_progress_running(self, mock_request):
        sudoku_obj = Sudoku()
        self.assertTrue(sudoku_obj.in_progress)

    def test_in_progress_no_win(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.inital_board = [[9 for x in range(9)] for y in range(8)]
        self.assertTrue(sudoku_obj.in_progress)

    def test_in_progress_win(self, mock_request):
        sudoku_obj = Sudoku()
        sudoku_obj.user_board = [[9 for x in range(9)] for y in range(9)]
        self.assertFalse(sudoku_obj.in_progress)


if __name__ == '__main__':
    unittest.main()