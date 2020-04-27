import unittest
from typing import Tuple


class Solution:
    """
    This recursive solution works by inspecting the next outermost pair of
    parentheses in the string. If the next outermost parentheses are just
    '()' then we can terminate the recursion and return 1 plus whatever the
    value is for the the rest of the string. On the other hand if the
    next outermost pair of parentheses contains a nested expression then
    we need to return 2 * the nested expression plus whatever the value
    is for the rest of the string.
    """
    def scoreOfParentheses(self, S: str) -> int:

        def extract_surrounding_parentheses(string) -> Tuple[int, int]:
            """
            Extracts the indices which indicate the outermost parentheses
            surrounding this string, i.e. given (()) it will return (0, 3).
            """
            count = 0
            for i, s in enumerate(string):
                if s == '(':
                    count += 1
                else:
                    count -= 1
                if not count:
                    break
            return 0, i

        if not S:
            return 0

        start, close = extract_surrounding_parentheses(S)

        # The next pair of parentheses are just ()
        if close - start == 1:
            return 1 + self.scoreOfParentheses(S[close + 1:])
        # The next pair of parentheses are  a nested expression like (()())
        else:
            return (2 * self.scoreOfParentheses(S[start + 1: close]) +
                    self.scoreOfParentheses(S[close + 1:]))


class TestSolution(unittest.TestCase):

    def test_single_pair(self):

        self.assertEqual(Solution().scoreOfParentheses('()'), 1)

    def test_nested_pairs(self):

        self.assertEqual(Solution().scoreOfParentheses('(())'), 2)

    def test_sequential_pairs(self):

        self.assertEqual(Solution().scoreOfParentheses('()()'), 2)

    def test_mixed_pairs(self):

        self.assertEqual(Solution().scoreOfParentheses('(()())'), 4)

    def test_complex_example(self):

        self.assertEqual(Solution().scoreOfParentheses('(()(()))'), 6)

    def test_failing_example(self):

        self.assertEqual(Solution().scoreOfParentheses('(())()'), 3)
