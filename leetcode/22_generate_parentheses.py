import unittest
from typing import List


class Solution:
    """
    This recursive solution constructs all the strings by maintaining a string
    with remaining closing parentheses and another string with remaining
    opening parentheses, as well as keeping track of the currently built
    sequence.

    The first call to the function starts with a "(" string. The successive
    calls append a closing parenthesis or an opening parenthesis from the
    remaining parentheses to the string and call the function recursively
    again. Finally once there are no parentheses left the string is added
    to a list and the recursion is terminated.

    Note that if at any point in the recursion there are more opening
    parentheses left than there are closing parentheses then the recursion
    can be immediately terminated as such a sequence is invalid.
    """
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(opening: str, closing: str, string: str, parentheses: List[str]) -> None:

            if not closing and not opening:
                parentheses.append(string)
                return
            if closing and not opening:
                generate(opening, closing[1:], string + closing[0], parentheses)
                return
            # More opening parentheses indicates an invalid sequence
            if len(closing) < len(opening):
                return

            generate(opening[1:], closing, string + opening[0], parentheses)
            generate(opening, closing[1:], string + closing[0], parentheses)

        parentheses: List[str] = []
        generate("(" * (n - 1), ")" * n, "(", parentheses)
        return parentheses


class TestSolution(unittest.TestCase):

    def test_basic_parentheses(self):

        parentheses = [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()"
        ]
        self.assertListEqual(Solution().generateParenthesis(3), parentheses)
