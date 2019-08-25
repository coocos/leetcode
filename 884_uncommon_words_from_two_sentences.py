import unittest
import collections
from typing import List, DefaultDict


class Solution:
    """
    This solution combines the words from the two sentences and counts
    their occurrences using a dictionary. Once the dictionary has been
    filled then it returns all the words which appeared only once.
    """
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        counts: DefaultDict[str, int] = collections.defaultdict(int)
        for word in A.split(" ") + B.split(" "):
            counts[word] += 1

        return [word for word, count in counts.items() if count == 1]


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        A = "this apple is sweet"
        B = "this apple is sour"
        expected = ["sweet", "sour"]
        self.assertCountEqual(Solution().uncommonFromSentences(A, B), expected)

    def test_second_example(self):

        A = "apple apple"
        B = "banana"
        expected = ["banana"]
        self.assertCountEqual(Solution().uncommonFromSentences(A, B), expected)

    def test_third_example(self):

        A = "s z z z s"
        B = "s z ejt"
        expected = ["ejt"]
        self.assertCountEqual(Solution().uncommonFromSentences(A, B), expected)
