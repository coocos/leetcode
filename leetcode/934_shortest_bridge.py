import unittest
import collections
from typing import List, Deque, Tuple


class Solution:
    """
    This solution is based on performing two breadth-first searches.

    The first breadth-first search is started from the first encountered
    square of land. This search expands until it has mapped out the entire island.
    The search also creates a secondary queue which will contain the perimeter, i.e.
    all immediate pieces of ocean surrounding the island which are encountered
    during the search. Once the island has been fully mapped a secondary breadth-first
    search is started from the perimeter which expands towards the second island. The
    search keeps track of the expansion distance until it meets the other island and at
    that point that particular distance is returned.
    """

    def shortestBridge(self, grid: List[List[int]]) -> int:

        height = len(grid)
        width = len(grid[0])
        neighbours = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        # Find a starting point for the first island
        start = (-1, -1)
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    start = (x, y)
                    break
            if start != (-1, -1):
                break

        # Map the island from the starting point
        visited = set([start])
        unexplored = collections.deque([start])
        perimeter: Deque[Tuple[int, int, int]] = collections.deque([])
        while unexplored:
            x, y = unexplored.popleft()
            if grid[y][x] == 0:
                perimeter.append((x, y, 0))
                continue
            for dx, dy in neighbours:
                neighbour = (x + dx, y + dy)
                if (
                    neighbour not in visited
                    and 0 <= neighbour[0] < width
                    and 0 <= neighbour[1] < height
                ):
                    unexplored.append(neighbour)
                    visited.add(neighbour)

        # Expand the island perimeter until it meets the other island
        while perimeter:
            x, y, distance = perimeter.popleft()
            if grid[y][x] == 1:
                return distance
            for dx, dy in neighbours:
                neighbour = (x + dx, y + dy)
                if (
                    neighbour not in visited
                    and 0 <= neighbour[0] < width
                    and 0 <= neighbour[1] < height
                ):
                    visited.add(neighbour)
                    perimeter.append((*neighbour, distance + 1))

        return -1


class TestSolution(unittest.TestCase):
    def test_small_islands(self):
        islands = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
        self.assertEqual(Solution().shortestBridge(islands), 2)

    def test_surrounded_island(self):
        islands = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual(Solution().shortestBridge(islands), 1)

    def test_orthogonal_islands(self):

        islands = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(Solution().shortestBridge(islands), 1)
