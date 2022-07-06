from persona import Persona


class Interfaz:
    def __init__(self):
        pass

    def input(self):
        print('\n    Ingreso de Persona')
        documento = int(input('\nDocumento: '))
        nombre = input('Nombre: ')
        return Persona(documento, nombre)

    def show(self, persona):
        print('\n    Persona encontrada')
        print('\n\n Documento: {}\n Nombre: {}\n'.format(
            persona.documento, persona.nombre))
