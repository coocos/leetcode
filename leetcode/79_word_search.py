import unittest
from typing import List, FrozenSet, Tuple


class Solution:
    """
    This solution performs a recursive depth-first search starting from
    each of the letters on the board which match the first letter of
    the word. The depth-first search expands to all of the neighboring
    letters if they match the next letter of the word. The search
    continues until either the word has been formed or the all of the
    branches of the recursion go out of bounds or fail to form the word.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:

        width = len(board[0]) - 1
        height = len(board) - 1

        def search(x: int, y: int, visited: FrozenSet[Tuple[int, int]], letter: int = 0) -> bool:

            if (not 0 <= x <= width or
                not 0 <= y <= height or
                (x, y) in visited):
                return False

            # Word lengths match so check if the words match
            if letter == len(word) - 1:
                return word[letter] == board[y][x]

            # Terminate recursion if the current letter does not match
            if board[y][x] != word[letter]:
                return False

            visited_plus_this = visited | frozenset(((x, y),))
            next_letter = letter + 1

            return (search(x + 1, y, visited_plus_this, next_letter) or
                    search(x - 1, y, visited_plus_this, next_letter) or
                    search(x, y + 1, visited_plus_this, next_letter) or
                    search(x, y - 1, visited_plus_this, next_letter))

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == word[0] and search(x, y, frozenset()):
                    return True
        return False


class TestSolution(unittest.TestCase):

    def test_true_example(self):

        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        self.assertTrue(Solution().exist(board, "ABCCED"))

    def test_false_example(self):

        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        self.assertFalse(Solution().exist(board, "ABCB"))
