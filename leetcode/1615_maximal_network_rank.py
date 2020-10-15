import unittest
import itertools
import collections
from typing import List


class Solution:
    """
    This solution uses brute force. First a graph is constructed where cities
    are the nodes and the roads to neighbouring cities are the edges. Then the
    algorithm iterates over all possible pairs of cities and computes the
    total amount of outgoing edges for each pair. The largest edge count for a
    pair is the maximal network rank.

    Note that the pair of cities might be connected. In that case you need to
    deduct the maximal rank by one in order to avoid counting the edge between
    them twice.
    """

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(set)
        for start, end in roads:
            graph[start].add(end)
            graph[end].add(start)

        max_rank = 0
        for first, second in itertools.combinations(graph.keys(), 2):
            rank = len(graph[first]) + len(graph[second])
            # Do not count shared road twice
            if first in graph[second] and second in graph[first]:
                rank -= 1
            max_rank = max(max_rank, rank)

        return max_rank


class TestSolution(unittest.TestCase):
    def test_network_with_four_cities(self):
        n = 4
        roads = [[0, 1], [0, 3], [1, 2], [1, 3]]
        self.assertEqual(Solution().maximalNetworkRank(n, roads), 4)

    def test_network_with_five_cities(self):
        n = 5
        roads = [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]]
        self.assertEqual(Solution().maximalNetworkRank(n, roads), 5)

    def test_network_with_one_road(self):

        n = 2
        roads = [[1, 0]]
        self.assertEqual(Solution().maximalNetworkRank(n, roads), 1)

    def test_disconnected_network_with_eight_cities(self):
        n = 8
        roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
        self.assertEqual(Solution().maximalNetworkRank(n, roads), 5)
