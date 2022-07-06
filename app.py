class Persona():
    def __init__(self, nombre='', apellido='', telefono=''):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def input(self):
        self.nombre = input("Ingrese Nombre: ")
        self.apellido = input("Ingrese Apellido: ")
        self.telefono = input("Ingrese Telefono: ")

    def __str__(self):
        return 'nombre: ' + self.nombre + ' apellido: ' + self.apellido + ' telefono:' + self.telefono

if __name__ == '__main__':
    persona = Persona('Florencia', 'Fernandez', '888')
    print('Persona')
    print(persona)
    persona2 = Persona()
    print('Persona2')
    print(persona2)
    persona3 = Persona(apellido='Cafiero')
    print(persona3)
