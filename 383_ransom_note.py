import unittest
import collections

from typing import DefaultDict


class Solution:
    """
    This solution constructs a dictionary with all the available letters
    and their counts. Once the dictionary has been constructed, the ransom
    note is iterated over and the counts in the dictionary are decremented
    for each letter found in the ransom note. If a letter is not found
    in the dictionary or its count gets decremented to less than 0 then
    the ransom note is impossible to construct.
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        available_letters: DefaultDict[str, int] = collections.defaultdict(int)
        for letter in magazine:
            available_letters[letter] += 1

        for letter in ransomNote:
            available_letters[letter] -= 1
            if available_letters[letter] < 0:
                return False

        return True


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertFalse(Solution().canConstruct("aa", "ab"))

    def test_second_example(self):

        self.assertTrue(Solution().canConstruct("aa", "aab"))
