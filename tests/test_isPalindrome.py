import unittest
import sys
import os

# Add the parent directory to sys.path to import modules from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from isPalindrome import IsPalindrome


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.check_palindrome = IsPalindrome().two_pointers

    def test_empty_string(self):
        self.assertTrue(self.check_palindrome("") )

    def test_single_character(self):
        self.assertTrue(self.check_palindrome("a"))

    def test_valid_palindrome(self):
        # simple palindrome
        self.assertTrue(self.check_palindrome("racecar"))
        # palindrome with punctuation and mixed case
        self.assertTrue(self.check_palindrome("A man, a plan, a canal, Panama"))

    def test_invalid_palindrome(self):
        # non palindrome strings
        self.assertFalse(self.check_palindrome("hello"))
        self.assertFalse(self.check_palindrome("abc"))


if __name__ == "__main__":
    unittest.main()