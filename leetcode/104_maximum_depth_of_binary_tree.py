import unittest

from leetcode.common import TreeNode


class Solution:
    """
    This solution traverses the tree recursively in a depth-first manner
    and keeps track of the depth of the current node. The recursion is
    terminated once a leaf node is reached and each recursive call returns
    the larger of the two sub-tree depths.
    """
    def depth(self, node: TreeNode, depth: int = 1) -> int:

        if not node or (not node.left and not node.right):
            return depth

        left = self.depth(node.left, depth + 1)
        right = self.depth(node.right, depth + 1)

        return max(left, right)

    def maxDepth(self, root: TreeNode) -> int:

        return self.depth(root) if root else 0


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().maxDepth(root), 3)

    def test_empty_tree(self):

        self.assertEqual(Solution().maxDepth(None), 0)
