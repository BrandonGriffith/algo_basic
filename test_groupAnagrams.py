import unittest
from groupAnagrams import GroupAnagrams


def normalize(groups):
    # sort each anagram group and sort the list of groups for comparison
    return sorted([sorted(group) for group in groups])


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.ga = GroupAnagrams()
        self.input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        self.expected = normalize([ ["eat", "tea", "ate"], ["tan", "nat"], ["bat"] ])

    def test_sorting_method(self):
        result = self.ga.sorting(self.input_words)
        self.assertEqual(normalize(result), self.expected)

    def test_hashing_method(self):
        result = self.ga.hashing(self.input_words)
        self.assertEqual(normalize(result), self.expected)


if __name__ == '__main__':
    unittest.main()
