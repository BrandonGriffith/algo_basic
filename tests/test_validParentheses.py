import unittest
import sys
import os

# Add the parent directory to sys.path to import modules from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validParentheses import ValidParentheses

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.validator = ValidParentheses()

    def test_brute_force_valid_simple(self):
        self.assertTrue(self.validator.brute_force("()"))
        self.assertTrue(self.validator.brute_force("{}"))
        self.assertTrue(self.validator.brute_force("[]"))

    def test_brute_force_valid_nested(self):
        self.assertTrue(self.validator.brute_force("([{}])"))
        self.assertTrue(self.validator.brute_force("{[()]}"))
        self.assertTrue(self.validator.brute_force("()[]{}"))

    def test_brute_force_invalid(self):
        self.assertFalse(self.validator.brute_force("(]"))
        self.assertFalse(self.validator.brute_force("([)]"))
        self.assertFalse(self.validator.brute_force("{[}"))
        self.assertFalse(self.validator.brute_force("]"))

    def test_brute_force_empty(self):
        self.assertTrue(self.validator.brute_force(""))

    def test_stack_valid_simple(self):
        self.assertTrue(self.validator.stack("()"))
        self.assertTrue(self.validator.stack("{}"))
        self.assertTrue(self.validator.stack("[]"))

    def test_stack_valid_nested(self):
        self.assertTrue(self.validator.stack("([{}])"))
        self.assertTrue(self.validator.stack("{[()]}"))
        self.assertTrue(self.validator.stack("()[]{}"))

    def test_stack_invalid(self):
        self.assertFalse(self.validator.stack("(]"))
        self.assertFalse(self.validator.stack("([)]"))
        self.assertFalse(self.validator.stack("{[}"))
        self.assertFalse(self.validator.stack("]"))

    def test_stack_empty(self):
        self.assertTrue(self.validator.stack(""))

    def test_stack_unbalanced(self):
        self.assertFalse(self.validator.stack("(("))
        self.assertFalse(self.validator.stack("((("))
        self.assertFalse(self.validator.stack("{{{"))
        self.assertFalse(self.validator.stack("["))

    def test_brute_force_unbalanced(self):
        self.assertFalse(self.validator.brute_force("(("))
        self.assertFalse(self.validator.brute_force("((("))
        self.assertFalse(self.validator.brute_force("{{{"))
        self.assertFalse(self.validator.brute_force("["))

if __name__ == '__main__':
    unittest.main()