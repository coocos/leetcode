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
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        # A set with all the pieces of land
        land = set()
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == '1':
                    land.add((x, y))

        # Pieces of land already visited
        visited: Set[Tuple[int, int]] = set()

        # Number of islands
        islands = 0

        while land:

            island = collections.deque([land.pop()])

            while island:

                x, y = island.popleft()
                try:
                    land.remove((x, y))
                except KeyError:
                    pass

                neighbours = ((x, y + 1),
                              (x, max(0, y - 1)),
                              (x + 1, y),
                              (max(0, x - 1), y))
                for neighbour in neighbours:
                    if neighbour not in visited:
                        try:
                            if grid[neighbour[1]][neighbour[0]] == '1':
                                island.append(neighbour)
                        except IndexError:
                            pass
                        finally:
                            visited.add(neighbour)
            islands += 1

        return islands


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        islands = [
            list('11110'),
            list('11010'),
            list('11000'),
            list('00000')
        ]
        self.assertEqual(Solution().numIslands(islands), 1)

    def test_second_example(self):
        islands = [
            list('11000'),
            list('11000'),
            list('00100'),
            list('00011')
        ]
        self.assertEqual(Solution().numIslands(islands), 3)

    def test_third_example(self):
        islands = [
            list('1011011')
        ]
        self.assertEqual(Solution().numIslands(islands), 3)
