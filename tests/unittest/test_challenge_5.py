import unittest
from py_projects.challenges.challenge_05 import findMaxNumber

class Test(unittest.TestCase):
    def test_findMaxNumber_correct(self):
        """Return the greatest number of a list"""
        nums = [1,2,3,50,55,40,30,20]
        self.assertEqual(findMaxNumber([1, 2, 3, 50, 55, 40, 30, 20]), 55)

    def test_findMaxNumber_incorrect(self):
        """Return the greatest number of a list"""
        nums = [1, 2, 3, 50, 55, 40, 30, 20]
        self.assertNotEqual(findMaxNumber([1, 2, 3, 50, 55, 40, 30, 20]), 20)


if __name__ == "__main__":
    unittest.main()
