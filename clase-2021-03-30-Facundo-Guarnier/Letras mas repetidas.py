import unittest

def count_letters(mi_palabra):
    exp_count_letters = {}                              #Cuenta cada letra
    for i in mi_palabra:
        exp_count_letters[i] = mi_palabra.count(i)      #hasta aca
    return exp_count_letters    




def mas_repetidas(mi_palabra):
    diccionario_cantidades = count_letters(mi_palabra)

    max_count = 0
    las_mas_repetidas = []

    for i in diccionario_cantidades.keys(): 
        
        cantidad_repetidas_letras = diccionario_cantidades[i]

        if cantidad_repetidas_letras > max_count:
            max_count = cantidad_repetidas_letras
            las_mas_repetidas = [i]

        elif cantidad_repetidas_letras == max_count:
            las_mas_repetidas.append(i)

    return las_mas_repetidas


class TestMasRepetidas(unittest.TestCase):
    def test_mas_repetidas(self):
        las_mas_repetidas = mas_repetidas('aaaBBBcccccddddd')
        self.assertTrue('c' in las_mas_repetidas)
        self.assertTrue('d' in las_mas_repetidas)
        self.assertFalse('a' in las_mas_repetidas)
        self.assertFalse('B' in las_mas_repetidas)



if __name__ == '__main__':
    unittest.main()
