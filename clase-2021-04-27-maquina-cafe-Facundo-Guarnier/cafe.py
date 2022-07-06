# maquina cafe simple:
# - cafe: 5 g
# - agua: 100 ml
# - azucar (opcional: con (3 g de azucar) o sin)

# maquina de cafe es una clase
# atributos (estado): cafe, agua y azucar (tiene que recordar cuanto tiene de cosa)
# hace??
# - prepara cafe:
#   - SIEMPRE Y CUANDO TENGA LOS INGREDIENTES!
#   - BOTON con azucar:
#     - cafe: 5 g + agua: 100 ml + 3 g de azucar
#   - BOTON sin azucar
#     - cafe: 5 g + agua: 100 ml
# - si me quedo sin ingrediente, hay que reponer


import unittest

class CafeteraSimple:

    def __init__(self):
        self.cafe = 0
        self.agua = 0
        self.azucar = 0

    def agregar_cafe(self, cantidad_cafe_agregar):
        self.cafe = self.cafe + cantidad_cafe_agregar

    def agregar_azucar(self, cantidad_azucar_agregar):
        self.azucar = self.azucar + cantidad_azucar_agregar

    def agregar_agua(self, cantidad_agua_agregar):
        self.agua = self.agua + cantidad_agua_agregar

    def hacer_cafe_sin_azucar(self):
        self.agua -= 100
        self.cafe -= 5
        return True

    def hacer_cafe_con_azucar(self):
        self.agua -= 100
        self.cafe -= 5
        self.azucar -= 3
        return True


