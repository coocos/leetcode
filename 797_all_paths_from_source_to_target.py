import unittest
from typing import List


class Solution:
    """
    This solution uses a simple depth-first search to find all the
    paths. Since the graph is guaranteed to be acyclic the algorithm
    simply constructs all the paths from the first node to the last node
    by passing along the path to each succssive recursive call until the
    last node is reached. At that point the constructed path is appended
    to a list of all possible paths.
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def search(node: int, path: List[int], all_paths: List[List[int]]):

            # Reached the final node
            if node == len(graph) - 1:
                all_paths.append(path + [node])
                return

            for next_node in graph[node]:
                search(next_node, path + [node], all_paths)

        all_paths: List[List[int]] = []
        search(0, [], all_paths)
        return all_paths


class TestSolution(unittest.TestCase):

    def test_basic_example(self):

        graph = [
            [1, 2],
            [3],
            [3],
            []
        ]
        paths = [
            [0, 1, 3],
            [0, 2, 3]
        ]
        self.assertListEqual(Solution().allPathsSourceTarget(graph), paths)
