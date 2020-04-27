import unittest
import collections

from typing import List, DefaultDict


class Solution:
    """
    This O(n) solution keeps a dictionary with a count of each
    encountered element. If an element count reaches over n / 2
    then it is the majority element.
    """
    def majorityElement(self, nums: List[int]) -> int:

        counts: DefaultDict[int, int] = collections.defaultdict(int)
        majority = len(nums) / 2

        for num in nums:

            counts[num] += 1
            if counts[num] > majority:
                return num

        raise Exception('No majority element in list')


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(Solution().majorityElement([3, 2, 3]), 3)

    def test_second_example(self):
        self.assertEqual(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)
