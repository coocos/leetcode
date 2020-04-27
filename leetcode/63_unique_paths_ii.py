import unittest
from typing import List


class Solution:
    """
    This solution uses the same dynamic programming logic as the
    solution to problem #62 - unique paths. The gist is to realize
    that all the positions on the the first row and column only have
    one possible path each - or not even one if the path is blocked.
    Once the first column and first row have been filled you can simply
    iterate over the rest of the grid and each position on the grid
    has as many paths to it as there are paths to the position above it
    and to the left of it. If the position is an obstacle it can be skipped
    and if the position above or to the left is an obstacle they can be
    considered to have 0 paths to them.

    The grid passed as an argument is reused to save space by converting
    the obstacles to -1 instead of 1 so that it's possible to keep track
    of which position is an actual obstacle and which is actually a position
    with a single path to it.
    """
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        # Do not attempt to solve grid where the endpoint is blocked
        if grid[-1][-1] == 1:
            return 0

        # Replace obstacles with -1 in order to reuse the grid
        for row in grid:
            for x in range(len(row)):
                if row[x] == 1:
                    row[x] = -1

        # Mark positions in the first column to 1 until an obstacle is met
        paths_to_position = 1
        for y in range(len(grid)):
            # Obstacle met - rest of the column is unreachable
            if grid[y][0] == -1:
                paths_to_position = 0
                continue
            grid[y][0] = paths_to_position

        # Mark positions in the first row to 1 until an obstacle is met
        paths_to_position = 1
        for x in range(len(grid[0])):
            # Obstacle met - rest of the row is unreachable
            if grid[0][x] == -1:
                paths_to_position = 0
                continue
            grid[0][x] = paths_to_position

        # Go over the the grid and sum up the paths
        for y in range(1, len(grid)):
            for x in range(1, len(grid[0])):
                if grid[y][x] != - 1:
                    top = grid[y - 1][x] if grid[y - 1][x] != -1 else 0
                    left = grid[y][x - 1] if grid[y][x - 1] != -1 else 0
                    grid[y][x] = top + left

        return grid[-1][-1]


class TestSolution(unittest.TestCase):

    def test_obstacle_in_the_middle(self):

        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Solution().uniquePathsWithObstacles(grid), 2)

    def test_vertical_obstacle(self):

        grid = [
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Solution().uniquePathsWithObstacles(grid), 3)

    def test_horizontal_obstacle(self):

        grid = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Solution().uniquePathsWithObstacles(grid), 3)

    def test_grid_with_a_wall(self):

        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(Solution().uniquePathsWithObstacles(grid), 1)

    def test_grid_where_target_is_blocked(self):

        grid = [
            [0, 1]
        ]
        self.assertEqual(Solution().uniquePathsWithObstacles(grid), 0)
