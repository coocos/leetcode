import unittest
from typing import List


class Solution:
    """
    This iterative solution simply constructs a temporary list and shuffles
    the string accordingly to indices list. Then the temporary list is
    joined to a string and returned.
    """
    def restoreString(self, s: str, indices: List[int]) -> str:
        restored = [""] * len(s)
        for i, c in enumerate(s):
            restored[indices[i]] = c
        return "".join(restored)


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(
            Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]), "leetcode"
        )

