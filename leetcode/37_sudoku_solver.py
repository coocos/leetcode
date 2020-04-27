import unittest
from typing import List, Tuple, Set, Optional


class Solution:
    """
    This solution is based on a brute force backtracking approach.

    First the first empty cell is located and it is pushed on to a stack. The
    cell is set to 1 and the board is checked for validity. If the board is
    valid then the next empty cell is located and it is pushed on to the stack
    and set as the current cell. If the board is not valid then the cell is
    incremented by 1 until the board is either valid or the number is larger
    than 9. If the number is larger than 9 then the algorithm backtracks and
    sets the current cell to empty and pops the last cell position from the
    stack and increments the cell by 1. This process is repeated until the
    board is valid.
    """
    def _is_row_valid(self, row: int) -> bool:
        seen: Set[str] = set()
        for letter in self.board[row]:
            if letter in seen and letter != '.':
                return False
            seen.add(letter)
        return True

    def _is_column_valid(self, col: int) -> bool:
        seen: Set[str] = set()
        for row in range(9):
            letter = self.board[row][col]
            if letter in seen and letter != '.':
                return False
            seen.add(letter)
        return True

    def _is_square_valid(self, row: int, col: int) -> bool:
        square_x = col // 3 * 3
        square_y = row // 3 * 3

        seen: Set[str] = set()
        for y in range(square_y, square_y + 3):
            for x in range(square_x, square_x + 3):
                letter = self.board[y][x]
                if letter in seen and letter != '.':
                    return False
                seen.add(letter)
        return True

    def is_board_valid(self, row: int, col: int):
        return self._is_square_valid(row, col) and \
               self._is_column_valid(col) and \
               self._is_row_valid(row)

    def _find_next_cell(self) -> Optional[Tuple[int, int]]:
        """Returns the next empty cell"""
        for y in range(9):
            for x in range(9):
                if self.board[y][x] == '.':
                    return (x, y)
        return None

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board

        previous_cells: List[Tuple[int, int]] = []
        current_cell = self._find_next_cell()
        previous_cells.append(current_cell)

        while current_cell is not None:

            # Increment current cell number
            x, y = current_cell
            next_number = int(board[y][x]) + 1 if board[y][x] != '.' else 1

            # Backtrack to previous cell because all numbers tried
            if next_number > 9:
                board[y][x] = '.'
                current_cell = previous_cells.pop()
                continue

            board[y][x] = str(next_number)

            # If board is valid then carry on to the next cell
            if self.is_board_valid(y, x):

                previous_cells.append(current_cell)
                current_cell = self._find_next_cell()


class TestSolution(unittest.TestCase):

    def test_example(self):

        board = [
            ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
            ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
            ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
            ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
            ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
            ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
            ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
            ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
            ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
        ]

        solution = Solution()
        solution.solveSudoku(board)

        expected_board = [
            ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
            ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
            ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
            ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
            ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
            ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
            ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
            ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
            ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
        ]

        self.assertListEqual(board, expected_board)
