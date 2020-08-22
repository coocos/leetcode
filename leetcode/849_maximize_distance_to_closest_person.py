import sys
import unittest
from typing import List


class Solution:
    """
    This solution scans the seats in two passes. First the seats
    are scanned from left to right while keeping track of the
    distance from each free seat to the nearest reserved seat on the
    left. Then the scan is performed from right to left. Finally
    the two scans are combined by finding the free seat which
    maximizes both distances to the left and right.
    """

    def maxDistToClosest(self, seats: List[int]) -> int:

        distances = {}

        # Scan from left to right
        i = 0
        last_from_left = -sys.maxsize
        while i < len(seats):
            if seats[i]:
                last_from_left = i
            else:
                distances[i] = [i - last_from_left]
            i += 1

        # Scan from right to left
        j = len(seats) - 1
        last_from_right = sys.maxsize
        while j >= 0:
            if seats[j]:
                last_from_right = j
            else:
                distances[j].append(last_from_right - j)
            j -= 1

        return min(
            max(distances.values(), key=lambda left_and_right: min(left_and_right))
        )


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)

    def test_second_example(self):
        self.assertEqual(Solution().maxDistToClosest([1, 0, 0, 0]), 3)
        pass

    def test_two_seat_example(self):
        self.assertEqual(Solution().maxDistToClosest([0, 1]), 1)

