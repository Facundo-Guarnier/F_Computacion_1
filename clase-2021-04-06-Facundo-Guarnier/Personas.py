class Persona():
    def __init__(self, nombre='', apellido=''):
        self.nombre = nombre
        self.apellido = apellido
        self.telefonos = []  # lista de telefonos, inicialmente vacia
        self.email = []

    def agregar_telefono(self, telefono_nuevo):  # telefono_nuevo es un OBJETO de la clase Telefono
        self.telefonos.append(telefono_nuevo)  # agrego el telefono nuevo a la lista de telefonos de la Persona

    def agregar_email(self, email_nuevo):  
        self.email.append(email_nuevo)

    def __str__(self):
        return 'Nombre: ' + self.nombre + ', Apellido: ' + self.apellido



class Telefono():
    def __init__(self, tipo, area, numero, horario_atencion):
        self.tipo = tipo
        self.area = area
        self.numero = numero
        self.horario_atencion = horario_atencion
        
    def __str__(self):
        return "Telefono: \nTipo: " + self.tipo + " (" + self.area + ") " + self.numero + ", Horario atencion: " + self.horario_atencion


class Email():
    def __init__(self, tipo, direccion, propaganda):
        self.tipo = tipo
        self.direccion = direccion
        self.propaganda = propaganda

    def __str__(self):
        return "Email: \nTipo: " + self.tipo + ", Direccion: " + self.direccion + ", Acepta propagana: " + self.propaganda



if __name__ == '__main__':
    print("-------------------------")
    profe_daniel = Persona('Daniel', 'Quinteros')  # creo un objeto de la clase Persona
    el_telefono_personal_de_daniel = Telefono('personal', '261', '213421243', '9-18')  # creo un objeto de la clase Telefono
    el_telefono_laboral_de_daniel = Telefono('laboral', '261', '12341234', '10-16')  # creo un objeto de la clase Telefono
    el_email_de_daniel = Email("Personal", "daniel@gmail.com", "si")
    
    profe_daniel.agregar_telefono(el_telefono_personal_de_daniel)
    profe_daniel.agregar_telefono(el_telefono_laboral_de_daniel)
    profe_daniel.agregar_email(el_email_de_daniel)


    print(profe_daniel)
    print(profe_daniel.telefonos[0])
    print(profe_daniel.telefonos[1])
    print(profe_daniel.email[0])

    print("-------------------------")
    profe_gabriel = Persona('Gabriel', 'Flores')  # creo un objeto de la clase Persona
    profe_gabriel.agregar_telefono(el_telefono_laboral_de_daniel)
    profe_gabriel.agregar_email(Email("Laboral", "gabriel@um.edu.ar", "no"))
    
    print(profe_gabriel)
    print(profe_gabriel.telefonos[0])
    print(profe_gabriel.email[0])