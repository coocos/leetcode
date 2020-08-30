import sys
import unittest
from typing import List


class Solution:
    """
    This solution iterates over the square array from top left to bottom
    right and adds to each cell the minimum value of the three cells above
    it. The last row ends up containing all the possible minimum falling path
    sums once this is performed all the way from the top to the bottom.
    """

    def minFallingPathSum(self, A: List[List[int]]) -> int:

        for y in range(1, len(A)):
            for x in range(len(A[y])):
                above = A[y - 1]
                left = above[x - 1] if x - 1 >= 0 else sys.maxsize
                center = above[x]
                right = above[x + 1] if x + 1 < len(A[y]) else sys.maxsize
                A[y][x] += min(left, center, right)

        return min(A[-1])


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(Solution().minFallingPathSum(grid), 12)

    def test_single_row_example(self):

        grid = [[1]]
        self.assertEqual(Solution().minFallingPathSum(grid), 1)

    def test_negative_example(self):

        grid = [[10, -98, 44], [-20, 65, 34], [-100, -1, 74]]
        self.assertEqual(Solution().minFallingPathSum(grid), -218)
