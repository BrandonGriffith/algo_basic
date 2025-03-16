import unittest
import sys
import os

# Add the parent directory to sys.path to import modules from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from maxProfit import MaxProfit

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.max_profit = MaxProfit()

    def test_two_pointers_standard_case(self):
        # Test with a standard increasing and decreasing prices
        prices = [7, 1, 5, 3, 6, 4]
        result = self.max_profit.two_pointers(prices)
        # expecting 5 (buy at 1, sell at 6)
        self.assertEqual(result, 5)

    def test_max_min_standard_case(self):
        # Test with a standard increasing and decreasing prices
        prices = [7, 1, 5, 3, 6, 4]
        result = self.max_profit.max_min(prices)
        # expecting 5 (buy at 1, sell at 6)
        self.assertEqual(result, 5)

    def test_two_pointers_decreasing_prices(self):
        # Test with prices that only decrease
        prices = [7, 6, 5, 4, 3, 2, 1]
        result = self.max_profit.two_pointers(prices)
        # expecting 0 (no profit possible)
        self.assertEqual(result, 0)

    def test_max_min_decreasing_prices(self):
        # Test with prices that only decrease
        prices = [7, 6, 5, 4, 3, 2, 1]
        result = self.max_profit.max_min(prices)
        # expecting 0 (no profit possible)
        self.assertEqual(result, 0)

    def test_two_pointers_single_price(self):
        # Test with only one price
        prices = [5]
        result = self.max_profit.two_pointers(prices)
        # expecting 0 (can't buy and sell with one price)
        self.assertEqual(result, 0)

    def test_max_min_single_price(self):
        # Test with only one price
        prices = [5]
        result = self.max_profit.max_min(prices)
        # expecting 0 (can't buy and sell with one price)
        self.assertEqual(result, 0)

    def test_two_pointers_multiple_peaks(self):
        # Test with multiple peaks and valleys
        prices = [3, 2, 6, 5, 0, 3]
        result = self.max_profit.two_pointers(prices)
        # expecting 4 (buy at 2, sell at 6)
        self.assertEqual(result, 4)

    def test_max_min_multiple_peaks(self):
        # Test with multiple peaks and valleys
        prices = [3, 2, 6, 5, 0, 3]
        result = self.max_profit.max_min(prices)
        # expecting 4 (buy at 2, sell at 6)
        self.assertEqual(result, 4)

    def test_two_pointers_empty_array(self):
        # Test with an empty array
        prices = []
        result = self.max_profit.two_pointers(prices)
        # Expect 0 for an empty array
        self.assertEqual(result, 0)

    def test_max_min_empty_array(self):
        # Test with an empty array - now properly handled in the implementation
        prices = []
        result = self.max_profit.max_min(prices)
        # Expect 0 for an empty array
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()