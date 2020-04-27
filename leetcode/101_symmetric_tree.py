import unittest
import collections
from typing import Generator

from leetcode.common import TreeNode


class Solution:
    """
    This solution lazily compares the trees by zipping two generators which
    yield nodes from both sub-trees in breadth-first order. Nodes from the
    sub-trees are yielded in a mirrored order, i.e. left child is yielded
    before the right child in the first sub-tree and vice versa in the second
    sub-tree. Each yielded node is compared against the node yielded from
    the other sub-tree and if they differ then the tree is not symmetric.
    """
    def visit(self, root: TreeNode, swap: bool = False) -> Generator[TreeNode, None, None]:

        queue = collections.deque([root])

        while queue:

            node = queue.popleft()
            yield node.val if node else None

            if node:
                if swap:
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    queue.append(node.right)
                    queue.append(node.left)

    def isSymmetric(self, root: TreeNode) -> bool:

        # Empty trees are considered symmetric
        if not root:
            return True

        for first, second in zip(self.visit(root.left), self.visit(root.right, True)):
            if first != second:
                return False

        return True


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.left = TreeNode(4)

        self.assertTrue(Solution().isSymmetric(root))

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        self.assertFalse(Solution().isSymmetric(root))

    def test_empty_tree(self):

        self.assertTrue(Solution().isSymmetric(None))
