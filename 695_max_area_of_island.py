import unittest
import collections
from typing import List, Set, Tuple


class Solution:
    """
    This solution first constructs a set with all the pieces of
    land. Next a piece of land is selected from the set and
    breadth-first search is conducted starting from that piece
    of land until all pieces of land on that particular island
    have been visited. Whenever a piece of land is visited, it is
    removed from the original set of lands. Once all the pieces
    of one island have been visited, then another piece of land
    from the original land set is taken and the process is repeated
    until all pieces of land have been visited and the original
    set of pieces of land is empty.

    The size of each island can be determined by simply computing
    how many pieces of land were explored (i.e. removed from the original
    set of land) during the breadth-first search of each island.
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Set of all pieces of land
        islands = set()
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == 1:
                    islands.add((x, y))

        explored: Set[Tuple[int, int]] = set()
        largest_island = 0

        while islands:

            unexplored = len(islands)
            island = collections.deque([islands.pop()])

            # Do breadth-first search of the entire island
            while island:
                x, y = island.popleft()
                try:
                    islands.remove((x, y))
                except KeyError:
                    pass
                neighbours = (
                    (x, max(0, y - 1)),
                    (x, y + 1),
                    (x + 1, y),
                    (max(0, x - 1), y)
                )
                for x, y in neighbours:
                    try:
                        if grid[y][x] == 1 and (x, y) not in explored:
                            island.append((x, y))
                    except IndexError:
                        pass
                    finally:
                        explored.add((x, y))

            # The size of the current island is the amount of explored cells
            island_size = unexplored - len(islands)
            if island_size > largest_island:
                largest_island = island_size

        return largest_island


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        islands = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
        self.assertEqual(Solution().maxAreaOfIsland(islands), 6)

    def test_second_example(self):
        islands = [
            [1, 0, 1],
            [0, 0, 1],
            [1, 1, 1]

        ]
        self.assertEqual(Solution().maxAreaOfIsland(islands), 5)
