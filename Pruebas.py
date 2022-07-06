    """
    def jugar(self):
        while self.ganador == False:
            print(self)
            enttradas = [0, 1, 2]
            torre_origen = ""
            torre_destino = ""

            while not (torre_destino in enttradas) or not (torre_origen in enttradas):
                try: 
                    torre_origen = int(input('Torre origen: (0, 1, 2):'))
                    torre_destino = int(input('Torre destino: (0, 1, 2):'))
                    if not (torre_destino in enttradas) or not (torre_origen in enttradas):
                        print("\n----Caracter fuera de los limites----\n")
                except:
                    print("\n----Caracter inválido----\n")
                    torre_destino, torre_origen = "", ""
                    
            self.mover(torre_origen, torre_destino)
    """


    """

    def jugar(self):
        while self.ganador == False:
            print(self)
            enttradas = [0, 1, 2]
            torre_origen = ""
            torre_destino = ""
            try: 
                torre_origen = int(input('Torre origen: (0, 1, 2):'))
                torre_destino = int(input('Torre destino: (0, 1, 2):'))
                if not(torre_destino in enttradas) or not(torre_origen in enttradas):
                    print("\n----Caracter fuera de los limites----\n")
                    torre_origen, torre_destino = "", ""
                    quit()
            except:
                print("\n----Caracter inválido----\n")
                quit() 
                    
            self.mover(torre_origen, torre_destino)

    """



    """
    def mover(self, torre_origen, torre_destino):
        
        if len(self.torres[torre_destino].discos_apilados) > 0:                     #Si el destino tiene discos
            disco_que_voy_a_sacar = self.torres[torre_origen].discos_apilados[-1]       
            ultimo_disco_del_destino = self.torres[torre_destino].discos_apilados[-1]
            
            if disco_que_voy_a_sacar.tamano > ultimo_disco_del_destino.tamano:      #Ver tamaños.
                print("\n----El disco origen es mas grande que el destino, no se puede----")
                return
        
        if len(self.torres[torre_origen].discos_apilados) > 0:                      #Ver si la torre origen tiene discos
            disco_sacado = self.torres[torre_origen].discos_apilados.pop()          #Saco de la torre de origen
            self.torres[torre_destino].discos_apilados.append(disco_sacado)         #Pongo la torre de destino
        else:
            print ("\n----La torre de origen no tiene discos----")
            return

        if len(self.torres[2].discos_apilados) == 6 or len(self.torres[1].discos_apilados) == 6: 
            self.ganador = True
            print("***************\n  ¡¡GANASTE!!  \n***************")
            quit()
    """



