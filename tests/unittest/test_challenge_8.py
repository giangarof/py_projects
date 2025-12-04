import unittest
from challenges.challenge_8 import isPalindrome


class Test(unittest.TestCase):
    def test_isPalindrome_correct(self):
        """Return True if palindrome is correct"""

        self.assertTrue(isPalindrome('racecar'), True)

    def test_isPalindrome_incorrect(self):
        """Return False if palindrome is incorrect"""
        self.assertFalse(isPalindrome("dog"), False)


if __name__ == "__main__":
    unittest.main()
