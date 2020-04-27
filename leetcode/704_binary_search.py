import unittest

from typing import List


class Solution:
    """
    This solution is a standard iterative binary search implementation.
    """
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


class TestSolution(unittest.TestCase):

    def test_successful_search(self):

        numbers = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(Solution().search(numbers, 9), 4)

    def test_missing_search(self):

        numbers = [-1, 0, 3, 5, 9, 12]
        self.assertEqual(Solution().search(numbers, 2), -1)

    def test_searching_single_value_list(self):

        numbers = [5]
        self.assertEqual(Solution().search(numbers, 5), 0)
