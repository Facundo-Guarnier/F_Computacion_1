import unittest

decimales = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def DecimalRomano(numero):
    resultado = ""
    n = 0

    while numero > 0 and n != len(decimales):
        if ((numero//decimales[n]) == 0):
            pass
        elif (numero // decimales[n]) <= 3 and (numero // decimales[n]) >= 1:
            for j in range((numero // decimales[n])):
                resultado += romanos[n]
                numero -= decimales[n]
        n += 1

    return resultado


class TestDecimalARomano(unittest.TestCase):
    
    def test_decimal_1(self):
        self.assertEqual(DecimalRomano(1), "I")    

    def test_decimal_3(self):
        self.assertEqual(DecimalRomano(3), "III")
    
    def test_decimal_4(self):
        self.assertEqual(DecimalRomano(4), "IV")

    def test_decimal_5(self):
        self.assertEqual(DecimalRomano(5), "V")

    def test_decimal_8(self):
        self.assertEqual(DecimalRomano(8), "VIII")

    def test_decimal_9(self):
        self.assertEqual(DecimalRomano(9), "IX")

    def test_decimal_10(self):
        self.assertEqual(DecimalRomano(10), "X")

    def test_decimal_40(self):
        self.assertEqual(DecimalRomano(40), "XL")

    def test_decimal_50(self):
        self.assertEqual(DecimalRomano(50), "L")

    def test_decimal_80(self):
        self.assertEqual(DecimalRomano(80), "LXXX")

    def test_decimal_90(self):
        self.assertEqual(DecimalRomano(90), "XC")

    def test_decimal_400(self):
        self.assertEqual(DecimalRomano(400), "CD")
        
    def test_decimal_500(self):
        self.assertEqual(DecimalRomano(500), "D")

    def test_decimal_800(self):
        self.assertEqual(DecimalRomano(800), "DCCC")

    def test_decimal_900(self):
        self.assertEqual(DecimalRomano(900), "CM")

    def test_decimal_1000(self):
        self.assertEqual(DecimalRomano(1000), "M")

    def test_decimal_459(self):
        self.assertEqual(DecimalRomano(459), "CDLIX")

    def test_decimal_66(self):
        self.assertEqual(DecimalRomano(66), "LXVI")

    def test_decimal_765(self):
        self.assertEqual(DecimalRomano(765), "DCCLXV")

    def test_decimal_411(self):
        self.assertEqual(DecimalRomano(411), "CDXI")



if __name__ == '__main__':
    unittest.main()
