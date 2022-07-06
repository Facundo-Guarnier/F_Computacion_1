import math

class Punto:
    def __init__(self):
        self.x = 0
        self.y = 0

    def ingresar(self):
        self.x = int(input('Ingrese coordenada x: '))
        self.y = int(input('Ingrese coordenada y: '))

    def distancia(self, punto):
        return math.sqrt((self.x - punto.x) ** 2 + (self.y - punto.y) ** 2)

class Triangulo:
    def __init__(self):
        self.punto1 = Punto()
        self.punto2 = Punto()
        self.punto3 = Punto()

    def ingresar(self):
        print('Ingrese datos del triangulo: ')
        print(' Punto 1: ')
        self.punto1.ingresar()
        print(' Punto 2: ')
        self.punto2.ingresar()
        print(' Punto 3: ')
        self.punto3.ingresar()

    def perimetro(self):
        d1 = self.punto1.distancia(self.punto2)
        d2 = self.punto2.distancia(self.punto3)
        d3 = self.punto3.distancia(self.punto1)
        return d1 + d2 + d3

triangulo = Triangulo()
triangulo.ingresar()
perimetro = triangulo.perimetro()

print('Perimetro', perimetro)