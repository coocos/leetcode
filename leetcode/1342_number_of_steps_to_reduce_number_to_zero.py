import unittest


class Solution:
    """
    This recursive solution keeps track of the current step
    while recursing and either subtracts or divides the number
    as it goes deeper. Once the number is equal to zero the
    step is returned.
    """
    def numberOfSteps(self, num: int, step: int = 0) -> int:
        if num == 0:
            return step
        elif num % 2 == 0:
            return self.numberOfSteps(num // 2, step + 1)
        else:
            return self.numberOfSteps(num - 1, step + 1)


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().numberOfSteps(14), 6)

    def test_second_example(self):

        self.assertEqual(Solution().numberOfSteps(8), 4)
