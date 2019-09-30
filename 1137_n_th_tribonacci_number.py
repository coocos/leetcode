import unittest


class Solution:
    """
    This solution is based on dynamic programming. Essentially it
    always stores the last three Tribonacci numbers and keeps summing
    them together until the nth number is reached. This way you do not
    end up recomputing the same numbers multiple times like you would
    with a basic recursive approach without memoization.
    """
    def tribonacci(self, n: int) -> int:

        first, second, third = 0, 1, 1

        for _ in range(n):
            temp = first
            first = second
            second = third
            third = temp + first + second

        return first


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(Solution().tribonacci(25), 1389537)
