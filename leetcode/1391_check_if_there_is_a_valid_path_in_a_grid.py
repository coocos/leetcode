import unittest
import collections
from typing import List


class Solution:
    """
    This rather inefficient and ugly solution has two separate steps. First
    the grid is upscaled into a larger grid where each cell is mapped
    into a larger 3 x 3 cell. Then a breadth-first search is performed
    starting from the (1, 1) position since it's a valid position for
    all different cell / street types. If the breadth-first search
    expands to the last cell the search can be terminated as the path
    is valid.

    Note that it's possible to avoid the previously described slow
    "upscaling" step by mapping the inputs and outputs of each street
    type but the resulting code is rather awkward to follow whereas a
    simple breadth-first search on a standard grid is quite easy to grasp.
    """

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def upscale_grid(grid: List[List[int]]) -> List[List[bool]]:

            scaled: List[List[bool]] = []
            for y in range(len(grid) * 3):
                scaled.append([])
                for x in range(len(grid[0]) * 3):
                    scaled[-1].append(False)

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    scaled[y * 3 + 1][x * 3 + 1] = True
                    if grid[y][x] == 1:
                        scaled[y * 3 + 1][x * 3] = True
                        scaled[y * 3 + 1][x * 3 + 2] = True
                    elif grid[y][x] == 2:
                        scaled[y * 3][x * 3 + 1] = True
                        scaled[y * 3 + 2][x * 3 + 1] = True
                    elif grid[y][x] == 3:
                        scaled[y * 3 + 1][x * 3] = True
                        scaled[y * 3 + 2][x * 3 + 1] = True
                    elif grid[y][x] == 4:
                        scaled[y * 3 + 1][x * 3 + 2] = True
                        scaled[y * 3 + 2][x * 3 + 1] = True
                    elif grid[y][x] == 5:
                        scaled[y * 3][x * 3 + 1] = True
                        scaled[y * 3 + 1][x * 3] = True
                    else:
                        scaled[y * 3][x * 3 + 1] = True
                        scaled[y * 3 + 1][x * 3 + 2] = True
            return scaled

        def bfs(x: int, y: int, grid: List[List[bool]]) -> bool:

            neighbour_vectors = [(0, -1), (1, 0), (0, 1), (-1, 0)]
            visited = set()
            queue = collections.deque([(x, y)])

            while queue:
                x, y = queue.popleft()
                visited.add((x, y))
                for xd, yd in neighbour_vectors:
                    neighbour_x = x + xd
                    neighbour_y = y + yd
                    if (
                        0 <= neighbour_x <= len(grid[0]) - 1
                        and 0 <= neighbour_y <= len(grid) - 1
                        and (neighbour_x, neighbour_y) not in visited
                        and grid[neighbour_y][neighbour_x]
                    ):
                        if y > len(grid) - 3 and x > len(grid[0]) - 3:
                            return True
                        queue.append((neighbour_x, neighbour_y))

            return False

        return bfs(1, 1, upscale_grid(grid))


class TestSolution(unittest.TestCase):
    def test_true_example(self):

        grid = [[2, 4, 3], [6, 5, 2]]
        self.assertTrue(Solution().hasValidPath(grid))

    def test_false_example(self):

        grid = [[1, 2, 1], [1, 2, 1]]
        self.assertFalse(Solution().hasValidPath(grid))

    def test_second_false_example(self):

        grid = [[1, 1, 2]]
        self.assertFalse(Solution().hasValidPath(grid))

    def test_second_true_example(self):

        grid = [[1, 1, 1, 1, 1, 1, 3]]
        self.assertTrue(Solution().hasValidPath(grid))

    def test_third_true_example(self):

        grid = [[1, 1, 1, 1, 1, 1, 3]]
        self.assertTrue(Solution().hasValidPath(grid))

    def test_failing_example(self):

        grid = [[4, 1], [6, 1]]
        self.assertTrue(Solution().hasValidPath(grid))
