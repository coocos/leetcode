import unittest

from typing import Set, List


class Solution:
    """
    This solution simply iterates over the numbers, adding each
    one to a set and checking whether the number already exists
    in the set. Since adding to and looking up from a set are both
    (on average) constant time operations this makes the solution O(N).
    """
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen: Set[int] = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertTrue(Solution().containsDuplicate([1, 2, 3, 1]))

    def test_second_example(self):

        self.assertFalse(Solution().containsDuplicate([1, 2, 3, 4]))
