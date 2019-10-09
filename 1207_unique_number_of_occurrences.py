import unittest
import collections
from typing import List, DefaultDict


class Solution:
    """
    This solution counts the amount of times each value occurs
    by iterating over the list and keeping a dictionary of the occurrence
    counts. Finally the size of the dictionary is compared against
    the size of the set of values (i.e. occurrences) in the dictionary.
    If they differ, then at least two values share the same count and
    thus are not unique.
    """
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts: DefaultDict[int, int] = collections.defaultdict(int)
        for value in arr:
            counts[value] += 1
        return len(counts) == len(set(counts.values()))


class TestSolution(unittest.TestCase):

    def test_true_example(self):
        self.assertTrue(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))

    def test_false_example(self):
        self.assertFalse(Solution().uniqueOccurrences([1, 2]))
