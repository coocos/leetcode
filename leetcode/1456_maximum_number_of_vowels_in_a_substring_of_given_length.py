import unittest


class Solution:
    """
    This solution maintains a sliding window of size k which
    keeps track of the amount of vowels within the window. First
    the algorithm computes the initial window and its amount of
    vowels. Then it moves the window one letter at a time and
    decrements or increments the vowel count based on whether the
    the letters entering or exiting the window are vowels or not.
    """

    def maxVowels(self, s: str, k: int) -> int:

        vowels = {"a", "e", "i", "o", "u"}
        vowels_in_window = 0

        # Compute the initial window
        vowels_in_window = sum(letter in vowels for letter in s[:k])
        max_vowels = vowels_in_window

        # Move window and keep track of vowel count
        for right in range(k, len(s)):
            left = right - k
            if s[right] in vowels:
                vowels_in_window += 1
            if s[left] in vowels:
                vowels_in_window -= 1
            max_vowels = max(max_vowels, vowels_in_window)

        return max_vowels


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().maxVowels("abciiidef", 3), 3)

    def test_second_example(self):

        self.assertEqual(Solution().maxVowels("aeiou", 2), 2)

    def test_third_example(self):

        self.assertEqual(Solution().maxVowels("leetcode", 3), 2)

    def test_long_example(self):

        self.assertEqual(
            Solution().maxVowels("ibpbhixfiouhdljnjfflpapptrxgcomvnb", 33), 7
        )

    def test_failing_example(self):

        self.assertEqual(Solution().maxVowels("weallloveyou", 7), 4)
