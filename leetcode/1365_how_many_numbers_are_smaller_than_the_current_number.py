import unittest
import collections
from typing import List, Dict


class Solution:
    """
    This solution first sorts the numbers and then iterates over them.
    As the numbers are iterated over, each number and its index is
    inserted into a dictionary if the number is not already present in
    the dictionary. This way the dictionary ends up containing how
    many smaller numbers each number has.

    After the dictionary has been constructed the original unsorted list
    of numbers is mapped to a new list by retrieving the value of each number
    from the constructed dictionary.
    """

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        counts: Dict[int, int] = {}
        for i, num in enumerate(sorted(nums)):
            if num not in counts:
                counts[num] = i
        return [counts[num] for num in nums]


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertListEqual(
            Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]), [4, 0, 1, 1, 3]
        )
