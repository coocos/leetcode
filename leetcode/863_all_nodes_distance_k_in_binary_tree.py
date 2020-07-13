import unittest
import collections
from typing import List, Dict, Set, Optional

from .common import TreeNode

Graph = Dict[int, List[int]]


class Solution:
    """
    This solution is based on a two step approach. First the tree is
    converted into a graph by doing a depth-first recursive traversal
    of the tree and constructing a dictionary where each dictionary
    key is the value of a node and each dictionary value is a list with
    the values of the neighbouring nodes.

    Once this graph is constructed then a breadth-first search is conducted
    using the graph. The breadth-first search starts from the target node
    and keeps track of the distance of the search. Each visited node is
    appended to a list if it's at the appropriate distance and once the search
    expands beyond the target distance then the list is returned.
    """

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def tree_to_graph(node: TreeNode, graph: Optional[Graph] = None) -> Graph:

            if graph is None:
                graph = collections.defaultdict(list)

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                tree_to_graph(node.left, graph)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                tree_to_graph(node.right, graph)

            return graph

        def nodes_at_distance(target: int, distance: int, graph: Graph) -> List[int]:

            visited: Set[int] = set()
            queue = collections.deque([(target, 0)])
            nodes = []
            while queue:
                node, node_distance = queue.popleft()
                if node_distance > distance:
                    break
                elif node_distance == distance:
                    nodes.append(node)
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append((neighbour, node_distance + 1))
            return nodes

        graph = tree_to_graph(root)
        return nodes_at_distance(target.val, K, graph)


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)

        self.assertCountEqual(Solution().distanceK(root, root.left, 2), [7, 4, 1])
