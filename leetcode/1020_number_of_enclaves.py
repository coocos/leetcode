import unittest
from typing import List, Set, Tuple


class Solution:
    """
    This solution uses a depth-first search to count the number of enclaves.
    The grid is looped over and whenever a piece of land is encountered a recursive
    depth-first search is started from that point. The search will expand to
    the surrounding pieces of land until it either meets a boundary and returns
    -1 or has explored all connected pieces of land and returns their count.
    """

    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(x: int, y: int, visited: Set[Tuple[int, int]]) -> int:

            # Out of bounds
            if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A):
                return -1
            # Visited already or encountered water
            if (x, y) in visited or A[y][x] == 0:
                return 0

            visited.add((x, y))
            enclaves = []
            for xd, yd in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                enclaves.append(dfs(x + xd, y + yd, visited))
            if -1 in enclaves:
                return -1
            return 1 + sum(enclaves)

        enclaves = 0
        visited: Set[Tuple[int, int]] = set()
        for y in range(1, len(A) - 1):
            for x in range(1, len(A[y]) - 1):
                if A[y][x] == 1:
                    enclaves += max(0, dfs(x, y, visited))
        return enclaves


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(Solution().numEnclaves(grid), 3)

    def test_second_example(self):

        grid = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        self.assertEqual(Solution().numEnclaves(grid), 0)
