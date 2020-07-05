import unittest
import collections
from typing import DefaultDict


class Solution:
    """
    This solution first constructs a dictionary with a count for each letter
    for the given string. Then it divides the count of each letter with the
    count of each letter in the string "balloon". The amount of times the word
    "balloon" can be formed is the minimum value returned by the divisions.
    """

    def maxNumberOfBalloons(self, text: str) -> int:

        letters: DefaultDict[str, int] = collections.defaultdict(int)
        for letter in text:
            letters[letter] += 1

        balloons = letters["b"]
        for letter in "alloon":
            balloons = min(balloons, letters[letter] // "alloon".count(letter))

        return balloons


class TestSolution(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(Solution().maxNumberOfBalloons("loonbalxballpoon"), 2)

