class Juego:
    def __init__(self):                             #Constructor (definir los atributos)
        self.torres = []
        torre_izq = Torre('Izquierda')              #Ejecuta el constructor
        disco_6 = Disco(6)
        torre_izq.discos_apilados.append(disco_6)   #Al atributo "discos apilados" le agrego disco 6
        disco_5 = Disco(5)
        torre_izq.discos_apilados.append(disco_5)
        disco_4 = Disco(4)
        torre_izq.discos_apilados.append(disco_4)
        disco_3 = Disco(3)
        torre_izq.discos_apilados.append(disco_3)
        disco_2 = Disco(2)
        torre_izq.discos_apilados.append(disco_2)
        disco_1 = Disco(1)
        torre_izq.discos_apilados.append(disco_1)
        self.torres.append(torre_izq)

        torre_cen = Torre('Central')                # ejecuta el constructor
        self.torres.append(torre_cen)

        torre_der = Torre('Derecha')                # ejecuta el constructor
        self.torres.append(torre_der)

        self.ganador = False

        self.intentos = 0

    def mover(self, torre_origen, torre_destino):
        
        rango = [0, 1, 2]

        if (torre_destino in rango) and (torre_origen in rango):                         #Contralar indices mayo a 2 y menor a 0.
            if len(self.torres[torre_origen].discos_apilados) != 0:                         #Si el origen tiene discos.
                if len(self.torres[torre_destino].discos_apilados) != 0:                    #Si el destino tiene discos.
                    disco_que_voy_a_sacar = self.torres[torre_origen].discos_apilados[-1]       
                    ultimo_disco_del_destino = self.torres[torre_destino].discos_apilados[-1]
                    
                    if disco_que_voy_a_sacar.tamano > ultimo_disco_del_destino.tamano:      #Si el destino es mas grande. 
                        print("\n----El disco origen es mas grande que el destino----")
                        return
                    else:
                        disco_sacado = self.torres[torre_origen].discos_apilados.pop()                  #Saco de la torre de origen
                        self.torres[torre_destino].discos_apilados.append(disco_sacado)                 #Pongo la torre de destino
                else:
                    disco_sacado = self.torres[torre_origen].discos_apilados.pop()                  
                    self.torres[torre_destino].discos_apilados.append(disco_sacado)


            else:                                                                       #Si NO tiene disco el origen.
                print("\n----El origen no tiene discos----")
                return
            
        else: 
            print("\n----El indice está fuera del limite----")
            return
        
        self.intentos += 1

        if len(self.torres[2].discos_apilados) == 6 or len(self.torres[1].discos_apilados) == 6: 
            self.ganador = True
            print("***************\n  ¡¡GANASTE!!  \n***************")
            quit()

    def jugar(self):
        while self.ganador == False:
            print(self)
            try:
                torre_origen = int(input('Torre origen: (0, 1, 2):'))
                torre_destino = int(input('Torre destino: (0, 1, 2):'))
            except:
                print("\n----Caracter no valido----")
                torre_origen, torre_destino = False, False
                pass

            if torre_destino == False:
                pass
            else:
                self.mover(torre_origen, torre_destino)

    def __str__(self):
        return "\nIntento N°:" + str(self.intentos) + "\n   " + '\n   '.join([str(torre) for torre in self.torres])


class Torre:
    def __init__(self, ubicacion):  # constructor
        self.ubicacion = ubicacion
        self.discos_apilados = []

    def __str__(self):
        return "> " + self.ubicacion + ": " + ','.join([str(disco) for disco in self.discos_apilados])


class Disco:
    def __init__(self, tamano):
        self.tamano = tamano

    def __str__(self):
        return str(self.tamano)



if __name__ == '__main__':
    mi_juego = Juego()          #Ejecuta el constructor
    mi_juego.jugar()