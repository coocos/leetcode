import unittest


class Solution:
    """
    This solution simply maps the moves performed by the robot
    to increments or decrements in x and y coordinates. If after
    processing all the moves the robot is back at (0, 0) then
    we've come a full circle.
    """
    def judgeCircle(self, moves: str) -> bool:

        x, y = 0, 0

        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'R':
                x += 1
            else:
                x -= 1

        return x == 0 and y == 0


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertTrue(Solution().judgeCircle('UD'))

    def test_second_example(self):

        self.assertFalse(Solution().judgeCircle('LL'))
