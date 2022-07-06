    #r = Repository()
    #p1 = r.add_persona(Persona(apellido='Doe', nombre='John'))



class Persona:
    
    def __init__(self, apellido, nombre):
        self.nombre = nombre
        self.apellido = apellido

    """    
    @property
    def persona_id(self):
        return self.__persona_id


    @persona_id.setter
    def persona_id(self, value):
        self.__persona_id = value
    """


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value




    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, value):
        self.__apellido = value



    def __str__(self):
        return str(self.__apellido, self.__nombre)

