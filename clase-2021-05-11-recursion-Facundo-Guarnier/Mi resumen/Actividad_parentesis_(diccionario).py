import unittest             #Con diccionario

class ErrorImpar(Exception):
    pass

class ErrorNoSonIguales(Exception):
    pass

class ErrorHayOtroElemento(Exception):
    pass


class Ejercicio():
    def __init__(self, oracion):
        self.oracion = oracion

    @property
    def oracion(self):
        return self.__oracion

    @oracion.setter
    def oracion(self, value):
        self.__oracion = []
        for i in value:
            self.__oracion.append(i)
        

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, value):
        self.__resultado = value


    def resolver(self):
        diccionario1 = {"(": ")", "[": "]", "{": "}"}
        resultado = []
        preresultado = []



        if len(self.__oracion) % 2 != 0:
            self.__resultado = False
            raise ErrorImpar("No hay la misma cantidad de abierto y cerrado")       #Par o impar


        for i in range(int(len(self.__oracion)/2)):                                 #Verifica que todos los elementos de "abrir" que esten en el diccionario (claves)
            if False == (self.__oracion[i] in diccionario1):                        
                self.__resultado = False
                raise ErrorHayOtroElemento("Hay un numero/letra/signo en el 'abierto'")             #No esta en la claves


        for i in range(int(len(self.__oracion)/2)):                                 #Primeros elementos copiados de la oracion inicial.
            resultado.append(self.__oracion[i])    


        for i in range(int(len(self.__oracion)/2)):                                 #Verificar los "cierre" si no son numeros u otro.
            if False == (self.__oracion[i + int(len(self.__oracion)/2)] in diccionario1.values()):                        
                self.__resultado = False
                raise ErrorHayOtroElemento("Hay un numero/letra/signo en el 'cerrado'")


        for i in range(int(len(self.__oracion)/2)):                                 #Ultimos elementos, con la clave del diccionario a su valor.
            preresultado.append(diccionario1[self.__oracion[i]])


        for i in range(len(preresultado) - 1, int(-1), -1):                         #Agrega al resultado el preresultado de final al comienzo.
            resultado.append(preresultado[i])


        if self.__oracion == resultado:
            self.__resultado = True


        else:
            print(self.__oracion)
            print(resultado)
            self.__resultado = False
            raise ErrorNoSonIguales ("No son iguales")



    def __str__(self):
        return str(self.__resultado)


class TestGeneral(unittest.TestCase):
    
    def test_facil_1_bien(self):
        actividad = Ejercicio("([[{{{[]}}}]])")
        actividad.resolver()
        self.assertEqual(actividad.resultado, True)

    def test_facil_impar_facil(self):
        actividad = Ejercicio(")")
        with self.assertRaises(ErrorImpar):
            actividad.resolver()
        self.assertEqual(actividad.resultado, False)

    def test_facil_impar_dificil(self):
        actividad = Ejercicio("([{[[{[)]}]]}])")
        with self.assertRaises(ErrorImpar):
            actividad.resolver()
        self.assertEqual(actividad.resultado, False)

    def test_otro_elemento_al_abrir(self):
        actividad = Ejercicio("((((5)))))")
        with self.assertRaises(ErrorHayOtroElemento):
            actividad.resolver()
        self.assertEqual(actividad.resultado, False)

    def test_otro_elemento_al_cerrar(self):
        actividad = Ejercicio("(((()5))")
        with self.assertRaises(ErrorHayOtroElemento):
            actividad.resolver()
        self.assertEqual(actividad.resultado, False)



if __name__ == "__main__":

    try:
        actividad1 = Ejercicio("[(((([[[[]]]))))5]")
        actividad1.resolver()
        print(actividad1)
    except ErrorImpar as e:
        print(e)
        print(actividad1.resultado)
    except ErrorNoSonIguales as e:
        print(e)
        print(actividad1.resultado)
    except ErrorHayOtroElemento as e:
        print(e)
        print(actividad1.resultado)

    
    unittest.main()