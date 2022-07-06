from Ahorcado_profe_POO import Ahorcado


class Juego:
    def __init__(self):
        self.ahorcado = Ahorcado()

    def iniciar(self):
        self.ahorcado.iniciar()

    def jugar(self):
        # hacer un bucle que juegue mientras nadie haya ganado o perdido
        while not self.ahorcado.ganado() and not self.ahorcado.perdido():
            self.ahorcado.jugar()


if __name__ == '__main__':
    juego = Juego()

    juego.iniciar()
    juego.jugar()