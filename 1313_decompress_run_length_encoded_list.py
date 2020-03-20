import unittest
from typing import List


class Solution:
    """Simple RLE implementation"""
    def decompressRLElist(self, nums: List[int]) -> List[int]:

        values: List[int] = []
        for i in range(0, len(nums), 2):
            length, value = nums[i: i + 2]
            values += [value] * length
        return values


class TestSolution(unittest.TestCase):
    def test_basic_example(self):

        self.assertListEqual(Solution().decompressRLElist([1, 2, 3, 4]), [2, 4, 4, 4])
