import unittest


class Solution:
    """
    This recursive solution keeps drinking the bottles while keeping track of the amount of
    empty bottles. If there are enough empty bottles then they are immediately converted into
    full bottles and the recursive calls repeat until no more full bottles are left.
    """

    def numWaterBottles(
        self, num_bottles: int, num_exchange: int, empty_bottles: int = 0
    ) -> int:

        if empty_bottles >= num_exchange:
            num_bottles += empty_bottles // num_exchange
            empty_bottles = empty_bottles % num_exchange

        if not num_bottles:
            return 0

        return num_bottles + self.numWaterBottles(
            0, num_exchange, empty_bottles + num_bottles
        )


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().numWaterBottles(9, 3), 13)

    def test_second_example(self):

        self.assertEqual(Solution().numWaterBottles(15, 4), 19)

    def test_third_example(self):

        self.assertEqual(Solution().numWaterBottles(5, 5), 6)

    def test_fourth_example(self):

        self.assertEqual(Solution().numWaterBottles(2, 3), 2)
