import unittest

from typing import List, Optional


class Node:
    def __init__(self, val, children: Optional[List['Node']] = None) -> None:
        self.val = val
        self.children = [] if children is None else children


class Solution:
    """
    This recursive depth-first solution keeps track of the depth
    of the currently visited node and always returns the deepest
    subtree of its children.
    """
    def maxDepth(self, root: Node, depth: int = 0) -> int:

        if not root:
            return depth

        if not root.children:
            return depth + 1

        return max(self.maxDepth(child, depth + 1) for child in root.children)


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_empty_tree(self):

        self.assertEqual(Solution().maxDepth(None), 0)
