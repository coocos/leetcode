import unittest
import collections
from typing import List, Deque


class Node:

    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children


class Solution:
    """
    This solution does a basic iterative breadth-first traversal
    using queues and collects all the node values into a list of
    lists in level order.
    """
    def levelOrder(self, root: Node) -> List[List[int]]:

        if not root:
            return []

        nodes = collections.deque([root])
        levels: List[List[int]] = [[]]
        children: Deque[Node] = collections.deque([])

        while nodes:
            node = nodes.popleft()
            levels[-1].append(node.val)
            for child in node.children:
                children.append(child)

            if not nodes:
                nodes = children
                children = collections.deque([])
                if nodes:
                    levels.append([])

        return levels


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        third = [Node(5), Node(6)]
        second = [Node(3, third), Node(2), Node(4)]
        root = Node(1, second)

        self.assertListEqual(Solution().levelOrder(root), [
            [1],
            [3, 2, 4],
            [5, 6]
        ])

    def test_empty_tree(self):

        self.assertListEqual(Solution().levelOrder(None), [])
