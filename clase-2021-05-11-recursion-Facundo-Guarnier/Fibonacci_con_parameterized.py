import unittest
from parameterized import parameterized

def fibonacci(numero):
    if numero == 1:
        return 1 
    elif numero == 0: 
        return 0
    return fibonacci(numero - 1) + fibonacci(numero - 2)


class TestFibonacci(unittest.TestCase):
    @parameterized.expand([(0, 0), (1, 1), (2, 1), (4, 3), (10, 55)])
    def test_fibonacci_30(self, numero, resultado):
        self.assertEqual(fibonacci(numero), resultado)

if __name__ == '__main__':
    unittest.main()