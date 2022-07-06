import unittest
from torres_de_hanoi import Juego

class TestTorreHanoi(unittest.TestCase):
    
    def test_estructura_juego(self):
        juego = Juego()
        
        self.assertEqual(len(juego.torres), 3)                          #El juego deberia tener 3 torres
        
        self.assertEqual(len(juego.torres[0].discos_apilados), 6)       #La torre de la izq deberia tener 6 elemento

        self.assertEqual(len(juego.torres[1].discos_apilados), 0)       #La torre de la cen deberia tener 0 elemento

        self.assertEqual(len(juego.torres[2].discos_apilados), 0)       #La torre de la der deberia tener 0 elemento

        self.assertEqual(juego.torres[0].discos_apilados[0].tamano, 6)  #El tamano del primer de abajo disco de la izquierda, debe ser 6
        
        self.assertEqual(juego.torres[0].discos_apilados[-1].tamano, 1) #El tamano del primer de arriba disco de la izquierda, debe ser 1
        

    def test_mover_inicial_de_izq_a_cen(self):
        juego = Juego()
        juego.mover(0, 1)
        
        self.assertEqual(len(juego.torres[0].discos_apilados), 5)       #La torre de la izq deberia tener 5 elemento
        
        self.assertEqual(len(juego.torres[1].discos_apilados), 1)       #La torre de la cen deberia tener 1 elemento
        
        self.assertEqual(len(juego.torres[2].discos_apilados), 0)       #La torre de la der deberia tener 0 elemento


    def test_mover_dos_veces_de_izq_a_cen(self):
        juego = Juego()
        juego.mover(0, 1) 
        juego.mover(0, 1)       #Segundo movimiento, no se deberia poder hacer.

        self.assertEqual(len(juego.torres[0].discos_apilados), 5)        #La torre de la izq deberia tener 5 elemento

        self.assertEqual(len(juego.torres[1].discos_apilados), 1)        #La torre de la cen deberia tener 1 elemento

        self.assertEqual(len(juego.torres[2].discos_apilados), 0)        #La torre de la der deberia tener 0 elemento
    
    
    def test_validar_indice_de_la_torre_no_sea_mayor_que_2(self):  
        juego = Juego()
        juego.mover(0, 9)
        
        self.assertEqual(len(juego.torres[0].discos_apilados), 6)
        
        self.assertEqual(len(juego.torres[1].discos_apilados), 0)       
        
        self.assertEqual(len(juego.torres[2].discos_apilados), 0)       
    
    
    def test_validar_indice_de_la_torre_no_sea_menor_que_0(self):
        juego = Juego()
        juego.mover(0, -9)
        
        self.assertEqual(len(juego.torres[0].discos_apilados), 6)
        
        self.assertEqual(len(juego.torres[1].discos_apilados), 0)       
        
        self.assertEqual(len(juego.torres[2].discos_apilados), 0)     


    def test_validar_indice_de_la_torre_no_es_un_numero(self):
        juego = Juego()
        juego.mover(0, "i")
        
        self.assertEqual(len(juego.torres[0].discos_apilados), 6)
        
        self.assertEqual(len(juego.torres[1].discos_apilados), 0)       
        
        self.assertEqual(len(juego.torres[2].discos_apilados), 0)   


    def test_si_la_torre_de_origen_tiene_discos(self):
        juego = Juego()
        juego.mover(2, 1)       #Primer movimiento

        self.assertEqual(len(juego.torres[0].discos_apilados), 6)       #La torre de la izq deberia tener 6 elemento

        self.assertEqual(len(juego.torres[1].discos_apilados), 0)       #La torre de la cen deberia tener 0 elemento

        self.assertEqual(len(juego.torres[2].discos_apilados), 0)       #La torre de la der deberia tener 0 elemento

    
    def test_condicion_de_victoria(self):
        juego = Juego()
        #La unica forma que se me ocurrio es hacer los 64 movimientos minimos para completar el juego pero no debe ser así.
        #self.assertEqual(juego.ganador, True)
        pass

    
    def test_intentos(self):        #Lo consideré como si fueran mvimientos.
        juego = Juego()
        juego.mover(0, 1)
        juego.mover(0, 2)
        juego.mover(1, 2)
        self.assertEqual(juego.intentos, 3)


if __name__ == '__main__':
    unittest.main()