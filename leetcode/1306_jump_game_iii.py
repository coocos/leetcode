import unittest
import collections
from typing import List, FrozenSet


class Solution:
    """
    This solution is based on doing a recursive depth-first traversal of
    the possible routes to the index with the zero value. The recursion
    starts at the given index and checks whether the given index contains
    the zero value. If not then two recursive calls are made to indices
    (i + arr[i]) and (i - arr[i]) if those indices are within array bounds.
    The recursion is terminated by returning True if it encounters an index
    with the zero value. Otherwise the recursion continues until all possible
    paths have been exhausted.

    In order to avoid a stack overflow due to cyclic paths each recursive
    call receives a frozen set of previously visited indices. If the current
    index is already present in the set of visited points then the recursion
    terminates for that particular path.
    """

    def canReach(
        self, arr: List[int], start: int, visited: FrozenSet[int] = frozenset()
    ) -> bool:

        if arr[start] == 0:
            return True
        if start in visited:
            return False

        visited = visited | {start}
        forward = start + arr[start]
        back = start - arr[start]
        can_reach_forward = (
            self.canReach(arr, forward, visited) if 0 <= forward < len(arr) else False
        )
        can_reach_back = (
            self.canReach(arr, back, visited) if 0 <= back < len(arr) else False
        )
        return can_reach_forward or can_reach_back


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertTrue(Solution().canReach([4, 2, 3, 0, 3, 1, 2], 5))

    def test_second_example(self):

        self.assertTrue(Solution().canReach([4, 2, 3, 0, 3, 1, 2], 0))

    def test_third_example(self):

        self.assertFalse(Solution().canReach([3, 0, 2, 1, 2], 2))

