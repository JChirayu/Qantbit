import unittest

def factorial(n):
    result = 1
    if not isinstance(n, int):
        raise TypeError('Input is not an integer')
    
    if n<0:
        raise ValueError('Input must not be a negative number')
    
    if n == 0 or n == 1:
        return 1
    
    for i in range(2, n+1):
        result *= i
    return result

class Check(unittest.TestCase):
    
    def test_forZero(self):
        self.assertEqual(factorial(0),1)

    def test_forOne(self):
        self.assertEqual(factorial(1),1)

    def test_forPositive(self):
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_forNegative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

    def test_forNonInteger(self):
        with self.assertRaises(TypeError):
            factorial(4.5)
        with self.assertRaises(TypeError):
            factorial('string')


unittest.main()