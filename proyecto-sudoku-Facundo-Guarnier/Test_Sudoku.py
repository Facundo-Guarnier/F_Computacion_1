from Sudoku import Sudoku
import unittest
from Sudoku import ErrorNumero
from Sudoku import ErrorFila
from Sudoku import ErrorColumna
from Sudoku import ErrorNumBase
from Sudoku import NumEnFila
from Sudoku import NumEnColumna
from Sudoku import ErrorSector

class TestSudoku(unittest.TestCase):
    
    def test_init(self):            #Test de creacion 
        sudoku_obj = Sudoku()
        self.assertTrue(type(sudoku_obj.tablero), list)
        self.assertEqual(len(sudoku_obj.tablero), 9)
        self.assertTrue(type(sudoku_obj.lista_negra), list)
        self.assertEqual(len(sudoku_obj.lista_negra), 0)

        for columna in range(9):
            self.assertEqual(len(sudoku_obj.tablero[columna]), 9)
    
    def test_verify_number_is_not_initials_OK(self):        #MAL, verificar si el numero que quiero poner ya está en el aleatorio inicial.
        sudoku_obj = Sudoku()
        sudoku_obj.tablero[3][2] = " "
        self.assertTrue(sudoku_obj.verificacion_inicial(3, 2))
    
    def test_verify_number_is_initials_ERROR(self):         #MAL, lo mismo que el de arriba
        sudoku_obj = Sudoku()
        sudoku_obj.tablero[3][2] = "9"
        self.assertTrue(sudoku_obj.verificacion_inicial(3, 2))
    
    def test_tamoaño_numero(self):              #Test del numero a ingresar, FALTA LA OPCION BUENA/CORRECTA
        sudoku_obj = Sudoku()
        with self.assertRaises(ErrorNumero):       
            sudoku_obj.agregar_numero(10, 5, 2)

    def test_tamoaño_fila(self):            #Test del rango de la fila, FALTA LA OPCION BUENA/CORRECTA
        sudoku_obj = Sudoku()
        with self.assertRaises(ErrorFila):       
            sudoku_obj.agregar_numero(1, 50, 2)

    def test_tamoaño_columna(self):
        sudoku_obj = Sudoku()
        with self.assertRaises(ErrorColumna):       
            sudoku_obj.agregar_numero(1, 5, 20)

    def test_cambiar_num_base(self):
        sudoku_obj = Sudoku()
        sudoku_obj.verificacion_lista_negra(5, 2)
        with self.assertRaises(ErrorNumBase):       
            sudoku_obj.agregar_numero(1, 5, 2)

    def test_repeticion_fila(self):
        sudoku_obj = Sudoku()
        sudoku_obj.agregar_numero(1, 2, 3)
        with self.assertRaises(NumEnFila):
            sudoku_obj.agregar_numero(1, 2, 5)    

    def test_repeticion_columna(self):
        sudoku_obj = Sudoku()
        sudoku_obj.agregar_numero(1, 2, 3)  
        with self.assertRaises(NumEnColumna):       
            sudoku_obj.agregar_numero(1, 5, 3)   

    def test_repeticion_sector(self):
        sudoku_obj = Sudoku()
        sudoku_obj.agregar_numero(1, 2, 3)  
        with self.assertRaises(ErrorSector):       
            sudoku_obj.agregar_numero(1, 1, 1)  


    # def test_validate_region_nw(self, mock_request):          #Validar los sectores
    #     sudoku_obj = Sudoku()
    #     sudoku_obj.user_board[0][0] = 9
    #     self.assertFalse(sudoku_obj.validate_region(1, 1, 9))


if __name__ == '__main__':
    unittest.main()