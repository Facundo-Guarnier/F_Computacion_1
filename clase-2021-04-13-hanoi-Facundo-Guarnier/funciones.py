class Mail:
    def __init__(self, email=''):
        self.email = email
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
    
    def __str__(self):
        return self.email


class Persona:
    def __init__(self, nombre='', apellido='', telefonos=[], edad=0, email=Mail('a@a.com')):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefonos = telefonos
        self.email = email
    
    def __str__(self):
        return '{}, {} edad -> {} - email: {}'.format(self.apellido, self.nombre, self.edad, self.email)
    
    def add_telefono(self, t):
        self.telefonos.append(t)
    
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
    
    @property
    def telefonos(self):
        return self.__telefonos
    
    @telefonos.setter
    def telefonos(self, value):
        self.__telefonos = value



class Telefono:
    def __init__(self, numero=''):
        self.numero = numero
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, value):
        self.__numero = value




if __name__ == '__main__':
    p = Persona('Juan', 'Perez', edad=18)
    p.add_telefono(Telefono('234567'))
    print(p)
    print(p.__dict__)