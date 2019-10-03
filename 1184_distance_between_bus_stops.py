import unittest
from typing import List


class Solution:
    """
    This iterative solution simply performs two passes through the
    bus stop distances: one forwards and one backwards and compares
    the traversed distances and returns the smaller one. The modulo
    operator is used to wrap around the distance list if the pointer
    reaches either the end of the list during a forward pass or the
    beginning of the list during a backwards pass.
    """
    def distanceBetweenBusStops(self,
                                distance: List[int],
                                start: int,
                                destination: int) -> int:

        forwards = 0
        current = start
        while current != destination:
            forwards += distance[current]
            current = (current + 1) % len(distance)

        backwards = 0
        current = start
        while current != destination:
            current = (current - 1) % len(distance)
            backwards += distance[current]
            # No point in traversing further since going backwards
            # will cover more distance than going forwards
            if backwards >= forwards:
                break

        return min(backwards, forwards)


class TestSolution(unittest.TestCase):

    def test_forwards_example(self):

        distances = [1, 2, 3, 4]
        self.assertEqual(Solution().distanceBetweenBusStops(distances, 0, 1), 1)

    def test_backwards_example(self):

        distances = [1, 2, 3, 4]
        self.assertEqual(Solution().distanceBetweenBusStops(distances, 0, 3), 4)

    def test_starting_after_destination(self):

        distances = [7, 0, 1, 12, 11, 14, 5, 0]
        self.assertEqual(Solution().distanceBetweenBusStops(distances, 7, 2), 7)
