import unittest


class Solution:
    """
    Two solutions are provided for this answer. The first recursive
    answer works by calling itself recursively and always decrementing the
    amount of steps left by one and two. Once the recursion ends up in a
    situation where the amount of steps is left is zero we've hit the
    top of the stairs and can return 1. The function then sums up the
    numbers returned by both of its recursive function calls and returns
    the sum. This recursive solution will most likely time out when
    submitted to leetcode, thus the need for a second solution.

    The second, faster solution uses dynamic programming. The problem
    can be partitioned into a subset of smaller problems by realizing
    that the amount of ways to reach the nth step is equal to the the
    amount of ways to reach the (n - 1)th step plus the amount of ways
    to reach the (n - 2)th step. This is because the steps can only be
    ascended by taking one step forward or two steps forward. Thus
    you can iterate over the steps and keep summing up the amount of
    ways used to reach the previous step and the step before that one.
    Once you reach the last step you're done.
    """
    def dynamic(self, n: int) -> int:

        first, second = 1, 1
        for i in range(1, n):
            temp = second
            second = first + second
            first = temp

        return second

    def recursive(self, n: int, left: int) -> int:
        """This recursive solution works but it's slow for large inputs"""
        if left < 0:
            return 0
        elif left == 0:
            return 1
        else:
            return self.recursive(n, left - 1) + self.recursive(n, left - 2)

    def climbStairs(self, n: int) -> int:
        # return self.recursive(n, n)
        return self.dynamic(n)


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(Solution().climbStairs(2), 2)

    def test_second_example(self):

        self.assertEqual(Solution().climbStairs(3), 3)

    def test_minimal_example(self):

        self.assertEqual(Solution().climbStairs(1), 1)

    def test_larger_example(self):

        self.assertEqual(Solution().climbStairs(5), 8)

    def test_large_example(self):
        self.assertEqual(Solution().climbStairs(35), 14930352)