class CafeteraPremiun:

    def __init__(self):
        self.cafe = 0
        self.agua = 0
        self.azucar = 0
        self.leche = 0
        self.chocolate = 0
        self.te = 0
        self.tia_maria = 0
        self.whisky = 0
        self.crema = 0
        
        

    def hacer(self, tipo):
        print("holaaaa")
        if tipo == 1:
            print("holaaaa2")
            if self.cafe <= 0:
                print("No hay mas cafe")
                self.cafe = 0
            else:   
                print("hola3") 
                self.hacer_cafe_con_azucar
        elif tipo == 2:
            self.hacer_cafe_sin_azucar

    def agregar_cafe(self, cantidad_cafe_agregar):
        self.cafe = self.cafe + cantidad_cafe_agregar

    def agregar_azucar(self, cantidad_azucar_agregar):
        self.azucar = self.azucar + cantidad_azucar_agregar

    def agregar_agua(self, cantidad_agua_agregar):
        self.agua = self.agua + cantidad_agua_agregar
 
    def agregar_leche(self, cantidad_leche):
        self.leche += cantidad_leche

    def agregar_chocolate(self, cantidad_chocolate):
        self.chocolate += cantidad_chocolate

    def agregar_te(self, cantidad_te):
        self.te += cantidad_te

    def agregar_tia_maria(self, cantidad_tia_maria):
        self.tia_maria += cantidad_tia_maria

    def agregar_whisky(self, cantidad_whisky):
        self.whisky += cantidad_whisky

    def agregar_crema(self, cantidad_crema):
        self.crema += cantidad_crema

    def tamaño_cafe(self, tamaño):
        self.tamaño = tamaño
        return self.tamaño
    
    def hacer_cafe_con_azucar(self): #1
        if self.tamaño == 1:
            self.agua -= 100
            self.cafe -= 5
            self.azucar -= 3

        elif self.tamaño == 2:
            self.agua -= 150
            self.cafe -= 7.5
            self.azucar -= 4.5

        elif self.tamaño == 3:
            self.agua -= 200
            self.cafe -= 10
            self.azucar -= 6

        return True

    def hacer_cafe_sin_azucar(self):
        if self.tamaño == 1:
            self.agua -= 100
            self.cafe -= 5

        elif self.tamaño == 2:
            self.agua -= 150
            self.cafe -= 7.5

        elif self.tamaño == 3:
            self.agua -= 200
            self.cafe -= 10
        return True

    def hacer_capuccino(self):
        if self.tamaño == 1:
            self.leche -= 100
            self.cafe -= 6
            self.crema -= 3
            self.chocolate -= 3

        elif self.tamaño == 2:
            self.leche -= 150
            self.cafe -= 9
            self.crema -= 4.5
            self.chocolate -= 4.5

        elif self.tamaño == 3:
            self.leche -= 200
            self.cafe -= 12
            self.crema -= 6
            self.chocolate -= 6

        return True

    def hacer_chocolate(self):
        if self.tamaño == 1:
            self.leche -= 50
            self.chocolate -= 50

        elif self.tamaño == 2:
            self.leche -= 75
            self.chocolate -= 75

        elif self.tamaño == 3:
            self.leche -= 100
            self.chocolate -= 100
        
        return True

    def hacer_te_sin_azucar(self):
        if self.tamaño == 1:
            self.te -= 100

        elif self.tamaño == 2:
            self.te -= 150

        elif self.tamaño == 3:
            self.te -= 200
        
        return True

    def hacer_te_con_azucar(self):
        if self.tamaño == 1:
            self.te -= 100
            self.azucar -= 3

        elif self.tamaño == 2:
            self.te -= 150
            self.azucar -= 4.5

        elif self.tamaño == 3:
            self.te -= 200
            self.azucar -= 6

        return True
    
    def hacer_cafe_irlandes(self): 
        if self.tamaño == 1:
            self.tia_maria -= 10
            self.whisky -= 10
            self.cafe -= 70
            self.crema -= 10

        elif self.tamaño == 2:
            self.tia_maria -= 15
            self.whisky -= 15
            self.cafe -= 105
            self.crema -= 15

        elif self.tamaño == 3:
            self.tia_maria -= 20
            self.whisky -= 20
            self.cafe -= 140
            self.crema -= 20

        return True
    
    def hacer_te_con_leche(self):         
        if self.tamaño == 1:
            self.te -= 50
            self.leche -= 50

        elif self.tamaño == 2:
            self.te -= 75
            self.leche -= 75

        elif self.tamaño == 3:
            self.te -= 100
            self.leche -= 100

        return True

    def hacer_cafe_con_crema(self):         
        if self.tamaño == 1:
            self.cafe -= 90
            self.crema -= 10

        elif self.tamaño == 2:
            self.cafe -= 135
            self.crema -= 15

        elif self.tamaño == 3:
            self.cafe -= 180
            self.crema -= 20

        return True

    def hacer_cafe_al_whisky(self):         
        if self.tamaño == 1:
            self.cafe -= 90
            self.whisky -= 10

        elif self.tamaño == 2:
            self.cafe -= 135
            self.whisky -= 15

        elif self.tamaño == 3:
            self.cafe -= 180
            self.whisky -= 20

        return True

    def __str__(self):
        return str(self.cafe) + " < tengo cafe"


