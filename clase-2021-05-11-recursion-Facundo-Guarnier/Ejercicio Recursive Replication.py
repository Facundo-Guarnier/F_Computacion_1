import unittest
from parameterized import parameterized

def replicate(times, number, matriz = []):
    if times < 0:
        return (matriz)
    elif times == 0:
        matriz2 = matriz.copy()
        matriz.clear()
        return (matriz2)
        
    matriz.append(number)
    return replicate (times -1, number)



class TestReplicate(unittest.TestCase):
    @parameterized.expand([(0, 5, []), (1, 4, [4]), (2, 5, [5, 5]), (-2, 5, [])])
    def test_fibonacci_30(self, tiempo, numero, resultado):
        self.assertEqual(replicate(tiempo, numero), resultado)
        

if __name__ == '__main__':
    unittest.main()