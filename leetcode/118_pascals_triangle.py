import unittest
from typing import List


class Solution:
    """This is a simple iterative solution to Pascal's triangle"""

    def generate(self, numRows: int) -> List[List[int]]:

        rows: List[List[int]] = []

        for i in range(numRows):
            row = [1]
            for j in range(1, i):
                row.append(rows[-1][j - 1] + rows[-1][j])
            rows.append(row + [1] if i > 0 else row)

        return rows


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertListEqual(Solution().generate(5), expected)

    def test_with_zero(self):

        expected = []
        self.assertListEqual(Solution().generate(0), expected)
