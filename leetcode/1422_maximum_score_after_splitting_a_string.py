import unittest


class Solution:
    """
    This solution iterates over the string from the left to the right and constructs
    a dictionary where each key is an index to the string and the value indicates
    how many zeroes and ones are present to the left of the index. Once the dictionary
    has been constructed it is iterated over to find the position where the sum of

        zeroes_at_index + (total_ones - ones_at_index)
    
    is maximized.
    """

    def maxScore(self, s: str) -> int:
        counts = {}
        ones = 0
        zeroes = 0
        for i, digit in enumerate(s):
            if digit == "1":
                ones += 1
            else:
                zeroes += 1
            counts[i] = (ones, zeroes)
        total_ones = ones
        max_sum = -1
        for i in range(len(s) - 1):
            ones, zeroes = counts[i]
            sum_ = zeroes + (total_ones - ones)
            if sum_ > max_sum:
                max_sum = sum_
        return max_sum


class TestSolution(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(Solution().maxScore("011101"), 5)

    def test_second_example(self):
        self.assertEqual(Solution().maxScore("00111"), 5)

    def test_third_example(self):
        self.assertEqual(Solution().maxScore("1111"), 3)

    def test_fourth_example(self):
        self.assertEqual(Solution().maxScore("00"), 1)
