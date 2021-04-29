import collections
import unittest


class Solution:
    """
    This solution uses a double-ended queue to simulate a ring.
    Essentially the double-ended queue is just rotated according
    to the rules of the game and the head of the queue is always
    popped after the rotation. This continues until the queue
    contains just a single friend.
    """

    def findTheWinner(self, n: int, k: int) -> int:

        circle = collections.deque(range(1, n + 1))
        while len(circle) > 1:
            circle.rotate(-(k - 1))
            circle.popleft()
        return circle.pop()


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().findTheWinner(5, 2), 3)

    def test_second_example(self):

        self.assertEqual(Solution().findTheWinner(6, 5), 1)
