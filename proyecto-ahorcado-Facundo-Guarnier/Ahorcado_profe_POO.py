from letra_profe import Letra

class Ahorcado:
    def __init__(self):
        self.palabra = []
        self.vida = 5
        self.riesgo = 0
        self.intentos = []

    def iniciar(self):
        for letra in input('Ingrese la palabra a adivinar: '):
            self.palabra.append(Letra(letra))

    def ganado(self):
        adivinada = True
        for letra in self.palabra:
            if not letra.adivinada:
                adivinada = False
        if adivinada:
            print('Adivinaste, la palabra es: "{}"'.format(self.interface(True)))
        return adivinada

    def perdido(self):
        resultado_perdido = self.vida == 0
        if resultado_perdido:
            print('Perdiste')
        return resultado_perdido

    def interface(self, sin_espacios=False):
        view = ''
        for letra in self.palabra:
            view += '{}{}'.format(letra, '' if sin_espacios else ' ')
        return view

    def jugar(self):
        # Mostrar la ayuda con los guiones
        view = 'Palabra: ' + self.interface()
        view += '           Vidas: {}'.format(self.vida)
        view += '   Riesgo: {}'.format(self.riesgo)
        view += '   Intentos: {}'.format(self.intentos)
        print(view)
        # Ingresar una letra
        letra = input('Ingrese una letra: ')
        if not letra in self.intentos:
            self.riesgo += 1
        # Verificar si esa letra pertenece a la palabra
        self.intentos.append(letra)
        resto_vida = True
        for objeto in self.palabra:
            if objeto.letra == letra:
                objeto.adivinada = True
                resto_vida = False
        if resto_vida:
            self.vida -= 1