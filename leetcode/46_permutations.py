import unittest
from typing import List


class Solution:
    """
    This solution recursively constructs all the permutations. This is done
    by taking a single number from the list of numbers and passing the rest of
    the numbers recursively to the permute function. Once the permute function
    receives a list with only a single number then the number is returned as a
    list of lists, thus terminating the recursion. As the recursion unwinds
    the calling function adds the previously selected single number to all
    the lists in the returned list of lists and returns this list of lists
    again.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]

        all_permutations: List[List[int]] = []
        for omitted in nums:
            permutations = self.permute([num for num in nums if num != omitted])
            for permutation in permutations:
                all_permutations.append(permutation + [omitted])
        return all_permutations


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        self.assertCountEqual(Solution().permute([1, 2, 3]), expected)
