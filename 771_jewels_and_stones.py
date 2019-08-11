import unittest
from collections import Set


class Solution:
    """
    This solution simply creates a set with all the jewel tokens
    and then iterates through the stones one by one incrementing
    a counter if they are present in the set.

    Note that using sum() and a comprehension like

        return sum(s in jewels for s in S)

    would be cleaner but benchmarking it on leetcode shows that it's
    a slightly slower approach than using an explicit counter and
    a for loop.
    """
    def numJewelsInStones(self, J: str, S: str) -> int:

        jewels: Set[int] = set(J)
        count = 0
        for s in S:
            if s in jewels:
                count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(Solution().numJewelsInStones('aA', 'aAAbbbb'), 3)
