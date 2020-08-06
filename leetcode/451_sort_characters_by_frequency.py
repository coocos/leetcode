import unittest
import collections
from typing import DefaultDict


class Solution:
    """
    This solution is based on doing a bucket sort. First the string is
    iterated over to construct a dictionary of how many times each letter
    appears in the string. Then a list of buckets equal to the size of the
    string is constructed and the dictionary is iterated over while placing
    each letter in a bucket inxeded according to the letter's frequency /
    count. Finally the list of buckets is iterated over in reverse to
    form the string.

    Note that it's also possible to use collections.Counter.most_common()
    to perform this operation in a neater way.
    """

    def frequencySort(self, s: str) -> str:

        counts: DefaultDict[str, int] = collections.defaultdict(int)
        for char in s:
            counts[char] += 1

        buckets = ["" for _ in s]
        for char, count in counts.items():
            buckets[count - 1] += char * count

        return "".join(char for char in reversed(buckets) if char)


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().frequencySort("tree"), "eetr")

    def test_repeating_example(self):

        self.assertEqual(Solution().frequencySort("eeeee"), "eeeee")
