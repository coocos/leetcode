
import unittest
from typing import List

from common import TreeNode


class Solution:
    """
    This recursive solution traverses the tree and constructs a list
    of nodes for each path until it reaches a leaf node. When a leaf
    node is encountered, the nodes in the path list are summed together
    and the sum is returned.
    """
    def sum_paths(self, node: TreeNode, path: List[int]) -> int:

        if not node:
            return 0

        if not node.left and not node.right:
            return sum(val * 10 ** i for i, val in enumerate(reversed(path + [node.val])))

        return (self.sum_paths(node.left, path + [node.val]) +
                self.sum_paths(node.right, path + [node.val]))

    def sumNumbers(self, root: TreeNode) -> int:

        return self.sum_paths(root, [])


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(Solution().sumNumbers(root), 25)

    def test_second_example(self):

        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)

        self.assertEqual(Solution().sumNumbers(root), 1026)
