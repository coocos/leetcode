import heapq
import unittest
from typing import List, Tuple


class Solution:
    """
    This solution iterates over points and uses a fixed size priority
    queue / heap to maintain a collection of the K closest points which
    is returned once all the points have been exhausted. Fixing the priority
    queue size to K elements will slightly improve the performance over a
    priority queue with N elements.

    Note that the distances are negated before they are put to the queue
    since heapq.heappushpop is used to maintain the size of queue and
    it always removes the closest element from the queue which we do not
    want to do. By negating the distance we can flip this behavior around
    and always remove the most distant element.
    """
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        points_by_distance: List[Tuple[int, List[int]]] = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if len(points_by_distance) < K:
                heapq.heappush(points_by_distance, (-distance, point))
            else:
                heapq.heappushpop(points_by_distance, (-distance, point))
        return [point for distance, point in heapq.nlargest(K, points_by_distance)]


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        points = [
            [3, 3],
            [5, -1],
            [-2, 4]
        ]
        closest = [
            [3, 3],
            [-2, 4]
        ]
        self.assertListEqual(Solution().kClosest(points, 2), closest)
