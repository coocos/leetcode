import unittest
from typing import List


class Solution:
    """
    This solution utilizes dynamic programming to iteratively solve
    the problem. First a list containing how many times each digit has been
    visited is constructed. Initially this list contains only ten values and
    they all are 1, i.e. each digit from 0 to 9 has been visited only once.
    This is the base case, i.e. n = 1. Next all the digits and their possible
    neighbours are iterated over and the times each digit has been visited is
    added to the times each neighbour has been visited. This step is performed
    n - 1 times resulting in the final list where the sum of all values in the
    list is equal to the amount of distinct digit combinations.

    Note that a recursive solution with memoization is perhaps easier to grasp
    but alas the leetcode test set includes some test cases where the digit count
    is several thousand digits long which results in a stack overflow with the Python
    default recursion limit.
    """

    def knightDialer(self, n: int) -> int:

        neighbours = {
            0: (4, 6),
            1: (8, 6),
            2: (7, 9),
            3: (8, 4),
            4: (9, 3, 0),
            5: tuple(),
            6: (7, 1, 0),
            7: (2, 6),
            8: (1, 3),
            9: (4, 2),
        }

        visit_count = [1] * 10
        for _ in range(n - 1):
            next_visit_count = [0] * 10
            for number in range(10):
                for neighbour in neighbours[number]:
                    next_visit_count[neighbour] += visit_count[number]
            visit_count = next_visit_count

        return sum(visit_count) % (10 ** 9 + 7)


class TestSolution(unittest.TestCase):
    def test_single_digit_number(self):

        self.assertEqual(Solution().knightDialer(1), 10)

    def test_two_digit_number(self):

        self.assertEqual(Solution().knightDialer(2), 20)

    def test_large_digit_number(self):

        self.assertEqual(Solution().knightDialer(3131), 136006598)
