import unittest


class Solution:
    """
    This solution simply pushes opening brackets to a stack and whenever
    it encounters a closing bracket it pops the previous opening bracket from
    the stack. If the bracket is of the wrong type then the brackets are mixed
    and the string is not valid. If the entire string has been processed and
    the stack still has opening brackets left then the string is not valid as
    some of the brackets have not been closed.
    """
    def isValid(self, s: str) -> bool:

        stack = []
        matching_brackets = {
                '}': '{',
                ']': '[',
                ')': '('
        }

        for bracket in s:
            # Opening brackets
            if bracket in '([{':
                stack.append(bracket)
            # Closing brackets
            else:
                try:
                    closing_bracket = stack.pop()
                except IndexError:
                    return False
                # Bracket needs to match the opening bracket
                if (matching_brackets[bracket] != closing_bracket):
                    return False

        # Brackets are not balanced as some opening brackets were not closed
        return not stack


class TestSolution(unittest.TestCase):

    def test_two_basic_brackets(self):
        self.assertTrue(Solution().isValid('()'))

    def test_multiple_bracket_types(self):
        self.assertTrue(Solution().isValid('()[]{}'))

    def test_two_invalid_brackets(self):
        self.assertFalse(Solution().isValid('(]'))

    def test_brackets_in_wrong_order(self):
        self.assertFalse(Solution().isValid('([)]'))

    def test_nested_brackets(self):
        self.assertTrue(Solution().isValid('{[]}'))

    def test_single_bracket(self):
        self.assertFalse(Solution().isValid(']'))
