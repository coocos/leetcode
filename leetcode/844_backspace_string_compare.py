import unittest
from typing import List


class Solution:
    """
    This solution iterates over characters in both strings
    and creates stacks out of them. If the current character is
    not # then it is added to the stack. On the other hand if the
    character is # then the stack is popped if the stack is non-empty.
    Finally the stacks for both strings are compared and if they are
    equal then the strings are also equal.
    """

    def backspaceCompare(self, S: str, T: str) -> bool:
        def stackify(word: str) -> List[str]:
            stack: List[str] = []
            for char in word:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return stackify(S) == stackify(T)


class TestSolution(unittest.TestCase):
    def test_equal_strings(self):
        S = "ab#c"
        T = "ad#c"
        self.assertTrue(Solution().backspaceCompare(S, T))

    def test_unequal_strings(self):
        S = "a#c"
        T = "b"
        self.assertFalse(Solution().backspaceCompare(S, T))
