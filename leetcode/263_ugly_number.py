import unittest


class Solution:
    """
    This recursive solution simply checks whether the number is
    dividable by any factor and if so, it recurses deeper by
    dividing the number and repeating the process. If at any point
    in the recursion the number becomes equal to 1 then the number
    can be considered ugly.
    """

    def isUgly(self, num: int) -> bool:

        if num < 1:
            return False

        if num == 1:
            return True

        for factor in (2, 3, 5):
            if num % factor == 0 and self.isUgly(num // factor):
                return True

        return False


class TestSolution(unittest.TestCase):
    def test_first_example(self):
        self.assertTrue(Solution().isUgly(6))

    def test_second_example(self):
        self.assertTrue(Solution().isUgly(8))

    def test_third_example(self):
        self.assertFalse(Solution().isUgly(14))
