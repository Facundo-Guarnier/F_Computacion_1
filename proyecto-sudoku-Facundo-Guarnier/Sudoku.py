import random
from time import sleep

class ErrorNumero(Exception):
    pass

class ErrorFila(Exception):
    pass

class ErrorColumna(Exception):
    pass

class ErrorNumBase(Exception):
    pass

class NumEnFila(Exception):
    pass

class NumEnColumna(Exception):
    pass

class ErrorSector(Exception):
    pass


class Sudoku():                                                             #A ARREGLAR: regla de sectores y test; test de la lista negra
    def __init__(self):                                                     #Test de 40 pares de cordenadas en lista negra
        self.tablero = [[" " for x in range(9)] for y in range(9)]  
        self.lista_negra = []


    def verificacion_inicial(self, fila, columna):
        return self.tablero[fila][columna]


    def verificacion_lista_negra(self, a, b):       #No es así pero como hago si son siempre numeros aleatorios.
        self.lista_negra = [[a, b]]                 #test_cambiar_num_base


    def numero_aleatorios(self):
        i = 0
        while i < 40:
            x = random.choice(range(9)) + 1
            y = random.choice(range(9)) + 1
            try:
                self.agregar_numero((random.choice(range(9)) + 1), x, y)
                self.lista_negra.append([x, y])
                i += 1

            except ErrorNumBase:
                pass

            except NumEnFila:
                pass

            except NumEnColumna:
                pass

            except ErrorSector:
                pass


    def agregar_numero(self, num, fila, columna):
        if (num - 1) not in (range(9)):
            raise ErrorNumero("----El numero no es entre 0 y 9----")   

        elif (fila - 1) not in (range(9)):
            raise ErrorFila("----La fila no es entre 0 y 9----")

        elif (columna - 1) not in (range(9)):
            raise ErrorColumna("----La columna no es entre 0 y 9----")
        
        elif [fila, columna] in self.lista_negra:
            raise ErrorNumBase("----No se puede modificar un numero ya dado----")    
        
        self.repeticion_fila(num, fila)         #LLamar a las 3 reglas cada una por separado.
        self.repeticion_columna(num, columna)
        self.repeticion_sector(num, fila, columna)

        self.tablero[fila-1][columna-1] = str(num)  #Si no se envio nunguna excepcion se carga el numero


    def repeticion_fila(self,num, fila):
        if str(num) in self.tablero[fila-1]:    #Analiza por la fila
            raise NumEnFila("----Ya está el numero en la fila----")


    def repeticion_columna(self, num, columna):
        for i in self.tablero:                  #Por cada fila se fija el mismo indice.
            if str(num) in i[columna-1]:
                raise NumEnColumna("----Ya está el numero en la columna----")


    def repeticion_sector(self, num, fila, columna):
        if fila in [1, 2, 3]:                   #Solo para el sector 1, no se como adaptarlo para los 9 sectores sin escribirlo 9 veces.
            i=0
            while i < 3:
                f = self.tablero[i]
                if (str(num) in f[1]) or (str(num) in f[2]) or (str(num) in f[2]):
                    raise ErrorSector("----Ya está el numero en el sector----")
                i+=1      





    # def repeticion_sector(self, num, fila, columna):
    #     region_fila = (fila-1)//3 
    #     region_columna = (columna-1)//3
    #     for r_row in range(3):
    #         for r_col in range(3):
    #             if(
    #             self.initial_board [region_fila*3+r_row] [region_columna*3+r_col] == num or
    #             self.user_board [region_fila*3+r_row] [region_columna*3+r_col]  == num
    #             ):
    #                 return False
    #     return True




    # def validate_col(self, col, value):
    #     for row in range(9):
    #         if (
    #             self.initial_board[row][col - 1] == value or
    #             self.user_board[row][col - 1] == value
    #         ):
    #             return False
    #     return True

    # def calculate_region(self, row, col):
    #     return tuple((
    #         (   int_row + ((row // 3) * 3),
    #             int_col + ((col // 3) * 3))
    #         for int_row in range(3)
    #         for int_col in range(3)
    #     ))

    # def validate_region(self, row, col, value):
    #     return not value in (
    #         self.user_board[i_row][i_col] + self.initial_board[i_row][i_col]
    #         for i_row, i_col in self.calculate_region(row - 1, col - 1)
    #     )





    def __str__(self):
        i = ""   
        for x in self.tablero:
            i += str(x) + "\n"
        return i


if __name__ == '__main__':
    juego1 = Sudoku()
    juego1.numero_aleatorios()
    print(juego1)
    while True:
        try:
            print("Esperando...")
            juego1.agregar_numero(int(input("Num: ")), int(input("Fila: ")), int(input("Columna: ")))
            print(juego1)

        except ErrorNumBase as e:
            print(e)

        except NumEnFila as e: 
            print(e)

        except NumEnColumna as e:
            print(e)

        except ErrorNumero as e:
            print(e)

        except ErrorFila as e:
            print(e)
        
        except ErrorColumna as e:
            print(e)

        except ErrorSector as e:
            print(e)
        
        except ValueError:
            print("----No se ingresó un numero----")