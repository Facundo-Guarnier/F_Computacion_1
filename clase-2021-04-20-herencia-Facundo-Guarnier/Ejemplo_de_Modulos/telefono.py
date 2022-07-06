class Telefono:
    def __init__(self, numero=''):
        self.numero = numero

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value

    def __str__(self):
        return self.numero


if __name__ == '__main__':
    print('Estoy en Telefono')
