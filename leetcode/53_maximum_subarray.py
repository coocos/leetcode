import unittest
from typing import List


class Solution:
    """
    This solution uses dynamic programming to find the sum of the maximum
    subarray. The idea is to realize that the maximum subarray sum of the
    nth number is either the nth integer plus the largest subarray sum of
    the (n - 1)th integer or the nth integer itself. Therefore it's possible
    to just iterate over the array once and compute the sum based on the
    integer itself and the sum in the previous position. To conserve space
    you can also reuse the original list of integers to store the sums.
    """
    def maxSubArray(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            try:
                nums[i] = max(nums[i] + nums[i - 1], nums[i])
            except IndexError:
                nums[i] = nums[i]
        return max(nums)


class TestSolution(unittest.TestCase):

    def test_basic_example(self):

        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(Solution().maxSubArray(nums), 6)

    def test_another_example(self):

        nums = [1]
        self.assertEqual(Solution().maxSubArray(nums), 1)
