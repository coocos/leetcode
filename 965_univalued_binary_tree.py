import unittest

from common import TreeNode


class Solution:
    """
    This solution recursively traverses the tree and returns
    False when it encounters a node with a value which differs
    from the root value. If the node does not differ in value then
    the algorithm returns the validity of both its subtrees thus
    confirming whether the tree is univalued or not.
    """
    def validate(self, node: TreeNode, value: int) -> bool:

        if node.val != value:
            return False

        left_valid = True
        if node.left:
            left_valid = self.validate(node.left, value)
        right_valid = True
        if node.right:
            right_valid = self.validate(node.right, value)

        return left_valid and right_valid

    def isUnivalTree(self, root: TreeNode) -> bool:

        return self.validate(root, root.val)


class TestSolution(unittest.TestCase):

    def test_univalued_tree(self):

        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.right.right = TreeNode(1)
        self.assertTrue(Solution().isUnivalTree(root))

    def test_regular_tree(self):

        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(2)
        self.assertFalse(Solution().isUnivalTree(root))
