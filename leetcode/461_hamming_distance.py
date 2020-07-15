import unittest


class Solution:
    """
    This solution does a bitwise XOR between the two numbers to
    create a number with the differing bits. Then the algorithm
    keeps checking the rightmost bit while shifting the resulting
    number to the right until the number eventually is equal to zero.
    """

    def hammingDistance(self, x: int, y: int) -> int:

        bits = 0
        xor = x ^ y
        while xor:
            bits += xor & 1
            xor = xor >> 1
        return bits


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().hammingDistance(1, 4), 2)

