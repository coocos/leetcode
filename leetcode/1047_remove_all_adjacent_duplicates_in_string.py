import unittest
from typing import List


class Solution:
    """
    This solution uses a stack to remove the duplicate characters. The idea
    is to iterate over the string character by character and put each character
    on top of the stack unless the character is already on top of the stack.
    If that is the case then the stack is popped and the current character is
    discarded. Once this is done for the entire string all the adjacent duplicates
    have been eliminated.
    """

    def removeDuplicates(self, S: str) -> str:

        stack: List[str] = []
        for letter in S:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().removeDuplicates("abbaca"), "ca")

