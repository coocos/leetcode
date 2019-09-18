import unittest

from common import TreeNode


class Solution:
    """
    This recursive depth-first solution traverses the tree and keeps track
    of whether the current node is a left or a right node. When a left leaf
    node is encountered its value is returned and the recursion is terminated.
    If the current node is not a leaf, the function will be called recursively
    for both left and right subtrees and the sum of their return values will be
    returned.
    """
    def sumOfLeftLeaves(self, root: TreeNode, left: bool = False) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            return root.val if left else 0

        return (self.sumOfLeftLeaves(root.left, True) +
                self.sumOfLeftLeaves(root.right, False))


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(Solution().sumOfLeftLeaves(root), 24)

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        self.assertEqual(Solution().sumOfLeftLeaves(root), 4)
