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


if __name__ == '__main__':
    print('Estoy en Mail')
