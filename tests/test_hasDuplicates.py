import unittest
import sys
import os

# Add the parent directory to sys.path to import modules from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../algo')))
from hasDuplicates import HasDuplicates

class TestHasDuplicates(unittest.TestCase):
    def setUp(self):
        self.hd = HasDuplicates()
        self.no_dup = [1, 2, 3, 4, 5]
        self.with_dup = [1, 2, 3, 2, 5]

    def test_brute_force_no_duplicates(self):
        self.assertFalse(self.hd.brute_force(self.no_dup))

    def test_brute_force_with_duplicates(self):
        self.assertTrue(self.hd.brute_force(self.with_dup))

    def test_sorting_no_duplicates(self):
        # Copy list because sorting modifies in place
        self.assertFalse(self.hd.sorting(self.no_dup.copy()))

    def test_sorting_with_duplicates(self):
        self.assertTrue(self.hd.sorting(self.with_dup.copy()))

    def test_hashing_no_duplicates(self):
        self.assertFalse(self.hd.hashing(self.no_dup))

    def test_hashing_with_duplicates(self):
        self.assertTrue(self.hd.hashing(self.with_dup))

    def test_hash_len_no_duplicates(self):
        self.assertFalse(self.hd.hash_len(self.no_dup))

    def test_hash_len_with_duplicates(self):
        self.assertTrue(self.hd.hash_len(self.with_dup))

if __name__ == '__main__':
    unittest.main()