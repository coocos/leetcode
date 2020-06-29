import unittest
from typing import List


class Solution:
    """
    This solution iterates over the list and replaces each value in the
    list with the value of the previous element plus the value of the current
    element. After this is performed over the entire list the end result is
    the running sum.
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i == 0:
                continue
            nums[i] += nums[i - 1]
        return nums


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertListEqual(Solution().runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
