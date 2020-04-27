import unittest
from typing import List, Dict, Set


class Solution:
    """
    This solution is based on doing a depth-first traversal of the graph.
    Although the problem description is a bit unclear, essentially a node
    is considered safe only if it's impossible to get stuck in a cycle when
    starting the traverse from the node, i.e. all possible paths from the node
    eventually lead to a terminal node.

    The recursive algorithm essentially explores all paths starting from a
    node and if a cycle or an already known unsafe node is encountered, then
    the recursion is terminated and the node is considered unsafe. Otherwise
    the node is declared safe.

    A dictionary is used to keep track of whether nodes are safe or not.
    As the traversal progresses, the dictionary is updated so the traversal
    becomes increasingly faster as more nodes are visited and marked as either
    safe or unsafe.
    """
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def is_safe(node: int, visited: Set[int], nodes: Dict[int, bool]):

            # Node safety already known
            if node in nodes:
                return nodes[node]

            # Terminal node
            if not graph[node]:
                return True

            # Node belongs to a cycle
            if node in visited:
                return False

            visited.add(node)
            for next_node in graph[node]:
                if node not in nodes:
                    if not is_safe(next_node, visited.copy(), nodes):
                        nodes[node] = False
                        return False
            nodes[node] = True
            return True

        nodes: Dict[int, bool] = {}
        for node, links in enumerate(graph):
            if node not in nodes:
                safe = is_safe(node, set(), nodes)
                nodes[node] = safe

        return sorted(node for node, safe in nodes.items() if safe)


class TestSolution(unittest.TestCase):

    def test_basic_graph(self):

        graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
        safe_nodes = [2, 4, 5, 6]
        self.assertListEqual(Solution().eventualSafeNodes(graph), safe_nodes)

    def test_graph_with_just_safe_nodes(self):

        graph = [[], [0, 2, 3, 4], [3], [4], [0]]
        safe_nodes = [0, 1, 2, 3, 4]
        self.assertListEqual(Solution().eventualSafeNodes(graph), safe_nodes)
