import unittest
from typing import List, Set, Tuple

Point = Tuple[int, int]


class Solution:
    """
    This solution treats the grid like a graph. The grid is iterated
    over and a recursive depth-first search is started from any point
    that has not been visited during any previous search. The depth-first
    search visits all the valid neighbours of the given point and is terminated
    when a cycle is found, i.e. the search reaches a point it has already
    visited once and which contains the same character. Note that the search
    also needs to maintain the previous point it arrived from.
    """

    def containsCycle(self, grid: List[List[str]]) -> bool:
        def is_cyclic(
            char: str,
            x: int,
            y: int,
            previous_x: int,
            previous_y: int,
            visited: Set[Point],
        ) -> bool:

            if not (0 <= x < len(grid[0])) or not (0 <= y < len(grid)):
                return False
            elif (x, y) in visited:
                return True
            elif grid[y][x] != char:
                return False

            visited.add((x, y))

            # Explore neighbours
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) != (previous_x, previous_y):
                    if is_cyclic(char, next_x, next_y, x, y, visited):
                        return True

            return False

        visited: Set[Point] = set()

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if (x, y) not in visited:
                    visited_during_search: Set[Point] = set()
                    if is_cyclic(grid[y][x], x, y, 1, -1, visited_during_search):
                        return True
                    visited.update(visited_during_search)

        return False


class TestSolution(unittest.TestCase):
    def test_true_example(self):

        grid = [
            ["a", "a", "a", "a"],
            ["a", "b", "b", "a"],
            ["a", "b", "b", "a"],
            ["a", "a", "a", "a"],
        ]
        self.assertTrue(Solution().containsCycle(grid))

    def test_another_true_example(self):
        grid = [
            ["c", "c", "c", "a"],
            ["c", "d", "c", "c"],
            ["c", "c", "e", "c"],
            ["f", "c", "c", "c"],
        ]
        self.assertTrue(Solution().containsCycle(grid))

    def test_false_example(self):

        grid = [["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]
        self.assertFalse(Solution().containsCycle(grid))

    def test_failing_example(self):

        grid = [
            ["f", "a", "a", "c", "b"],
            ["e", "a", "a", "e", "c"],
            ["c", "f", "b", "b", "b"],
            ["c", "e", "a", "b", "e"],
            ["f", "e", "f", "b", "f"],
        ]
        self.assertTrue(Solution().containsCycle(grid))
