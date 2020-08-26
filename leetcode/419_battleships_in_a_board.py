import unittest
from typing import List, Set, Tuple


class Solution:
    """
    This recursive solution iterates over the grid and performs a depth-first
    search whenever it finds a battleship. This depth-first search perform a
    flood fill to map out the entire ship and essentially discards the points
    consumed by the ship from the grid. Once the entire grid has been iterated
    over the amount of battleships is equal to amount of depth-first searches
    performed.

    Note that it would probably be faster to restrict the flood fill to only
    expand vertically or horizontally since it's guaranteed that the ships are
    either vertical or horizontal.
    """

    def countBattleships(self, board: List[List[str]]) -> int:
        def explore_battleship(y: int, x: int, visited: Set[Tuple[int, int]]) -> None:
            if (
                not (0 <= y < len(board))
                or not (0 <= x < len(board[y]))
                or board[y][x] == "."
                or (x, y) in visited
            ):
                return

            visited.add((x, y))
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    explore_battleship(ny, nx, visited)

        visited: Set[Tuple[int, int]] = set()

        battleships = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if (x, y) not in visited and board[y][x] == "X":
                    explore_battleship(y, x, visited)
                    battleships += 1
        return battleships


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        board = [
            list("X..X"),
            list("...X"),
            list("...X"),
        ]
        self.assertEqual(Solution().countBattleships(board), 2)
