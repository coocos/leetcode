import unittest

from leetcode.common import TreeNode


class Solution:
    """
    This recursive depth-first solution keeps track of the ongoing sum
    as it traverses the tree. This is done by always shifting the sum to
    the left by 1 bit for each node and then doing a bitwise OR with the
    value of that particular node.

    Once a leaf node is found the sum for that root-to-leaf path is returned,
    whereas all non-leaf calls return the sum of the paths to the leaves found
    in their subtrees.
    """
    def sumRootToLeaf(self, root: TreeNode, sum_: int = 0) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            return sum_ << 1 | root.val

        return (self.sumRootToLeaf(root.left, sum_ << 1 | root.val) +
                self.sumRootToLeaf(root.right, sum_ << 1 | root.val))


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(1)

        self.assertEqual(Solution().sumRootToLeaf(root), 22)
