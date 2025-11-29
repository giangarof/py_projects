import unittest
from challenges.challenge_3 import calculator


class Test(unittest.TestCase):

    def test_calculate_multiplication(self):
        """Calculate multiplication"""
        self.assertEqual(calculator(5, 5, "*"), 25)


    def test_calculate_division(self):
        """Calculate division"""
        self.assertEqual(calculator(8, 4, "/"), 2)


    def test_calculate_addition(self):
        """ Calcualte wrong addition """
        self.assertNotEqual(calculator(10, 10, "+"), 25)


    def test_calculate_substraction(self):
        """ Calculate wrong subtraction """
        self.assertNotEqual(calculator(10, 10, "-"), 5)


if __name__ == "__main__":
    unittest.main()