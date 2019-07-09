import unittest

from common import TreeNode


class UnbalancedTreeException(Exception):
    """Raised when tree is unbalanced"""


class Solution:
    """
    This solution uses recursive depth-first traversal to visit all the
    nodes in the tree. Once the bottom of the tree is reached the current
    depth is returned for that particular subtree. The depth is compared
    against the second subtree and if they differ by more than one then
    an exception is raised. If they do not differ then the larger depth
    value of the two is returned and the comparison moves back up one node
    in the tree and the process repeats until all the subtrees have been
    verified.
    """
    def verify_balance(self, node: TreeNode, depth: int = 0) -> int:

        if not node:
            return depth

        left = self.verify_balance(node.left, depth + 1)
        right = self.verify_balance(node.right, depth + 1)

        if abs(left - right) > 1:
            raise UnbalancedTreeException()

        return max(left, right)

    def isBalanced(self, root: TreeNode) -> bool:

        try:
            self.verify_balance(root)
            return True
        except UnbalancedTreeException:
            return False


class TestSolution(unittest.TestCase):

    def test_balanced_tree(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertTrue(Solution().isBalanced(root))

    def test_unbalanced_tree(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)

        self.assertFalse(Solution().isBalanced(root))

    def test_simple_unbalanced_tree(self):

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        self.assertFalse(Solution().isBalanced(root))
