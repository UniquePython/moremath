import unittest
from moremath.arithmetic import add, subtract, multiply, divide, factorial

class TestArithmetic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertRaises(ValueError, add, "3", 4)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)
        self.assertRaises(ValueError, subtract, 10, "5")

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 5), 0)
        self.assertRaises(ValueError, multiply, 3, "4")

    def test_divide(self):
        self.assertEqual(divide(10, 3), 10/3)
        self.assertEqual(divide(-10, 3), -10/3)
        self.assertEqual(divide(0, 3), 0)
        self.assertRaises(ValueError, divide, 10, 0)
        self.assertRaises(ValueError, divide, 10, "3")

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertRaises(ValueError, factorial, -1)
        self.assertRaises(ValueError, factorial, "5")

if __name__ == '__main__':
    unittest.main()
