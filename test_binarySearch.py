import unittest

from binarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def test_iterative_found(self):
        # Test iterative search with a target that exists in the array
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 6
        result = BinarySearch.iterativeBinarySearch(arr, target)
        # expecting index 5
        self.assertEqual(result, 5)

    def test_iterative_not_found(self):
        # Test iterative search with a target that doesn't exist
        arr = [1, 2, 3, 5, 6]
        target = 4
        result = BinarySearch.iterativeBinarySearch(arr, target)
        self.assertEqual(result, -1)

    def test_recursive_found(self):
        # Test recursive search with a target that exists in the array
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 8
        result = BinarySearch.recursiveBinarySearch(arr, target)
        # expecting index 7
        self.assertEqual(result, 7)

    def test_recursive_not_found(self):
        # Test recursive search with a target that doesn't exist
        arr = [1, 2, 3, 5, 6]
        target = 4
        result = BinarySearch.recursiveBinarySearch(arr, target)
        self.assertEqual(result, -1)
    
    def test_empty_array(self):
        # Test both methods with an empty array
        arr = []
        target = 1
        iterative_result = BinarySearch.iterativeBinarySearch(arr, target)
        recursive_result = BinarySearch.recursiveBinarySearch(arr, target)
        self.assertEqual(iterative_result, -1)
        self.assertEqual(recursive_result, -1)
        
    def test_edge_cases(self):
        # Test with target at the beginning and end of array
        arr = [1, 3, 5, 7, 9]
        
        # Test first element
        self.assertEqual(BinarySearch.iterativeBinarySearch(arr, 1), 0)
        self.assertEqual(BinarySearch.recursiveBinarySearch(arr, 1), 0)
        
        # Test last element
        self.assertEqual(BinarySearch.iterativeBinarySearch(arr, 9), 4)
        self.assertEqual(BinarySearch.recursiveBinarySearch(arr, 9), 4)

if __name__ == '__main__':
    unittest.main()