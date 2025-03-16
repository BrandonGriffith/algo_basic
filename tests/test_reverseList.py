import unittest
import sys
import os

# Add the parent directory to sys.path to import modules from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reverseList import ReverseList

# Define a ListNode class for testing
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # Helper to convert list to array for easier testing
    @staticmethod
    def to_array(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    # Helper to create linked list from array
    @staticmethod
    def from_array(arr):
        if not arr:
            return None
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.reverser = ReverseList()
    
    def test_iteration_empty(self):
        # Test reversing an empty list
        self.assertIsNone(self.reverser.iteration(None))
    
    def test_iteration_single_node(self):
        # Test reversing a single node list
        head = ListNode(1)
        result = self.reverser.iteration(head)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)
    
    def test_iteration_multiple_nodes(self):
        # Test reversing a list with multiple nodes
        head = ListNode.from_array([1, 2, 3, 4, 5])
        result = self.reverser.iteration(head)
        self.assertEqual(ListNode.to_array(result), [5, 4, 3, 2, 1])
    
    def test_recursion_empty(self):
        # Test recursively reversing an empty list
        self.assertIsNone(self.reverser.recursion(None))
    
    def test_recursion_single_node(self):
        # Test recursively reversing a single node list
        head = ListNode(1)
        result = self.reverser.recursion(head)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.next)
    
    def test_recursion_multiple_nodes(self):
        # Test recursively reversing a list with multiple nodes
        head = ListNode.from_array([1, 2, 3, 4, 5])
        result = self.reverser.recursion(head)
        self.assertEqual(ListNode.to_array(result), [5, 4, 3, 2, 1])
    
    def test_compare_methods(self):
        # Test that both methods produce the same result
        array = [1, 2, 3, 4, 5]
        list1 = ListNode.from_array(array)
        list2 = ListNode.from_array(array)
        
        iter_result = ListNode.to_array(self.reverser.iteration(list1))
        recur_result = ListNode.to_array(self.reverser.recursion(list2))
        
        self.assertEqual(iter_result, recur_result)

if __name__ == '__main__':
    unittest.main()