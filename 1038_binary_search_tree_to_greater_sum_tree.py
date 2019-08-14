import unittest

from common import TreeNode


class Solution:
    """
    This tricky'ish recursive solution traverses the tree in a right to
    left depth-first order. When a leaf node is reached the function
    adds to the node value an accumulated value which for the right-most node
    in the tree is initially zero. As the algorithm traverses back up the
    the tree it returns the node value, continually accumulating to it
    the sum of values greater than than the node value itself.
    """
    def construct(self, node: TreeNode, accumulated: int = 0) -> int:

        if node.left is None and node.right is None:
            node.val += accumulated
            return node.val

        if node.right:
            node.val += self.construct(node.right, accumulated)
        else:
            node.val += accumulated

        if node.left:
            return self.construct(node.left, node.val)
        else:
            return node.val

    def bstToGst(self, root: TreeNode) -> TreeNode:

        self.construct(root)
        return root


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(4)
        root.left = TreeNode(1)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(3)
        root.right = TreeNode(6)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        root.right.right.right = TreeNode(8)

        updated_root = Solution().bstToGst(root)
        self.assertEqual(root.right.left.val, 26)
        self.assertEqual(updated_root.val, 30)
        self.assertEqual(updated_root.left.right.right.val, 33)
        self.assertEqual(updated_root.left.right.val, 35)
        self.assertEqual(updated_root.left.left.val, 36)

    def test_second_example(self):

        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)

        updated_root = Solution().bstToGst(root)
        self.assertEqual(updated_root.val, 7)
        self.assertEqual(updated_root.left.val, 9)
        self.assertEqual(updated_root.right.val, 4)
        self.assertEqual(updated_root.left.left.val, 10)
