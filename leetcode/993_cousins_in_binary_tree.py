import unittest
from typing import Tuple

from leetcode.common import TreeNode


class Solution:
    """
    This recursive depth-first solution traverses the tree and keeps track
    of the depth of the traversal and when it encounters the target node,
    it returns its depth along with its parent. Finally the parents and the
    depths of the two target nodes are compared against the cousin criteria.
    """
    def find(self,
             node: TreeNode,
             parent: TreeNode,
             value: int,
             depth: int = 0) -> Tuple[int, TreeNode]:

        if not node:
            return 0, node

        if node.val == value:
            return depth, parent

        left_depth, child = self.find(node.left, node, value, depth + 1)
        if left_depth > 0:
            return left_depth, child

        right_depth, child = self.find(node.right, node, value, depth + 1)
        if right_depth > 0:
            return right_depth, child

        return 0, node

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        depth_x, parent_x = self.find(root, None, x)
        depth_y, parent_y = self.find(root, None, y)
        return depth_x == depth_y and parent_x != parent_y


class TestSolution(unittest.TestCase):

    def test_true_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(3)
        root.right.right = TreeNode(5)
        self.assertTrue(Solution().isCousins(root, 5, 4))

    def test_false_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right = TreeNode(3)
        self.assertFalse(Solution().isCousins(root, 2, 3))

    def test_second_false_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(5)
        self.assertFalse(Solution().isCousins(root, 2, 4))
