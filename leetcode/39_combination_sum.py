import unittest
from typing import List


class Solution:
    """
    This solution uses a recursive depth-first approach to find the
    combinations. Essentially the recursive function creates a tree
    of paths starting from each candidate number and terminates the recursion
    whenever a path exceeds the target sum. If the recursion encounters
    a sum which matches the target then that particular path is added
    to the list of combinations.

    To avoid creating duplicate combinations / paths (i.e. [3, 2] and [2, 3]
    both sum to 5) only the candidates following the chosen candidate
    are passed to recursive function call since the preceding candidates
    have already been processed by previous calls. For example given
    candidates like [2, 3, 4] then there's no reason to examine the combination
    [4, 3, 2] if combinations [2, 3, ...] and [3, 4, ...] have been explored
    since they also contain that combination.
    """
    def combine(self,
                candidates: List[int],
                path: List[int],
                current_sum: int,
                target: int,
                combinations: List[List[int]]) -> None:

        if current_sum > target:
            return

        if current_sum == target:
            combinations.append(path)
            return

        for i, candidate in enumerate(candidates):
            self.combine(candidates[i:],  # Omit the preceding candidates
                         path + [candidate],
                         current_sum + candidate,
                         target,
                         combinations)

    def combinationSum(self,
                       candidates: List[int],
                       target: int) -> List[List[int]]:
        combinations: List[List[int]] = []
        self.combine(candidates, [], 0, target, combinations)
        return combinations


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        expected = [
            [7],
            [2, 2, 3]
        ]
        self.assertCountEqual(Solution().combinationSum([2, 3, 6, 7], 7), expected)

    def test_second_example(self):

        expected = [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ]
        self.assertCountEqual(Solution().combinationSum([2, 3, 5], 8), expected)
