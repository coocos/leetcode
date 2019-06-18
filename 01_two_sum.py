import unittest
from typing import List, Dict


class Solution:
    """
    A simple O(N) solution which stores previously seen numbers' indices
    in a dictionary. For each number the other needed number can be
    computed by subtracting the current number from the target number.
    Then you can just check the dictionary if it's already been seen
    and at what index.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen: Dict[int, int] = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in seen:
                return [seen[needed], i]
            seen[num] = i

        return []


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        self.assertListEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_second_example(self):
        self.assertListEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
