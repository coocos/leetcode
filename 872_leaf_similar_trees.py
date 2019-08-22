import unittest
from typing import Generator

from common import TreeNode


class Solution:
    """
    This depth-first recursive solution uses a generator which yields
    leaves from the tree one by one. Generators for both trees are
    iterated upon simultaneously and once differing leaves are found
    then False is returned. Otherwise the trees are leaf-similar.
    """
    def leaves(self, node: TreeNode) -> Generator[int, None, None]:

        if not node.left and not node.right:
            yield node.val

        if node.left:
            yield from self.leaves(node.left)

        if node.right:
            yield from self.leaves(node.right)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        for first, second in zip(self.leaves(root1), self.leaves(root2)):
            if first != second:
                return False
        return True


class TestSolution(unittest.TestCase):

    def test_true_example(self):

        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(8)

        self.assertTrue(Solution().leafSimilar(root, root))

    def test_false_example(self):

        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(8)

        self.assertFalse(Solution().leafSimilar(root, root.right))
