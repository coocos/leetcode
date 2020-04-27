import unittest

from leetcode.common import TreeNode


class Solution:
    """
    This recursive solution simply traverses the BST, returning
    the value of node plus its subtrees while discarding branches
    of the tree which are not within range.
    """
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        if not root:
            return 0

        range_sum = root.val if L <= root.val <= R else 0

        if root.val < R:
            range_sum += self.rangeSumBST(root.right, L, R)
        if root.val > L:
            range_sum += self.rangeSumBST(root.left, L, R)

        return range_sum


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)
        self.assertEqual(Solution().rangeSumBST(root, 7, 15), 32)
