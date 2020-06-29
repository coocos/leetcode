import unittest
from typing import Optional

from .common import TreeNode


class Solution:
    """
    This solution performs a recursive depth-first search to prune the tree of
    leaf nodes with the given value. Note that the scenario where the root turns
    into a target leaf after the pruning operation is handled explicitly. 
    """

    def removeLeafNodes(self, root: TreeNode, target: int) -> Optional[TreeNode]:
        def is_target_leaf(node: TreeNode) -> bool:
            return not node.right and not node.left and node.val == target

        def remove_target_leaves(node: TreeNode) -> bool:

            if is_target_leaf(node):
                return True
            if node.left and remove_target_leaves(node.left):
                node.left = None
            if node.right and remove_target_leaves(node.right):
                node.right = None

            return is_target_leaf(node)

        return None if remove_target_leaves(root) else root


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)

        root = Solution().removeLeafNodes(root, 2)
        self.assertListEqual(root.levels(), [[1], [3], [4]])

    def test_removing_all_nodes(self):

        root = TreeNode(1)
        root.left = TreeNode(1)
        root.left.left = TreeNode(1)

        root = Solution().removeLeafNodes(root, 1)
        self.assertIsNone(root)
