import unittest
from parameterized import parameterized

def reducir(numerador, denominador):
    
    if numerador == 0:
        return [0]

    elif denominador == 0:
        return "ERROR"

    elif (numerador % 11 == 0) and (denominador % 11 == 0):
        return reducir (numerador/11, denominador/11)

    elif (numerador % 7 == 0) and (denominador % 7 == 0):
        return reducir (numerador/7, denominador/7)

        
    elif (numerador % 5 == 0) and (denominador % 5 == 0):
        return reducir (numerador/5, denominador/5)

    elif (numerador % 3 == 0) and (denominador % 3 == 0):
        return reducir (numerador/3, denominador/3)  

    elif (numerador % 2 == 0) and (denominador % 2 == 0):
        return reducir (numerador/2, denominador/2)

    else:
        return [int(numerador), int(denominador)]



class TestReducir(unittest.TestCase):
    @parameterized.expand([(0, 5, [0]), (1, 4, [1, 4]), (-2, 5, [-2, 5]), (60, 20, [3, 1]), (80, 120, [2, 3])])
    def test_fibonacci_30(self, num, den, resultado):
        self.assertEqual(reducir(num, den), resultado)
        

if __name__ == '__main__':
    unittest.main()