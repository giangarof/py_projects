import unittest
from challenges.challenge_2 import getSum


class Test(unittest.TestCase):
    def test_getsum_correct(self):
        """getSum must return the right addition"""
        self.assertEqual(getSum(5, 5), 10)
        self.assertEqual(getSum(1, 1), 2)
        self.assertEqual(getSum(7, 7), 14)

    def test__getsum_incorrect(self):
        """getSum must return the incorrect addition"""
        self.assertNotEqual(getSum(5, 5), 11)
        self.assertNotEqual(getSum(5, 10), 5)


if __name__ == "__main__":
    unittest.main()
