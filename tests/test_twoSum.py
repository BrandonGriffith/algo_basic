import unittest
import sys
import os

# Add the parent directory to sys.path to import modules from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from twoSum import TwoSum

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.two_sum = TwoSum()

    def test_brute_force_found(self):
        # Test brute_force method with a valid sum
        arr = [2, 7, 11, 15]
        target = 9
        result = self.two_sum.brute_force(arr, target)
        # expecting indices [0, 1]
        self.assertEqual(result, [0, 1])

    def test_hashing_found(self):
        # Test hashing method with a valid sum
        arr = [3, 2, 4]
        target = 6
        result = self.two_sum.hashing(arr, target)
        # expecting indices [1, 2] because 2+4=6
        self.assertEqual(result, [1, 2])

    def test_no_solution(self):
        # When no two numbers add up to the target, functions should return None.
        arr = [1, 2, 3]
        target = 7
        result_brute = self.two_sum.brute_force(arr, target)
        result_hash = self.two_sum.hashing(arr, target)
        self.assertIsNone(result_brute)
        self.assertIsNone(result_hash)

if __name__ == '__main__':
    unittest.main()