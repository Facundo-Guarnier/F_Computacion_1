"""
    Consigna:
        Agregar la funcionalidad de sumar teléfonos a la persona.
        Agregar la funcionalidad de poder usar print(persona) y que me muestre la lista de atributos de la persona 
        incluyendo la lista de teléfonos que le pertenecen teniendo en cuenta las responsabilidades de las clases.
"""



class Persona:
    def __init__(self, nombre='', apellido=''):
        self.nombre = nombre
        self.apellido = apellido
        self.telefonos = []


    def agregar_telefono(self, telefono_nuevo):
        self.telefonos.append(telefono_nuevo)


    def __str__(self):
        telefono_str = ""
        for i in self.telefonos:
            telefono_str += i.__str__()

        return self.nombre + " " + self.apellido + ", Telefonos: " + telefono_str



class Telefono():
    def __init__(self, tipo, numero):
        self.tipo = tipo
        self.numero = numero
        
    def __str__(self):
        return "\nTipo: " + self.tipo + ", Numero: " + self.numero 



if __name__ == '__main__':

    persona1 = Persona('Juan', 'Perez')

    persona1.agregar_telefono(Telefono("Personal", "261 5648741"))
    persona1.agregar_telefono(Telefono("Fijo", "261 9635458"))

    print(persona1)














