import unittest


def count_letters(mi_palabra):
    exp_count_letters = {}
    for i in mi_palabra:
        exp_count_letters[i] = mi_palabra.count(i)

    return exp_count_letters


class TestLetterCount(unittest.TestCase):
    
    def test_count1(self):
        exp_count_letters = count_letters('hola mundo')
        self.assertEqual(exp_count_letters['h'], 1)
        self.assertEqual(exp_count_letters['o'], 2)
        self.assertEqual(exp_count_letters['l'], 1)
        self.assertEqual(exp_count_letters['a'], 1)
        self.assertEqual(exp_count_letters['m'], 1)
        self.assertEqual(exp_count_letters['u'], 1)
        self.assertEqual(exp_count_letters['n'], 1)
        self.assertEqual(exp_count_letters['d'], 1)

    def test_count2(self):
        exp_count_letters = count_letters('computacion')
        self.assertEqual(exp_count_letters['c'], 2)
        self.assertEqual(exp_count_letters['o'], 2)
        self.assertEqual(exp_count_letters['m'], 1)
        self.assertEqual(exp_count_letters['p'], 1)
        self.assertEqual(exp_count_letters['u'], 1)
        self.assertEqual(exp_count_letters['t'], 1)
        self.assertEqual(exp_count_letters['a'], 1)
        self.assertEqual(exp_count_letters['i'], 1)
        self.assertEqual(exp_count_letters['n'], 1)

    def test_count3(self):
        exp_count_letters = count_letters('abcdabcdabcde')
        self.assertEqual(exp_count_letters['a'], 3)
        self.assertEqual(exp_count_letters['b'], 3)
        self.assertEqual(exp_count_letters['c'], 3)
        self.assertEqual(exp_count_letters['d'], 3)
        self.assertEqual(exp_count_letters['e'], 1)

    def test_count4(self):
        exp_count_letters = count_letters('a!b?¿!!')
        self.assertEqual(exp_count_letters['a'], 1)
        self.assertEqual(exp_count_letters['!'], 3)
        self.assertEqual(exp_count_letters['b'], 1)
        self.assertEqual(exp_count_letters['¿'], 1)
        self.assertEqual(exp_count_letters['?'], 1)



if __name__ == '__main__':
    unittest.main()

