from persona import Persona
from mail import Mail


class Repository:

    def __init__(self):
        self.persona = {}
        self.email = {}
        self.persona_id = 0
        self.email_id = 0
        

    @property
    def persona(self):
        return self.__persona


    @persona.setter
    def persona(self, value):
        self.__persona = value
    



    @property
    def persona_id(self):
        return self.__persona_id


    @persona_id.setter
    def persona_id(self, value):
        self.__persona_id = value



    def add_persona(self, value):                       #Se ingresa la instancia de persona con clave persona_id
        self.__persona_id += 1
        self.__persona[self.__persona_id] = value





    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self, value):
        self.__email = value



    @property
    def email_id(self):
        return self.__email_id


    @email_id.setter
    def email_id(self, value):
        self.__email_id = value




    def add_mail(self, value):
        self.__email_id += 1
        self.__email[self.__email_id] = value




    def to_string(self, email_id=False, persona_id=False):
        if email_id == False:
            return self.__persona[persona_id]
        else:
            return self.__email[email_id]


