import unittest
import collections
from typing import DefaultDict


class Solution:
    """
    The algorithm starts by first counting how many times each letter
    appears in the string. Then the length of longest palindrome can
    be computed by counting how many times each letter can be divided
    by two and finally adding a single letter if a single letter still
    remains unused.

    For example, let's say we have a string like 'aaaabbbc'. You can
    construct the palindrome by first taking two a's and putting them
    to the start and the end of an empty string. Afterwards you still have
    'aabbbc' left. From that you can choose either 'bb' or 'aa' next
    so let's say you choose 'bb'. Now your palindrome looks like 'abba'
    and you still have 'aabc' left. Now you can again choose 'aa' and
    you will have a palindrome like 'abaaba' and 'bc' leftover. Since
    there are no more duplicate characters left unused you can choose
    either 'b' or 'c' and your palindrome is complete. The algorithm
    performs these very same steps but it does not actually construct
    the palindrome - it just computes how long the palindrome will be.
    """
    def longestPalindrome(self, s: str) -> int:

        letters_by_count: DefaultDict[str, int] = collections.defaultdict(int)
        for letter in s:
            letters_by_count[letter] += 1
        length = 0

        for letter, count in letters_by_count.items():
            if count % 2 == 0:
                length += count
                letters_by_count[letter] = 0
            elif count > 1:
                length += (count // 2) * 2
                letters_by_count[letter] = 1

        # There's still space for a single letter in the middle
        for count in letters_by_count.values():
            if count == 1:
                length += 1
                break

        return length


class TestSolution(unittest.TestCase):

    def test_example_palindrome(self):

        string = "abccccdd"
        self.assertEqual(Solution().longestPalindrome(string), 7)

    def test_single_letter_palindrome(self):

        string = "abc"
        self.assertEqual(Solution().longestPalindrome(string), 1)

    def test_two_letter_palindrome(self):

        string = "bb"
        self.assertEqual(Solution().longestPalindrome(string), 2)

    def test_yet_another_palindrome(self):

        string = "abcba"
        self.assertEqual(Solution().longestPalindrome(string), 5)

    def test_bananas(self):

        string = "bananas"
        self.assertEqual(Solution().longestPalindrome(string), 5)
