import unittest
from typing import Set

from .common import TreeNode


class FindElements:
    """
    This recursive solution performs a depth-first traversal to recover the tree.
    As the tree is traversed and the values of the nodes are recovered they are
    also added to a set of values. find() uses the constructed set to look up the
    values making it a constant time operation.
    """

    def __init__(self, root: TreeNode):
        self.root = TreeNode
        self._values: Set[int] = set()
        self._recover(root, 0)

    def _recover(self, node: TreeNode, value: int) -> None:

        node.val = value
        self._values.add(value)

        if node.right:
            self._recover(node.right, node.val * 2 + 2)
        if node.left:
            self._recover(node.left, node.val * 2 + 1)

    def find(self, target: int) -> bool:
        return target in self._values


class TestSolution(unittest.TestCase):
    def test_first_example(self):
        root = TreeNode(-1)
        root.right = TreeNode(-1)

        elements = FindElements(root)
        self.assertFalse(elements.find(1))
        self.assertTrue(elements.find(2))

    def test_second_example(self):
        root = TreeNode(-1)
        root.right = TreeNode(-1)
        root.left = TreeNode(-1)
        root.left.left = TreeNode(-1)
        root.left.right = TreeNode(-1)

        elements = FindElements(root)
        self.assertTrue(elements.find(1))
        self.assertTrue(elements.find(3))
        self.assertFalse(elements.find(5))
