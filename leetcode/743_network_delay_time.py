import unittest
import collections

from typing import List, Dict, DefaultDict


class Solution:
    """
    This solution uses breadth-first search to visit all routes in the
    network while keeping track of the shortest time periods taken to visit
    each node.

    Note that using something like Dijkstra's algorithm instead of pure
    breadth-first search would be faster.
    """
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        # Construct a dictionary of nodes and links
        nodes: DefaultDict[int, List] = collections.defaultdict(list)
        for node, link, time in times:
            nodes[node].append((link, time))

        node_times: Dict[int, int] = {}
        queue = collections.deque([(K, 0)])

        while queue:

            node, time = queue.popleft()

            # If we arrived at this node later than from some previous route
            # then there is no need to explore this path further as it's slower
            if node in node_times and node_times[node] < time:
                    continue

            node_times[node] = time

            for next_node, link_time in nodes[node]:
                node_visit_time = time + link_time

                if next_node in node_times:
                    # Prune paths which have already been explored faster
                    if node_visit_time < node_times[next_node]:
                        queue.append((next_node, node_visit_time))
                else:
                    queue.append((next_node, node_visit_time))

        if len(node_times) < N:
            return -1

        return max(node_times.values())


class TestSolution(unittest.TestCase):

    def test_trivial_network(self):

        times = [
            [2, 1, 1],
            [2, 3, 1],
            [3, 4, 1],
        ]
        self.assertEqual(Solution().networkDelayTime(times, 4, 2), 2)

    def test_impossible_network(self):

        times = [
            [1, 2, 1]
        ]
        self.assertEqual(Solution().networkDelayTime(times, 2, 2), -1)

    def test_network_with_multiple_routes(self):
        times = [
            [1, 2, 1],
            [2, 3, 2],
            [1, 3, 4]
        ]
        self.assertEqual(Solution().networkDelayTime(times, 3, 1), 3)

    def test_looping_network(self):
        times = [
            [1, 2, 1],
            [2, 1, 3]
        ]
        self.assertEqual(Solution().networkDelayTime(times, 2, 2), 3)

    def test_failing_example(self):
        times = [
            [1, 2, 1],
            [2, 3, 2],
            [1, 3, 2]
        ]
        self.assertEqual(Solution().networkDelayTime(times, 3, 1), 2)
