# test_isAnagram.py
import unittest
from isAnagram import IsAnagram

class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.ia = IsAnagram()

    def test_sorting_empty(self):
        self.assertTrue(self.ia.sorting("", ""))

    def test_hashing_empty(self):
        self.assertTrue(self.ia.hashing("", ""))

    def test_sorting_anagram(self):
        self.assertTrue(self.ia.sorting("listen", "silent"))

    def test_hashing_anagram(self):
        self.assertTrue(self.ia.hashing("listen", "silent"))

    def test_sorting_non_anagram(self):
        self.assertFalse(self.ia.sorting("hello", "world"))

    def test_hashing_non_anagram(self):
        self.assertFalse(self.ia.hashing("hello", "world"))

    def test_sorting_diff_length(self):
        self.assertFalse(self.ia.sorting("hello", "helloo"))

    def test_hashing_diff_length(self):
        self.assertFalse(self.ia.hashing("hello", "helloo"))

if __name__ == '__main__':
    unittest.main()