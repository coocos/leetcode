import unittest
from typing import List


class Solution:
    """
    This solution simply slices the list into two, zips the slices together
    and then keeps appending numbers from the zipped iterable to a new list, finally
    returning the new list.
    """

    def shuffle(self, nums: List[int], n: int) -> List[int]:

        shuffled = []
        for x, y in zip(nums[:n], nums[n:]):
            shuffled.append(x)
            shuffled.append(y)
        return shuffled


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertListEqual(
            Solution().shuffle([2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7]
        )

