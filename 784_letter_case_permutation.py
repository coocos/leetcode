import unittest
from typing import List


class Solution:
    """
    This recursive solution consumes the string token by token, recursing
    into two different branches if the next token in the string is a
    character. Once the entire string has been consumed, it is added
    to the list and the recursion is terminated.
    """
    def permute(self,
                permutated: str,
                remaining: str,
                words: List[str]) -> None:

        if not remaining:
            words.append(permutated)
            return

        # Branch on letters
        if remaining[0].isalpha():
            self.permute(permutated + remaining[0].upper(), remaining[1:], words)
            self.permute(permutated + remaining[0].lower(), remaining[1:], words)
        # Skip over digits
        else:
            self.permute(permutated + remaining[0], remaining[1:], words)

    def letterCasePermutation(self, S: str) -> List[str]:

        permutations: List[str] = []
        self.permute('', S, permutations)
        return permutations


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        word = 'a1b2'
        permutations = ['a1b2', 'a1B2', 'A1b2', 'A1B2']
        self.assertCountEqual(Solution().letterCasePermutation(word), permutations)
