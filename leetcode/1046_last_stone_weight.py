import unittest
import heapq
from typing import List, Sequence


class Solution:
    """
    This solution uses a max heap to form a priority queue of the stones
    prioritized by their weight. This queue is emptied two stones at a time
    and the stones are smashed until only one stone remains or the queue is
    empty.

    Note that heap implementation provided by the Python standard library
    is a min heap, i.e. the heap will return the smallest item when it's
    popped. To work around this the weights of the stones are negated before
    they are pushed to the heap, effectively turning the min heap into
    a max heap.
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        heap: List[int] = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = abs(heapq.heappop(heap))
            second = abs(heapq.heappop(heap))
            if first == second:
                continue
            heapq.heappush(heap, -abs(first - second))

        return abs(heap[0]) if heap else 0


class TestSolution(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]), 1)
