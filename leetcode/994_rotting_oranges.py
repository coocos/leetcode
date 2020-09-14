import unittest
import collections
from typing import List


class Solution:
    """
    This solution uses breadth-first search to propagate the
    rottenness. First the grid is scanned to locate all rotten and
    fresh oranges. Then a standard breadth-first search is started
    by queueing the coordinates of the rotten oranges and the initial time.
    As the search expands to cover the fresh neighbours of the rotten oranges,
    those fresh oranges are also marked as rotten and they are removed from
    the set of fresh oranges constructed during the initial scan.
    The search terminates when there no more fresh oranges remain or
    the queue powering the breadth-first search is emptied yet fresh
    oranges still remain.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        rotten = set()
        fresh = set()
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 2:
                    rotten.add((x, y))
                elif grid[y][x] == 1:
                    fresh.add((x, y))

        visited = set()
        queue = collections.deque([(x, y, 0) for x, y in rotten])
        time = 0
        while queue:

            # No point in continuing breadth-first search if there are no fresh oranges left
            if not fresh:
                return time

            x, y, time = queue.popleft()
            if (x, y) in visited:
                continue

            visited.add((x, y))
            if grid[y][x] == 1:
                fresh.remove((x, y))

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if (
                    0 <= nx < width
                    and 0 <= ny < height
                    and (nx, ny) not in visited
                    and grid[ny][nx] == 1
                ):
                    queue.append((nx, ny, time + 1))

        return -1 if fresh else time


class TestSolution(unittest.TestCase):
    def test_all_oranges_rotting(self):

        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        self.assertEqual(Solution().orangesRotting(grid), 4)

    def test_one_orange_staying_fresh(self):
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        self.assertEqual(Solution().orangesRotting(grid), -1)

    def test_all_oranges_being_rotten_at_start(self):
        grid = [[0, 2]]
        self.assertEqual(Solution().orangesRotting(grid), 0)

    def test_example_with_two_rotting_oranges(self):
        grid = [[2], [1], [1], [1], [2], [1], [1]]
        self.assertEqual(Solution().orangesRotting(grid), 2)

    def test_grid_with_no_oranges(self):
        grid = [[0]]
        self.assertEqual(Solution().orangesRotting(grid), 0)
