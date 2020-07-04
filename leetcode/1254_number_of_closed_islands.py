import unittest
import collections
from typing import List, Set


class Solution:
    """
    This solution iterates over the grid and when it finds a point of land, it
    performs a breadth-first search for all surrounding points of land starting
    from that point. If during the breadth-first search the search goes out of
    bounds it means that the island is not closed. To speed up the search a set
    of already visited points is maintained.
    """

    def closedIsland(self, grid: List[List[int]]) -> int:

        all_visited_points = set()
        closed_islands = 0

        def is_closed_island(x: int, y: int) -> bool:

            unvisited_points = collections.deque([(x, y)])
            visited_points = set()
            closed_island = True
            while unvisited_points:
                x, y = unvisited_points.popleft()
                if (x, y) in visited_points:
                    continue
                # Out of bounds
                if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1:
                    closed_island = False
                    continue
                visited_points.add((x, y))
                if grid[y][x] == 0:
                    for xy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                        if xy not in visited_points:
                            unvisited_points.append(xy)
            all_visited_points.update(visited_points)
            return closed_island

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (
                    grid[y][x] == 0
                    and (x, y) not in all_visited_points
                    and is_closed_island(x, y)
                ):
                    closed_islands += 1

        return closed_islands


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        grid = [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
        self.assertEqual(Solution().closedIsland(grid), 2)

    def test_second_example(self):
        grid = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]
        self.assertEqual(Solution().closedIsland(grid), 1)

    def test_third_example(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
        self.assertEqual(Solution().closedIsland(grid), 2)

    def test_fourth_example(self):

        grid = [
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0],
        ]
        self.assertEqual(Solution().closedIsland(grid), 1)

    def test_fifth_example(self):

        grid = [
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
        ]
        self.assertEqual(Solution().closedIsland(grid), 5)

    def test_sixth_example(self):

        grid = [
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        ]
        self.assertEqual(Solution().closedIsland(grid), 4)
