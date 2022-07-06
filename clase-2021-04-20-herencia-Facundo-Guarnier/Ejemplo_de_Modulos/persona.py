from mail import Mail


class Persona:
    def __init__(self, nombre='', apellido='', edad=0, email=Mail('a@a.com')):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

    def __str__(self):
        return '{}, {} edad -> {} - email: {}'.format(self.apellido, self.nombre, self.edad, self.email)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value


if __name__ == '__main__':
    print('Estoy en Persona')
