import unittest
from Untitled import Sudoku
from Untitled import ErrorUno 

class Test_1(unittest.TestCase):
    def test_primero(self):
        juego1 = Sudoku()
        with self.assertRaises(ErrorUno): 
            juego1.agregar_numero(1,2,3)



if __name__ == '__main__':
    unittest.main()