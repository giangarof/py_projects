import unittest
from py_projects.challenges.challenge_04 import countOccurrences


class Test(unittest.TestCase):
    def test_countOccurrences_correct(self):
        """ count occurrences for 'l' in 'hello world' """
        self.assertEqual(countOccurrences('l','hello world'), 3)

    def test_countOccurrences_incorrect(self):
        """ count occurrences for 'w' in 'world wide web' """
        self.assertNotEqual(countOccurrences("w", "world wide web"), 4)


if __name__ == "__main__":
    unittest.main()