class TestCafeteraSimple(unittest.TestCase):
    
    def test_cafetera_nueva_vacia(self):
        mi_cafetera = CafeteraSimple()
        self.assertEqual(mi_cafetera.cafe, 0)
        self.assertEqual(mi_cafetera.agua, 0)
        self.assertEqual(mi_cafetera.azucar, 0)

    def test_cafetera_carga_cafe(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_cafe(1000)
        self.assertEqual(mi_cafetera.cafe, 1000)
        self.assertEqual(mi_cafetera.agua, 0)
        self.assertEqual(mi_cafetera.azucar, 0)

    def test_cafetera_segunda_carga_cafe(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_cafe(1000)
        mi_cafetera.agregar_cafe(500)
        self.assertEqual(mi_cafetera.cafe, 1500)
        self.assertEqual(mi_cafetera.agua, 0)
        self.assertEqual(mi_cafetera.azucar, 0)

    def test_cafetera_carga_azucar(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_azucar(1000)
        self.assertEqual(mi_cafetera.cafe, 0)
        self.assertEqual(mi_cafetera.agua, 0)
        self.assertEqual(mi_cafetera.azucar, 1000)

    def test_cafetera_segunda_carga_azucar(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_azucar(1000)
        mi_cafetera.agregar_azucar(500)
        self.assertEqual(mi_cafetera.cafe, 0)
        self.assertEqual(mi_cafetera.agua, 0)
        self.assertEqual(mi_cafetera.azucar, 1500)

    def test_cafetera_carga_agua(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_agua(1000)
        self.assertEqual(mi_cafetera.cafe, 0)
        self.assertEqual(mi_cafetera.azucar, 0)
        self.assertEqual(mi_cafetera.agua, 1000)

    def test_cafetera_segunda_carga_agua(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_agua(1000)
        mi_cafetera.agregar_agua(500)
        self.assertEqual(mi_cafetera.cafe, 0)
        self.assertEqual(mi_cafetera.azucar, 0)
        self.assertEqual(mi_cafetera.agua, 1500)

    def test_hacer_cafe_sin_azucar_camino_feliz(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_cafe(50)
        mi_cafetera.agregar_agua(300)
        hice_un_cafe = mi_cafetera.hacer_cafe_sin_azucar()
        self.assertTrue(hice_un_cafe)
        self.assertEqual(mi_cafetera.cafe, 45)
        self.assertEqual(mi_cafetera.agua, 200)
        self.assertEqual(mi_cafetera.azucar, 0)

    def test_hacer_cafe_con_azucar_camino_feliz(self):
        mi_cafetera = CafeteraSimple()
        mi_cafetera.agregar_cafe(50)
        mi_cafetera.agregar_agua(300)
        mi_cafetera.agregar_azucar(100)
        hice_un_cafe = mi_cafetera.hacer_cafe_con_azucar()
        self.assertTrue(hice_un_cafe)
        self.assertEqual(mi_cafetera.cafe, 45)
        self.assertEqual(mi_cafetera.agua, 200)
        self.assertEqual(mi_cafetera.azucar, 97)


class TestCafeteraPremiun(unittest.TestCase):

    def test_segunda_carga_cafe(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(100)
        mi_cafe.agregar_cafe(50)
        self.assertEqual(mi_cafe.cafe, 150)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_azucar(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_azucar(100)
        mi_cafe.agregar_azucar(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 150)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_agua(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_agua(100)
        mi_cafe.agregar_agua(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 150)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_leche(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_leche(100)
        mi_cafe.agregar_leche(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 150)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_chocolate(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_chocolate(100)
        mi_cafe.agregar_chocolate(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 150)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_te(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_te(100)
        mi_cafe.agregar_te(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 150)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)
    
    def test_segunda_carga_tia_maria(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_tia_maria(100)
        mi_cafe.agregar_tia_maria(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 150)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_whisky(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_whisky(100)
        mi_cafe.agregar_whisky(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 150)
        self.assertEqual(mi_cafe.crema, 0)

    def test_segunda_carga_crema(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_crema(100)
        mi_cafe.agregar_crema(50)
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 150)

    def test_elegir_tamaño(self):
        mi_cafe = CafeteraPremiun()
        self.assertEqual(mi_cafe.tamaño_cafe(3), 3)

    def test_cafe_con_azucar(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_cafe(50)
        mi_cafe.agregar_azucar(100)
        mi_cafe.agregar_agua(5000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_cafe_con_azucar())
        self.assertEqual(mi_cafe.cafe, 1040)
        self.assertEqual(mi_cafe.azucar, 94)
        self.assertEqual(mi_cafe.agua, 4800)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)
        
    def test_capuccino(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_cafe(50)
        mi_cafe.agregar_azucar(100)
        mi_cafe.agregar_agua(5000)
        mi_cafe.agregar_leche(2000)
        mi_cafe.agregar_chocolate(100)
        mi_cafe.agregar_crema(100)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_capuccino())
        self.assertEqual(mi_cafe.cafe, 1038)
        self.assertEqual(mi_cafe.azucar, 100)
        self.assertEqual(mi_cafe.agua, 5000)
        self.assertEqual(mi_cafe.leche, 1800)
        self.assertEqual(mi_cafe.chocolate, 94)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 94)

    def test_cafe_sin_azucar(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_cafe(50)
        mi_cafe.agregar_azucar(100)
        mi_cafe.agregar_agua(5000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_cafe_sin_azucar())
        self.assertEqual(mi_cafe.cafe, 1040)
        self.assertEqual(mi_cafe.azucar, 100)
        self.assertEqual(mi_cafe.agua, 4800)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)
    
    def test_chocolate(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_cafe(50)
        mi_cafe.agregar_azucar(100)
        mi_cafe.agregar_agua(5000)
        mi_cafe.agregar_leche(2000)
        mi_cafe.agregar_chocolate(2000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_chocolate())
        self.assertEqual(mi_cafe.cafe, 1050)
        self.assertEqual(mi_cafe.azucar, 100)
        self.assertEqual(mi_cafe.agua, 5000)
        self.assertEqual(mi_cafe.leche, 1900)
        self.assertEqual(mi_cafe.chocolate, 1900)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_te_sin_azucar(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_te(1000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_te_sin_azucar())
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 800)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_te_con_azucar(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_te(1000)
        mi_cafe.agregar_azucar(1000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_te_con_azucar())
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 994)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 800)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_cafe_irlandes(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_tia_maria(500)
        mi_cafe.agregar_whisky(500)
        mi_cafe.agregar_crema(500)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_cafe_irlandes())
        self.assertEqual(mi_cafe.cafe, 860)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 480)
        self.assertEqual(mi_cafe.whisky, 480)
        self.assertEqual(mi_cafe.crema, 480)

    def test_cafe_te_con_leche(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_te(1000)
        mi_cafe.agregar_leche(1000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_te_con_leche())
        self.assertEqual(mi_cafe.cafe, 0)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 900)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 900)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 0)

    def test_cafe_con_crema(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_crema(1000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_cafe_con_crema())
        self.assertEqual(mi_cafe.cafe, 820)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 0)
        self.assertEqual(mi_cafe.crema, 980)

    def test_cafe_al_whisky(self):
        mi_cafe = CafeteraPremiun()
        mi_cafe.agregar_cafe(1000)
        mi_cafe.agregar_whisky(1000)
        mi_cafe.tamaño_cafe(3)
        self.assertTrue(mi_cafe.hacer_cafe_al_whisky())
        self.assertEqual(mi_cafe.cafe, 820)
        self.assertEqual(mi_cafe.azucar, 0)
        self.assertEqual(mi_cafe.agua, 0)
        self.assertEqual(mi_cafe.leche, 0)
        self.assertEqual(mi_cafe.chocolate, 0)
        self.assertEqual(mi_cafe.te, 0)
        self.assertEqual(mi_cafe.tia_maria, 0)
        self.assertEqual(mi_cafe.whisky, 980)
        self.assertEqual(mi_cafe.crema, 0)

if __name__ == '__main__':  
    
    mi_cafe = CafeteraPremiun()
    mi_cafe.agregar_cafe(100)
    while True:                 #Areglar porque no resta cafe con .hacer(input)
        mi_cafe.tamaño_cafe(int(input("Tamaño: \n  >Chico (1) \n  >Mediano (2) \n  >Grande (3) \nIngrese el numero correspondinte: ")))
        mi_cafe.hacer(int(input("Tipos: \n  >Cafe con azúcar (1)\n  >Cafe sin azúcar (2)\n  >Capuccino (3)\n  >Chocolate (4)\n  >Té sin azucar (5)\n  >Té con azúcar (6)\n  >Café Irlandes (7)\n  >Té con leche (8)\n  >Café con crema (9)\n  >Cafe al Whisky (10)\n")))
        #mi_cafe.hacer_cafe_sin_azucar()
        print(mi_cafe.cafe) 
    unittest.main()