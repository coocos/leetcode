import unittest
from typing import List


class Solution:
    """
    Since it's possible to reach all nodes via other nodes expect the nodes with
    no incoming edges, the solution with the minimum number of nodes is equal to
    the set of nodes with no incoming edges. This is because you can reach all the
    other nodes directly or indirectly via the nodes with no incoming edges.
    """

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = {i: {"in": [], "out": []} for i in range(n)}
        for start, end in edges:
            graph[start]["out"].append(end)
            graph[end]["in"].append(start)
        return [node for node, edges in graph.items() if not edges["in"]]


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        n = 6
        edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        self.assertListEqual(Solution().findSmallestSetOfVertices(n, edges), [0, 3])
