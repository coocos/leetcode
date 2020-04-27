import unittest
import sys

from leetcode.common import TreeNode


class Solution:
    """
    This depth-first recursive solution validates the tree by keeping
    track of the bounds each node needs to remain within. For example
    when validating the right subtree of a node A, the bounds can be set
    to be between the value of the node itself and whatever the upper bound
    is for the current node as the node needs to between those in order
    for the tree to be valid. To handle the special root node case the bounds
    are set to (-sys.maxsize, sys.maxsize).
    """
    def validate(self,
                 node: TreeNode,
                 lower: int = -sys.maxsize,
                 upper: int = sys.maxsize) -> bool:

        if not node:
            return True
        elif lower < node.val < upper:
            left = self.validate(node.left, lower, node.val)
            right = self.validate(node.right, node.val, upper)
            return left and right
        else:
            return False

    def isValidBST(self, root: TreeNode) -> bool:

        return self.validate(root)


class TestSolution(unittest.TestCase):

    def test_true_example(self):

        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(Solution().isValidBST(root))

    def test_false_example(self):

        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(Solution().isValidBST(root))
