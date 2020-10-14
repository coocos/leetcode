import unittest


class Solution:
    """
    This solution simply iterates over the string, pushing
    opening parentheses to a stack and popping the stack when it
    encounters closing parentheses. The maximum depth is the maximum
    size of the stack encountered during the iteration.
    """

    def maxDepth(self, s: str) -> int:

        depth = 0
        stack = []

        for token in s:
            if token == "(":
                stack.append(token)
            elif token == ")":
                depth = max(depth, len(stack))
                stack.pop()

        return depth


class TestSolution(unittest.TestCase):
    def test_string_with_no_parentheses(self):
        self.assertEqual(Solution().maxDepth("s"), 0)

    def test_string_with_nested_parenthese(self):
        self.assertEqual(Solution().maxDepth("(1+(2*3)+((8)/4))+1"), 3)
