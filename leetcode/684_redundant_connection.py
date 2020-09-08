import unittest
from typing import List


class DisjointSet:
    """Disjoint set / union find"""

    def __init__(self, n: int) -> None:
        self.nodes = list(range(n))

    def _root(self, node: int) -> int:
        """Returns the root of node"""
        x = node
        while self.nodes[x] != x:
            x = self.nodes[x]
        return x

    def find(self, first: int, second: int) -> bool:
        """Returns whether two nodes are connected"""
        return self._root(first) == self._root(second)

    def union(self, first: int, second: int) -> None:
        """Joins nodes"""
        self.nodes[self._root(first)] = self._root(second)


class Solution:
    """
    This solution uses a disjoint set / union find to find the redundant edge.
    The idea is to simply iterate over the edges and keep joining the nodes
    until you come upon an edge where the two nodes are already connected. This
    will be the redundant edge.
    """

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        disjoint_set = DisjointSet(len(edges))

        for edge in edges:
            start, end = edge[0] - 1, edge[1] - 1
            if disjoint_set.find(start, end):
                return edge
            disjoint_set.union(start, end)

        return []


class TestSolution(unittest.TestCase):
    def test_three_node_graph(self):

        edges = [[1, 2], [1, 3], [2, 3]]
        self.assertListEqual(Solution().findRedundantConnection(edges), [2, 3])

    def test_five_node_graph(self):

        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
        self.assertListEqual(Solution().findRedundantConnection(edges), [1, 4])
