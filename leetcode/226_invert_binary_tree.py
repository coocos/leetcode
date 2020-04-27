import unittest

from leetcode.common import TreeNode


class Solution:
    """
    This solution simply recursively traverses the tree and swaps
    left and right subtrees for each node.
    """
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(7)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        inverted = Solution().invertTree(root)
        self.assertEqual(inverted.val, 4)
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.val, 2)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertEqual(inverted.right.right.val, 1)
