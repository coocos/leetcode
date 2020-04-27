import unittest
from typing import List


class Node:

    def __init__(self, val, children=None):
        self.val = val
        if children is not None:
            self.children = children
        else:
            self.children = []


class Solution:
    """
    This depth-first recursive solution simply constructs a
    list of node values by adding the children of each node
    to a list and then appending themselves to the end of the
    list.
    """
    def postorder(self, root: Node) -> List[int]:

        if not root:
            return []

        nodes: List[int] = []

        for child in root.children:
            nodes += self.postorder(child)

        return nodes + [root.val]


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = Node(1)
        root.children = [Node(3), Node(2), Node(4)]
        root.children[0].children = [Node(5), Node(6)]
        self.assertListEqual(Solution().postorder(root), [5, 6, 3, 2, 4, 1])
