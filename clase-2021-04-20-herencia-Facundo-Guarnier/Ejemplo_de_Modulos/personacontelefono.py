from persona import Persona
from mail import Mail


class PersonaConTelefono(Persona):
    def __init__(self, nombre='', apellido='', edad=0, email=Mail('a@a.com'), telefonos=[]):
        super().__init__(nombre, apellido, edad, email)
        self.telefonos = telefonos

    @property
    def telefonos(self):
        return self.__telefonos

    @telefonos.setter
    def telefonos(self, value):
        self.__telefonos = value


if __name__ == '__main__':
    print('Estoy en Persona Con Telefono')
