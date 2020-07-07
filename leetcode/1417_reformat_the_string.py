import unittest
import itertools


class Solution:
    """
    This solution first iterates over the string and creates two lists: one for digits
    and one for letters. Then the two lists are zipped together and iterated over while
    putting one character from each list to a temporary list which forms the permutation.

    Note that you need to check that lengths of the two lists do not differ by more than
    one in order for the zipping procedure to work properly as the loop assumes that there's
    only a single None at most in the sequence.
    """

    def reformat(self, s: str) -> str:

        digits = []
        letters = []
        for character in s:
            if character.isalpha():
                letters.append(character)
            else:
                digits.append(character)
        if abs(len(digits) - len(letters)) > 1:
            return ""

        permutation = []
        more, less = (
            (letters, digits) if len(letters) > len(digits) else (digits, letters)
        )
        for more, less in itertools.zip_longest(more, less):
            permutation.append(more)
            if less:
                permutation.append(less)

        return "".join(permutation)


class TestSolution(unittest.TestCase):
    def assertPermutation(self, original: str, permutation: str) -> None:

        # FIXME: THis is wrong... This would mean that llab and lab are permutations
        self.assertEqual(set(original), set(permutation))
        for i in range(len(permutation) - 1):
            first, second = permutation[i], permutation[i + 1]
            self.assertTrue(
                (first.isdigit() and second.isalpha())
                or (first.isalpha() and second.isdigit())
            )

    def test_first_example(self):

        string = "a0b1c2"
        self.assertPermutation(string, Solution().reformat(string))

    def test_second_example(self):

        string = "leetcode"
        self.assertEqual(Solution().reformat(string), "")

    def test_fourth_example(self):

        string = "covid2019"
        self.assertPermutation(string, Solution().reformat(string))

    def test_fifth_example(self):

        string = "ab123"
        self.assertPermutation(string, Solution().reformat(string))
