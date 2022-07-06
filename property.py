class EMail:
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
    def __init__(self, nombre='', apellido='', telefonos=[], edad=0, email=EMail('a@a.com')):    #Estoy creando un objeto EMail
        self.nombre = nombre                    #Llama a la funcion @nombre.setter 
        self.apellido = apellido
        self.edad = edad
        self.telefonos = telefonos
        self.email = email

    
    def __str__(self):                                  #Esto es para cuando no usamos @property
        return ("Apellido: " + self.apellido + "\n" +
            "Nombre: " + self.nombre + "\n" +
            "Edad: " + str(self.edad) + "\n" +
            "Email: " + str(self.email) + "\n")
    

    def add_telefono(self, t):
        self.telefonos.append(t)
    
    @property                           #Seria mi getter de un atributo (devuelve el valor)
    def nombre(self):                   
        return self.__nombre            #Este seria el nombre del atributo
    
    @nombre.setter                      #Seria mi setter, define el atributo y su valor
    def nombre(self, value):
        #If x < Y: etc....              #Se pueden poner condiciones, de la otra forma hay que escribirla cada vez que se ingresa un nombre
        self.__nombre = value

    @property
    def apellido(self):
        return self.__nombre
    
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value
    
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
    persona1 = Persona('Juan', 'Perez', edad=18)
    persona1.add_telefono(Telefono('234567'))
    print(persona1)
    print(persona1.__dict__)            #imprime un diccionario con todos los atribucos y sus valores del constructor, o bien si ya se llamo a otro atributo extra.