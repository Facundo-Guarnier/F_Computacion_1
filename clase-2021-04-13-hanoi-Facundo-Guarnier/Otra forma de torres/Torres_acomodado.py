class GameOverException(Exception):
    pass


class ErrorHumanoException(Exception):
    pass


class Juego:
    def __init__(self): 
        self.torres = []
        torre_izq = Torre('Izquierda')                      
        disco_6 = Disco(6)  
        torre_izq.discos_apilados.append(disco_6)
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
        torre_cen = Torre('Central') 
        self.torres.append(torre_cen)
        torre_der = Torre('Derecha') 
        self.torres.append(torre_der)

    def mover(self, torre_origen, torre_destino):
        print('moviendo {} -> {}'.format(torre_origen, torre_destino))

        if torre_origen < 0 or torre_origen > 2:                                            #Numero no valido
            raise ErrorHumanoException('La torre origen tiene que ser entre 0 y 2')         #Lanza/envia la excepcion 

        if torre_destino < 0 or torre_destino > 2:                                          #Numero no valido
            raise ErrorHumanoException('La torre destino tiene que ser entre 0 y 2')

        if torre_origen == torre_destino:                                                   #Torre destino distinta a la origen
            raise ErrorHumanoException('La torres tienen que ser distintas')

        if len(self.torres[torre_origen].discos_apilados) == 0:                             #Si el origen tiene discos
            raise ErrorHumanoException('La torre de origen esta vacia')

        if len(self.torres[torre_destino].discos_apilados) > 0:                             #Comopara el tamaño de los discos
            disco_que_voy_a_sacar = self.torres[torre_origen].discos_apilados[-1]
            ultimo_disco_del_destino = self.torres[torre_destino].discos_apilados[-1]
            if disco_que_voy_a_sacar.tamano > ultimo_disco_del_destino.tamano:
                raise ErrorHumanoException("El disco origen es mas grande que el destino, no se puede")

        
        disco_sacado = self.torres[torre_origen].discos_apilados.pop()                  #Saco de la torre de origen
        self.torres[torre_destino].discos_apilados.append(disco_sacado)                 #Pongo la torre de destino
        
        if len(self.torres[0].discos_apilados) == 0 and len(self.torres[1].discos_apilados) == 0:
            raise GameOverException('GAME OVER')                                        #GANE!!!! Lanzar exception para termina partida

    def __str__(self):
        #return ' aaaaaa,'.join([str(torre) for torre in self.torres])                   #Muestra el estado de las torres
        return  "     >" + '\n     >'.join([str(torre) for torre in self.torres])

class Torre:
    def __init__(self, ubicacion):  # constructor
        self.ubicacion = ubicacion
        self.discos_apilados = []

    def __str__(self):
        return self.ubicacion + "::" + ','.join([str(disco) for disco in self.discos_apilados])


class Disco:
    def __init__(self, tamano):
        self.tamano = tamano

    def __str__(self):
        return str(self.tamano)

import pygame
from pygame.locals import *

from pygame.rect import *
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

class Juego2d(Juego):

    def jugar(self):
        pygame.init()
        size = 600, 620  # ancho, alto
        width, height = size
        screen = pygame.display.set_mode(size)
        pygame.display.update()
        torres_rect = []
        for torre_index, torre in enumerate(self.torres):
            torres_rect.append(Rect(torre_index * 200, 0, 199, 600))
        running = True
        selecting = None
        font = pygame.font.SysFont(None, 24)
        message = ''
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == MOUSEBUTTONDOWN:
                    for torre_index, rect in enumerate(torres_rect):
                        if rect.collidepoint(event.pos):
                            if selecting is None:
                                selecting = torre_index
                            elif selecting == torre_index:
                                selecting = None
                            else:
                                try:
                                    self.mover(selecting, torre_index)
                                    selecting = None
                                except ErrorHumanoException as error:
                                    message = str(error)
                                except GameOverException:
                                    running = False

            screen.fill(GRAY)
            # pygame.draw.rect(screen, BLACK, base)
            for torre_index, rect in enumerate(torres_rect):
                if selecting is not None and selecting == torre_index:
                    pygame.draw.rect(screen, GRAY, rect)
                else:
                    pygame.draw.rect(screen, BLACK, rect)

            img = font.render(message, True, BLUE)
            screen.blit(img, (20, 603))
            for torre_index, torre in enumerate(self.torres):
                for disco_index, disco in enumerate(torre.discos_apilados):
                    disco_ancho = 30 * disco.tamano
                    rect = Rect(
                        100 + (torre_index * 200) - (disco_ancho // 2),
                        400 - (disco_index * 50),
                        disco_ancho,
                        30,
                    )
                    pygame.draw.rect(screen, BLUE, rect)

            pygame.display.flip()
        pygame.quit()


class JuegoLineaDeCommando(Juego):
    def jugar(self):
        while True:
            print(self)                                                                 #Muestra el estado de las torres
            torre_origen = 9999
            while torre_origen == 9999:
                torre_origen_string = input('Torre origen: (0, 1, 2):')
                try:
                    torre_origen = int(torre_origen_string)
                except ValueError:                                                      #Indico que es un error de valor int, str
                    print('El numero no es valido, por favor de 0 a 2')

            torre_destino = 9999
            while torre_destino == 9999:
                torre_destino_string = input('Torre destino: (0, 1, 2):')
                try:
                    torre_destino = int(torre_destino_string)
                except ValueError:
                    print('El numero no es valido, por favor de 0 a 2')

            try:
                self.mover(torre_origen, torre_destino)                                 # puede fallar... PUEDE LANZAR UNA EXCEPTION
            except GameOverException:                                                   #Recive la excepcion
                print('GANE!!!!')
                break
            except ErrorHumanoException as error:
                print('UPS!! ERROR: ' + str(error))



if __name__ == '__main__':
    """
    game_mode = input('select 2d or CL:')
    
    if game_mode == "2d":
        mi_juego = Juego2d()  # ejecuta el constructor
    else: 
        mi_juego = JuegoLineaDeCommando()  # ejecuta el constructor
    mi_juego.jugar()
    """
    mi_juego = JuegoLineaDeCommando()
    mi_juego.jugar()