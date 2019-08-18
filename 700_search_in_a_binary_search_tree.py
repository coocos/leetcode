import unittest

from common import TreeNode


class Solution:
    """
    This recursive solution simply searches the binary search
    tree and returns the node with the searched value and thus
    the subtree.
    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root:
            return None

        if root.val == val:
            return root

        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        node = Solution().searchBST(root, 2)
        self.assertEqual(node.val, 2)
        self.assertEqual(node.left.val, 1)
        self.assertEqual(node.right.val, 3)
