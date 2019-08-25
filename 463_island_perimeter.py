import unittest
from typing import List, Set, Tuple


class Solution:
    """
    This solution goes through the grid and generates four
    edges for each land cell in the grid. The edges are added
    to a set of edges if they are not already in the set and
    removed from the set if they already present in it. This way
    the shared edges are not present in the set and after
    iterating over the entire grid only the perimeter edges remain
    in the set of edges.
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter: Set[Tuple[float, float]] = set()

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    edges = ((x - 0.5, y),
                             (x, y - 0.5),
                             (x + 0.5, y),
                             (x, y + 0.5))
                    for edge in edges:
                        if edge not in perimeter:
                            perimeter.add(edge)
                        else:
                            perimeter.remove(edge)

        return len(perimeter)


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        grid = [[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]]

        self.assertEqual(Solution().islandPerimeter(grid), 16)
