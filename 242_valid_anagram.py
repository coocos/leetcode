import unittest
import collections

from typing import DefaultDict


class Solution:
    """
    This solution first iterates the first string and adds all the letters
    and how often they appear in the string to a dictionary. Then the second
    string is iterated upon and for each letter the value in the dictionary
    is decremented. If decrementing the value results in the value being zero
    then the letter is removed from the dictionary. After this process is done
    the dictionary should not contain a single entry if the words formed an
    anagram.
    """
    def isAnagram(self, s: str, t: str) -> bool:

        letter_counts: DefaultDict[str, int] = collections.defaultdict(int)

        for letter in s:
            letter_counts[letter] += 1
        for letter in t:
            letter_counts[letter] -= 1
            if letter_counts[letter] == 0:
                del letter_counts[letter]

        return len(letter_counts) == 0


class TestSolution(unittest.TestCase):

    def test_true_example(self):

        self.assertTrue(Solution().isAnagram('anagram', 'nagaram'))

    def test_false_example(self):

        self.assertFalse(Solution().isAnagram('rat', 'car'))

    def test_different_lengths(self):

        self.assertFalse(Solution().isAnagram('a', 'ab'))
