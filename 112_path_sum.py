import unittest

from common import TreeNode


class Solution:
    """
    This solution utilizes a recursive depth-first traversal
    to visit all nodes in the tree. Each recursive call decrements
    the sum by the value of the current node and as the traversal
    reaches a leaf node, the remaining sum is compared against the
    value of the leaf node. If subtracting the value of the leaf node
    from the remaining sum is equal to zero then the path used to
    reach that leaf node adds up to the target sum.
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return sum - root.val == 0

        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)

        return left or right


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(5)

        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        self.assertTrue(Solution().hasPathSum(root, 22))

    def test_empty_tree(self):

        self.assertFalse(Solution().hasPathSum(None, 22))
