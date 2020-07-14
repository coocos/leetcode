import unittest
import collections
from typing import List


class Solution:
    """
    This solution performs a breadth-first traversal of the friend matrix
    one student at a time. Each breadth-first traversal adds all students
    it visits to a set of students which are then skipped in later traversals.
    Finally the amount of breadth-first traversals performed is the amount of
    friend circles.
    """

    def findCircleNum(self, M: List[List[int]]) -> int:

        visited = set()
        circles = 0

        for student in range(len(M)):

            if student in visited:
                continue

            queue = collections.deque([student])
            while queue:
                friend = queue.popleft()
                visited.add(friend)
                for next_friend, is_friends in enumerate(M[friend]):
                    if is_friends and next_friend not in visited:
                        queue.append(next_friend)

            circles += 1

        return circles


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        friends = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        self.assertEqual(Solution().findCircleNum(friends), 2)

    def test_second_example(self):

        friends = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
        self.assertEqual(Solution().findCircleNum(friends), 1)
