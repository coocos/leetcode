import unittest
from typing import List


class Solution:
    """
    This solution uses binary search to find the insert position.
    Binary search can be used since the array is already guaranteed
    to be sorted.
    """
    def searchInsert(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            middle = (low + high) // 2
            if nums[middle] > target:
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                return middle

        return low


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 5), 2)

    def test_second_example(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 2), 1)

    def test_third_example(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 7), 4)

    def test_fourth_example(self):
        self.assertEqual(Solution().searchInsert([1, 3, 5, 6], 0), 0)
