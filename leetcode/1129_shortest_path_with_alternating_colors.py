import unittest
import collections
from typing import List, Deque, Tuple, Dict


class Solution:
    """
    This solution is based on performing a breadth-first graph traversal.

    First a dictionary based graph is constructed based on the node count
    and the given edges. Next a breadth-first search is performed on the graph
    starting from the first node. As the neighbours of the node are explored a
    flag is maintained in the queue which indicates whether the current node was
    arrived to via a red edge or a blue edge. This flag dictates the color of the
    edges which are possible to use to proceed to the next neighbour. This process
    is repeated until all the nodes have been visited via various combinations of
    alternating color edges.
    """

    def shortestAlternatingPaths(
        self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]
    ) -> List[int]:

        # Construct graph
        graph: Dict[int, Dict[str, List]] = {
            node_id: {"red": [], "blue": []} for node_id in range(n)
        }
        for color, edges in (("red", red_edges), ("blue", blue_edges)):
            for from_, to in edges:
                graph[from_][color].append(to)

        shortest_distances = {node_id: {"red": -1, "blue": -1} for node_id in range(n)}
        nodes: Deque[Tuple[int, int, str]] = collections.deque(
            [(0, 0, "red"), (0, 0, "blue")]
        )

        while nodes:
            node, distance, color = nodes.popleft()
            if shortest_distances[node][color] == -1:
                shortest_distances[node][color] = distance
            elif distance <= shortest_distances[node][color]:
                shortest_distances[node][color] = distance
            else:
                continue

            next_color = "red" if color == "blue" else "blue"
            for next_node in graph[node][next_color]:
                nodes.append((next_node, distance + 1, next_color))

        final_distances = []
        for temp in shortest_distances.values():
            distance_via_either_color = [temp["red"], temp["blue"]]
            if -1 in distance_via_either_color:
                final_distances.append(max(distance_via_either_color))
            else:
                final_distances.append(min(distance_via_either_color))

        return final_distances


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        n = 3
        red_edges = [[0, 1], [1, 2]]
        blue_edges = []
        self.assertListEqual(
            Solution().shortestAlternatingPaths(n, red_edges, blue_edges), [0, 1, -1]
        )

    def test_failing_example(self):

        n = 5
        red_edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        blue_edges = [[1, 2], [2, 3], [3, 1]]
        self.assertListEqual(
            Solution().shortestAlternatingPaths(n, red_edges, blue_edges),
            [0, 1, 2, 3, 7],
        )

