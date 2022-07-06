import unittest
from Ahorcado_POO import Ahorcado 

class TestAhorcado(unittest.TestCase): 

    def testIngresoPalabra(self):
        juego = Ahorcado()
        juego.ingresarPalabra("aabbccddaa")
        self.assertEqual(juego.palabra.palabra, "aabbccddaa")
        self.assertEqual(juego.palabra.letras, ["a", "b", "c", "d"])

    def testIngresoLetra_ok(self):
        juego = Ahorcado()
        juego.ingresarPalabra("aabbccddaa")
        self.assertTrue(juego.ingresarLetra("a"))

    def testIngresoLetra_no_ok(self):
        juego = Ahorcado()
        juego.ingresarPalabra("aabbccddaa")
        self.assertFalse(juego.ingresarLetra("i"))


if __name__ == '__main__':
    unittest.main()