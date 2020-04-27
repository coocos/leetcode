import sys
import unittest
from typing import List


class Solution:
    """
    This solution uses a dynamic programming approach. The minimum
    path sum used to reach a point (x, y) on the grid is the minimum path
    sum used to reach the point (x - 1, y) or (x, y - 1) plus the
    value of the point (x, y) itself. This is because you can only
    traverse down and / or right so the only way to reach a point is
    to arrive to it from the left or above. Therefore you can iterate
    over the entire grid, row by row and column by column, always
    updating the current point on the grid to be equal to
    min(sum_left, sum_top) + point_value until you reach the bottom
    right corner. At that point all of the points on the grid will
    contain the minimum path sum used to reach that point.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:

        height = len(grid)
        width = len(grid[0])

        for y in range(height):
            for x in range(width):

                # First point can be skipped since it's the starting point
                if x == 0 and y == 0:
                    continue

                top = grid[y - 1][x] if y > 0 else sys.maxsize
                left = grid[y][x - 1] if x > 0 else sys.maxsize
                grid[y][x] = min(top, left) + grid[y][x]

        return grid[-1][-1]


class TestSolution(unittest.TestCase):

    def test_simple_grid(self):

        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        self.assertEqual(Solution().minPathSum(grid), 7)
