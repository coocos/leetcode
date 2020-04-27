import unittest


class Solution:
    """
    This solution iterates over the string and uses a stack to keep
    track of the parentheses. If the current token under iteration
    is "(" then it's pushed to the stack. If the current token is ")"
    then the stack is popped. If the stack is empty when it's popped,
    the algorithm increments a counter keeping track of missing opening
    parentheses by 1 as this can only happen if the string was missing
    an opening parenthesis at some point. Once the string has been exhausted,
    the counter plus the size of the stack equals the amount of missing
    parentheses.
    """
    def minAddToMakeValid(self, S: str) -> int:

        stack = []
        missing_opening = 0
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                try:
                    stack.pop()
                except IndexError:
                    missing_opening += 1
        return missing_opening + len(stack)


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(Solution().minAddToMakeValid('())'), 1)

    def test_second_example(self):
        self.assertEqual(Solution().minAddToMakeValid('((('), 3)

    def test_third_example(self):
        self.assertEqual(Solution().minAddToMakeValid('()'), 0)

    def test_fourth_example(self):
        self.assertEqual(Solution().minAddToMakeValid('()))(('), 4)
