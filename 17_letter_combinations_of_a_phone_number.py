import unittest

from typing import List


# Map telephone numbers to letters
NUMBERS_TO_LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    """
    This solution is based on a recursive approach where the digits
    are split into a tree of letters. Each recursive call of the function
    receives the digits remaining as well as the string formed by the previous
    letters. The function picks the first of the remaining digits, maps
    it to the possible letters and calls itself recursively for each letter,
    passing the rest of the digits as well as the currently formed string
    plus the letter as arguments.

    Once there are no more digits left the formed string is appended
    to a list of combinations and the recursion is terminated for that
    particular branch.
    """
    def create_combinations(self,
                            numbers: str,
                            string: str,
                            combinations: List[str]) -> None:

        # No numbers left - this particular string is now complete
        if not numbers:
            combinations.append(string)
            return

        for letter in NUMBERS_TO_LETTERS[numbers[0]]:
            self.create_combinations(numbers[1:],
                                     string + letter,
                                     combinations)

    def letterCombinations(self, digits: str) -> List[str]:

        combinations: List[str] = []
        if digits:
            self.create_combinations(digits, '', combinations)

        return combinations


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        expected = [
            "ad",
            "ae",
            "af",
            "bd",
            "be",
            "bf",
            "cd",
            "ce",
            "cf"
        ]
        self.assertListEqual(Solution().letterCombinations('23'), expected)

    def test_with_empty_input(self):
        self.assertListEqual(Solution().letterCombinations(''), [])
