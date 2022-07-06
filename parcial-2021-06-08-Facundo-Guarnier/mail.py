class Mail:
    

    def __init__(self, email, tipo, email_id=None, persona_id=None):
        self.tipo = tipo
        self.email = email
        self.email_id = email_id
        self.persona_id = persona_id


    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value


    @property
    def persona_id(self):
        return self.__persona_id

    @persona_id.setter
    def persona_id(self, value):
        self.__persona_id = value


    @property
    def email_id(self):
        return self.__email_id

    @email_id.setter
    def email_id(self, value):
        self.__email_id = value




    def __str__(self):
        return self.__email_id, self.__email, self.__tipo, self.__persona_id