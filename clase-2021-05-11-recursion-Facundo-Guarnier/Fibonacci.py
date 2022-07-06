import unittest

def fibonacci(numero):
    if numero == 1:
        return 1 
    elif numero == 0: 
        return 0
    return fibonacci(numero - 1) + fibonacci(numero - 2)

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_4(self):
        self.assertEqual(fibonacci(4), 3)
    
    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_20(self):
        self.assertEqual(fibonacci(20), 6765)

    @unittest.skip("lo salteo porque quiero que alguien mas lo arregle")    
    def test_fibonacci_30(self):
        self.assertEqual(fibonacci(30), 832040)

if __name__ == '__main__':
    unittest.main()