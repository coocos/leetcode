import unittest
from typing import List


class Solution:
    """
    The key to understanding this solution is to stare at the
    visualization picture long enough to realize that each point
    will trap as much water as the smallest of the two highest
    elevated points to the left and right of it:

       #
     #~#~~#
    #####~###

    Additionally to compensate for the fact that the point itself
    might be elevated, you need to reduce from this value the height
    of the elevated point itself.

    However, if you iterate over the elevation map and continuously
    find the largest value to the left of the current index and the
    largest value to the right of the current index the algorithm as
    a whole will be very slow with large inputs. Therefore a cache is
    first built which contains the largest elevation to the left of
    each index and the largest elevation to the right of each index.
    Then as you're iterating over the elevation map you can just look
    up the largest value to the left and the largest value to the right
    of each point in O(1) time.
    """
    def trap(self, height: List[int]) -> int:

        maxes: List[List[int]] = []

        # Precompute the highest point to the left for all points
        left_max = 0
        for h in height:
            maxes.append([left_max])
            if h > left_max:
                left_max = h

        # Precompute the highest point to the right for all points
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            maxes[i].append(right_max)
            if h > right_max:
                right_max = h

        total_water = 0
        for x, h in enumerate(height):
            left_max, right_max = maxes[x]
            water = max(min(left_max, right_max) - h, 0)
            total_water += water

        return total_water


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        elevation_map = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(Solution().trap(elevation_map), 6)

    def test_border_walls(self):

        elevation_map = [2, 0, 2]
        self.assertEqual(Solution().trap(elevation_map), 2)

    def test_large_input(self):

        elevation_map = [0, 1, 2, 0, 2, 1] * 1000
        self.assertEqual(Solution().trap(elevation_map), 5996)
