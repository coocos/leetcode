import unittest
from typing import List


class Solution:
    """
    This solution uses dynamic programming to compute the minimum cost for
    reaching top of the stairs. The basic gist is to realize that the
    minimum cost for reaching the i'th step is the minimum cost for
    reaching either step i - 2 or step i - 1 plus the cost of step i itself.
    Therefore if you set step 0 and step 1 as the first steps you can compute
    the minimum cost to reach step 2 by taking the smallest of the two
    (and adding the cost of step 2 itself) and then doing the same thing for
    step 3 etc.

    To save memory you can also just keep track of the previous step and
    the step before that one as the costs used to reach the steps before the
    last two are irrelevant.
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        first, second = cost[:2]
        cost = cost[2:] + [0]  # Zero as last step indicates top floor

        for i, step_cost in enumerate(cost):
            step_cost = min(first + step_cost, second + step_cost)
            first = second
            second = step_cost

        return second


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        steps = [10, 15, 20]
        self.assertEqual(Solution().minCostClimbingStairs(steps), 15)

    def test_second_example(self):

        steps = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        self.assertEqual(Solution().minCostClimbingStairs(steps), 6)
