import unittest
import collections

from typing import Dict


class Solution:
    """
    This solution is based on a sliding window. First a dictionary
    is constructed containing the counts for each letter in s1.
    Next s2 is iterated over while maintaining a sliding window using
    two pointers: one at the head of the iteration and one len(s1)
    behind the head. The range between these two pointers forms the
    sliding window. If a letter enters the window and is also present
    in the previously constructed dictionary, the count of that letter
    is decremented by one. On the other hand if a letter exits the window,
    the count of that letter is incremented by one. If at any point
    during the iteration all the letter counts in the dictionary are zero,
    it means that the letters in the current window contain a permutation
    of s1.
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        letters: Dict[str, int] = collections.defaultdict(int)
        for letter in s1:
            letters[letter] += 1

        window_size = len(s1)
        head = 0

        while head < len(s2):

            entering = s2[head]
            if entering in letters:
                letters[entering] -= 1
            if head >= window_size:
                exiting = s2[head - window_size]
                if exiting in letters:
                    letters[exiting] += 1

            if all(count == 0 for count in letters.values()):
                return True

            head += 1

        return False


class TestSolution(unittest.TestCase):
    def test_true_example(self):

        s1 = "ab"
        s2 = "eidbaooo"
        self.assertTrue(Solution().checkInclusion(s1, s2))

    def test_false_example(self):
        s1 = "ab"
        s2 = "eidboaoo"
        self.assertFalse(Solution().checkInclusion(s1, s2))

    def test_three_letter_true_example(self):

        s1 = "adc"
        s2 = "dcda"
        self.assertTrue(Solution().checkInclusion(s1, s2))

    def test_substring_being_longer_than_string(self):

        s1 = "ab"
        s2 = "a"
        self.assertFalse(Solution().checkInclusion(s1, s2))
