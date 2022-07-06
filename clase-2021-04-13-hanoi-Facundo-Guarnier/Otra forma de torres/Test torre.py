import unittest
from Torres_acomodado import Juego, ErrorHumanoException


class TestTorreHanoi(unittest.TestCase):

    def test_estructura_juego(self):
        juego = Juego()
        # el juego deberia tener 3 torres
        # self.assert -> DEBERIA / DEBE!!!
        self.assertEqual(
            len(juego.torres),  # la cantidad de elementos de la lista de torres
            3,
        )
        # la torre de la izq deberia tener 6 elemento
        # la torre de la cen deberia tener 0 elemento
        # la torre de la der deberia tener 0 elemento
        # el tamano del primer de abajo disco de la izquierda, debe ser 6
        # el tamano del primer de arriba disco de la izquierda, debe ser 1

    def test_mover_inicial_de_izq_a_cen(self):
        juego = Juego()
        juego.mover(0, 1)  # 0 es la izq, 1 es el centro
        # self.assert -> DEBERIA / DEBE!!!
        # la torre de la izq deberia tener 5 elemento
        self.assertEqual(
            len(juego.torres[0].discos_apilados),  # tamano de elementos de la torre de la izq
            5,
        )
        # la torre de la cen deberia tener 1 elemento
        self.assertEqual(
            len(juego.torres[1].discos_apilados),  # tamano de elementos de la torre de la cen
            1,
        )
        # la torre de la der deberia tener 0 elemento
        self.assertEqual(
            len(juego.torres[2].discos_apilados),  # tamano de elementos de la torre de la der
            0,
        )

    def test_mover_dos_veces_de_izq_a_cen(self):
        juego = Juego()
        # primer movimiento
        juego.mover(0, 1)  # 0 es la izq, 1 es el centro
        with self.assertRaises(ErrorHumanoException):  # segundo movimiento (ILEGAL!!)
            juego.mover(0, 1)  # 0 es la izq, 1 es el centro
        # la torre de la izq deberia tener 5 elemento
        self.assertEqual(
            len(juego.torres[0].discos_apilados),  # tamano de elementos de la torre de la izq
            5,
        )
        # la torre de la cen deberia tener 1 elemento
        self.assertEqual(
            len(juego.torres[1].discos_apilados),  # tamano de elementos de la torre de la cen
            1,
        )
        # la torre de la der deberia tener 0 elemento
        self.assertEqual(
            len(juego.torres[2].discos_apilados),  # tamano de elementos de la torre de la der
            0,
        )

    def test_validar_indice_de_la_torre_no_sea_mayor_que_2(self):
        pass

    def test_validar_indice_de_la_torre_no_sea_menor_que_0(self):
        pass

    def test_si_la_torre_de_origen_tiene_discos(self):
        # Izquierda::6,5,4,3,2,1,Central::,Derecha::
        # Torre origen: (0, 1, 2):1
        # Torre destino: (0, 1, 2):2
        # Traceback (most recent call last):
        #   File "torres_de_hanoi.py", line 69, in <module>
        #     mi_juego.jugar()
        #   File "torres_de_hanoi.py", line 44, in jugar
        #     self.mover(torre_origen, torre_destino)
        #   File "torres_de_hanoi.py", line 35, in mover
        #     disco_sacado = self.torres[torre_origen].discos_apilados.pop()
        # IndexError: pop from empty list
        pass

    def test_condicion_de_victoria(self):
        pass

    def test_intentos(self):
        # creativos...
        pass


if __name__ == '__main__':
    unittest.main()
