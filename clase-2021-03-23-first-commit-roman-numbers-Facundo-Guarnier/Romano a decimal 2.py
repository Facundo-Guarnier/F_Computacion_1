import unittest    #Inicia los tests

romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_decimal(numero_romano):
    entero = 0
    for i in range(len(numero_romano)):
        if i > 0 and romanos[numero_romano[i]] > romanos[numero_romano[i - 1]]:
            entero += romanos[numero_romano[i]] - 2 * romanos[numero_romano[i - 1]]
        else:
            entero += romanos[numero_romano[i]]
        
    return entero


#Declaro los tests

class TestRomanToDecimal(unittest.TestCase):
    
    def test_roman_I(self):
        self.assertEqual(roman_to_decimal('I'), 1)          #Tipo 1 de test

    def test_roman_II(self):
        self.assertEqual(roman_to_decimal('II'), 2) 

    def test_roman_II(self):
        resultado = roman_to_decimal('III')                 #Tipo 2 de test
        self.assertEqual(resultado, 3)

    def test_roman_IV(self):
        self.assertTrue(roman_to_decimal("IV")==4)          #Tipo 3 de test (no estan recomendada, ya que no se cual es el numero del error)

    def test_roman_VIII(self):
        resultado = roman_to_decimal("VIII) 
        self.assertEqual(resultado, 8)

    def test_roman_IX(self):
        resultado = roman_to_decimal("IX") 
        self.assertEqual(resultado, 9)

    def test_roman_XL(self):
        resultado = roman_to_decimal("XL") 
        self.assertEqual(resultado, 40)

    def test_roman_XC(self):
        resultado = roman_to_decimal("XC") 
        self.assertEqual(resultado, 90)

    def test_roman_CD(self):
        resultado = roman_to_decimal("CD") 
        self.assertEqual(resultado, 400)

    def test_roman_CM(self):
        resultado = roman_to_decimal("CM") 
        self.assertEqual(resultado, 900)

    def test_roman_CMXCIX(self):
        resultado = roman_to_decimal("CMXCIX") 
        self.assertEqual(resultado, 999)

    def test_roman_MMMDCLXVI(self):
        resultado = roman_to_decimal("MMMDCLXVI") 
        self.assertEqual(resultado, 3666)

    def test_roman_CMXLIX(self):
        resultado = roman_to_decimal("CMXLIX") 
        self.assertEqual(resultado, 949)

    def test_roman_CDXLIV(self):
        resultado = roman_to_decimal("CDXLIV") 
        self.assertEqual(resultado, 444)

    def test_roman_MXLIX(self):
        resultado = roman_to_decimal("MXLIX") 
        self.assertEqual(resultado, 1049)


if __name__ == '__main__':
    unittest.main()




