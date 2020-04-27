import unittest
from typing import List

from leetcode.common import TreeNode


class Solution:
    """
    This recursive solution traverses the BST until it hits
    the left-most leaf, i.e. the smallest value in the BST.
    Then it adds the value of the leaf node to a list and
    unwinds the recursion, adding nodes to the list until
    the list contains k items. Then the kth item is returned.
    """
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        def gather_k_nodes(node: TreeNode, values: List[int]):

            if len(values) > k:
                return

            if not node:
                return

            if not node.left and not node.right:
                values.append(node.val)
                return

            gather_k_nodes(node.left, values)
            values.append(node.val)
            gather_k_nodes(node.right, values)

        values: List[int] = []
        gather_k_nodes(root, values)
        return values[k - 1]


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(Solution().kthSmallest(root, 1), 1)

    def test_second_example(self):

        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        self.assertEqual(Solution().kthSmallest(root, 3), 3)
