import unittest
from typing import List, FrozenSet, Tuple


class Solution:
    """
    This solution performs a recursive depth-first search over the grid.
    The search keeps track of all points it has visited so far, dodges
    the obstacles, never backtracks and once it encounters the ending point,
    it compares the amount of visited points against the amount of empty squares
    on the grid. If the counts match then that particular search path has
    visited all the empty squares once. Finally the count of such paths is
    summed as the recursion terminates.
    """

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        starting_square = (0, 0)
        ending_square = (0, 0)
        empty_squares = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    starting_square = (x, y)
                elif grid[y][x] == 2:
                    ending_square = (x, y)
                elif grid[y][x] == 0:
                    empty_squares += 1

        def search(x: int, y: int, visited: FrozenSet[Tuple[int, int]]) -> int:

            # Out of bounds
            if not 0 <= x < len(grid[0]) or not 0 <= y < len(grid):
                return 0
            # Obstacle
            elif grid[y][x] == -1:
                return 0
            # Ending
            elif grid[y][x] == 2:
                return int(len(visited) == empty_squares + 1)

            paths = 0
            for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
                if (nx, ny) not in visited:
                    paths += search(nx, ny, visited | frozenset([(x, y)]))
            return paths

        return search(*starting_square, frozenset())


class TestSolution(unittest.TestCase):
    def test_grid_with_two_paths(self):

        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
        self.assertEqual(Solution().uniquePathsIII(grid), 2)

    def test_grid_with_four_paths(self):

        grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
        self.assertEqual(Solution().uniquePathsIII(grid), 4)

    def test_grid_with_no_valid_path(self):
        grid = [[0, 1], [2, 0]]
        self.assertEqual(Solution().uniquePathsIII(grid), 0)
