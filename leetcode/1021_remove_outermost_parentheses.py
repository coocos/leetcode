import unittest


class Solution:
    """
    This solution uses the classic stack approach for finding the outermost
    parentheses. The string is iterated over and whenever an opening
    parenthesis is found, its position is pushed to a stack. When a
    closing parenthesis is found the stack is popped. If the stack is empty
    after the pop operation, that means the current parenthesis is the closing
    parenthesis of an outermost parentheses pair. Since the value popped from
    the stack is the starting position of the parentheses pair, the starting
    position can be used with the current position to slice the inner
    parentheses from string.  Once this is repeated for the entire string all
    the outermost parentheses have been removed.
    """
    def removeOuterParentheses(self, S: str) -> str:

        stack = []
        parentheses = ''
        for position, parenthesis in enumerate(S):
            if parenthesis == '(':
                stack.append(position + 1)
            else:
                start_position = stack.pop()
            if not stack:
                parentheses += S[start_position:position]
        return parentheses


class TestSolution(unittest.TestCase):

    def test_basic_example(self):

        parentheses = "(()())(())"
        self.assertEqual(Solution().removeOuterParentheses(parentheses), "()()()")

    def test_complex_example(self):

        parentheses = "(()())(())(()(()))"
        self.assertEqual(Solution().removeOuterParentheses(parentheses), "()()()()(())")

    def test_empty_example(self):
        parentheses = "()()"
        self.assertEqual(Solution().removeOuterParentheses(parentheses), "")
