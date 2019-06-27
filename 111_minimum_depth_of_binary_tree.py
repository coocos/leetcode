import sys
import unittest

from common import TreeNode


class Solution:
    """
    This recursive depth-first algorithm visits the tree nodes until it
    hits a leaf node and then returns the depth of the visited leaf node.
    If the node is not a leaf node, the algorithm will return the smallest
    depth value of the node's children.
    """
    def depth(self, node: TreeNode, depth: int) -> int:

        # Reached leaf node so return current depth
        if node.left is None and node.right is None:
            return depth

        left_depth = sys.maxsize
        right_depth = sys.maxsize

        if node.left is not None:
            left_depth = self.depth(node.left, depth + 1)
        if node.right is not None:
            right_depth = self.depth(node.right, depth + 1)

        return min(left_depth, right_depth)

    def minDepth(self, root: TreeNode) -> int:

        return self.depth(root, 1) if root else 0


class TestSolution(unittest.TestCase):

    def test_example(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().minDepth(root), 2)
