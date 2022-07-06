class Persona:
    def __init__(self, documento=0, nombre=''):
        self.documento = documento
        self.nombre = nombre

    def __str__(self):
        return "{} - {}".format(self.documento, self.nombre)

    def input(self):
        self.documento = int(input("Ingrese documento: "))
        self.nombre = input("Ingrese nombre: ")

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, value):
        self.__documento = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value


if __name__ == '__main__':
    p = Persona()
    p.input()
    print(p)
