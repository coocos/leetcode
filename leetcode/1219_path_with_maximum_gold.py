import unittest
from typing import List, FrozenSet, Tuple


class Solution:
    """
    This solution starts a depth-first search from each position with gold.
    The search is expanded to the surrounding positions while keeping track of
    the accumulated sum as well as the already visited positions. The recursion
    terminates when the search attempts to revisit a visited position, it goes
    out of bounds or the position does not contain gold. Finally the maximum of
    of all the searches is returned.
    """
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        width = len(grid[0]) - 1
        height = len(grid) - 1

        def gather(x: int,
                   y: int,
                   visited: FrozenSet[Tuple[int, int]],
                   gold: int = 0) -> int:

            if not 0 <= x <= width:
                return gold
            if not 0 <= y <= height:
                return gold
            if (x, y) in visited:
                return gold
            if grid[y][x] == 0:
                return gold

            visited_plus_this = visited | frozenset([(x, y)])
            gold += grid[y][x]

            return max(gather(x - 1, y, visited_plus_this, gold),
                       gather(x + 1, y, visited_plus_this, gold),
                       gather(x, y - 1, visited_plus_this, gold),
                       gather(x, y + 1, visited_plus_this, gold))

        best = 0
        visited: FrozenSet[Tuple[int, int]] = frozenset()
        for y, row in enumerate(grid):
            for x, gold in enumerate(row):
                if gold:
                    best = max(gather(x, y, visited), best)

        return best


class TestSolution(unittest.TestCase):

    def test_simple_mine(self):

        mine = [
            [0, 6, 0],
            [5, 8, 7],
            [0, 9, 0]
        ]
        self.assertEqual(Solution().getMaximumGold(mine), 24)

    def test_larger_mine(self):
        mine = [
            [1, 0, 7],
            [2, 0, 6],
            [3, 4, 5],
            [0, 3, 0],
            [9, 0, 20]
        ]
        self.assertEqual(Solution().getMaximumGold(mine), 28)
