import unittest
from typing import List


class Solution:
    """
    This solution combines depth-first search with a binary search
    to find the earliest point in time when you can reach the bottom
    right square.

    The depth-first search is given a specific time value and it searches
    whether it's possible to reach the bottom right square during
    that time. It's possible to brute-force the solution this way by
    simply iterating over possible time values like 0, 1, 2, 3, ...
    until the depth-first search is able to find a valid path to the
    bottom right square. However since we know the valid time range
    (because the grid contains values from 0 to N) we can perform
    a binary search to narrow down the time range faster by first
    attempting to find the path at time N / 2 and by then halving
    the search space until the search converges to a single time value.
    """

    def swimInWater(self, grid: List[List[int]]) -> int:

        size = len(grid)
        neighbours = ((0, -1), (1, 0), (0, 1), (-1, 0))

        def dfs(x: int, y: int, time: int, visited) -> bool:

            if (
                not (0 <= x < size and 0 <= y < size)
                or grid[y][x] > time
                or (x, y) in visited
            ):
                return False
            elif x == size - 1 and y == size - 1:
                return True

            visited.add((x, y))

            for nx, ny in neighbours:
                if dfs(x + nx, y + ny, time, visited):
                    return True

            return False

        low = 0
        high = len(grid) * len(grid) - 1
        while low < high:
            middle = (low + high) // 2
            if dfs(0, 0, middle, set()):
                high = middle
            else:
                low = middle + 1
        return high


class TestSolution(unittest.TestCase):
    def test_small_size_grid(self):

        grid = [[0, 2], [1, 3]]
        self.assertEqual(Solution().swimInWater(grid), 3)

    def test_medium_size_grid(self):

        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
        self.assertEqual(Solution().swimInWater(grid), 16)

    def test_large_size_grid(self):

        grid = [
            [26, 99, 80, 1, 89, 86, 54, 90, 47, 87],
            [9, 59, 61, 49, 14, 55, 77, 3, 83, 79],
            [42, 22, 15, 5, 95, 38, 74, 12, 92, 71],
            [58, 40, 64, 62, 24, 85, 30, 6, 96, 52],
            [10, 70, 57, 19, 44, 27, 98, 16, 25, 65],
            [13, 0, 76, 32, 29, 45, 28, 69, 53, 41],
            [18, 8, 21, 67, 46, 36, 56, 50, 51, 72],
            [39, 78, 48, 63, 68, 91, 34, 4, 11, 31],
            [97, 23, 60, 17, 66, 37, 43, 33, 84, 35],
            [75, 88, 82, 20, 7, 73, 2, 94, 93, 81],
        ]
        self.assertEqual(Solution().swimInWater(grid), 81)
