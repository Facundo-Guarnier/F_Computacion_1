class Palabra:
    def __init__(self):
        self.palabra = None
        self.letras = []

    def ingresar(self, palabra):
        self.palabra = palabra
        for i in palabra:
            if not(i in self.letras):
                self.letras.append(i) 


class Ahorcado:
    def __init__(self):
        self.palabra = Palabra()
        self.estado = None
        self.lista_negra = []

    def ingresarLetra(self, letra):
        if letra in self.lista_negra:
            return None
        self.lista_negra.append(letra)
        if not(letra in self.palabra.letras):
            return False
        else:
            self.palabra.letras.remove(letra)
            return True

    def ingresarPalabra(self, palabra):
        self.palabra.ingresar(palabra)




if __name__ == "__main__":                          
    juego1 = Ahorcado()
    juego1.ingresarPalabra(input("Palabra: "))    # Ingreso la palabra
    vidas = 10

    while juego1.estado == None:    # Repeticion hasta ganar
        letra = juego1.ingresarLetra(input("Letra: "))
        if letra == False:
            vidas -= 1
            print("No está")

        elif letra == True:
            print("Si está")

        elif letra == None:
            print("Ya la dijiste wey")

        if vidas == 0:
            print("Perdiste, la palabra era ", juego1.palabra.palabra)

        elif len(juego1.palabra.letras) == 0:
            print("Ganaste con {} vidas de sobra".format(vidas))

    print(juego1.estado)


# NO SE SI SE PUEDE HACER UN TEST DE ESTO, YA QUE HAY UNA PARTE DE LAS REGLAS (LAS VIDAS)