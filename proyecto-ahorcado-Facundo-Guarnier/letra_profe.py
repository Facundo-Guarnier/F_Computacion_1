class Letra:
    def __init__(self, letra=''):
        self.letra = letra
        self.adivinada = False

    def __repr__(self):
        return self.letra if self.adivinada else '_'
