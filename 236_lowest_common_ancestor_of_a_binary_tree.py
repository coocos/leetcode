import unittest
from typing import List, Set

from common import TreeNode


class Solution:
    """
    This not-so-optimal recursive solution first constructs the paths to
    both nodes and then unpacks the paths for both nodes until a common
    ancestor is met.
    """
    def find_path(self, node: TreeNode, target: TreeNode) -> List[TreeNode]:

        if not node:
            return []

        if node == target:
            return [node]

        left = self.find_path(node.left, target)
        right = self.find_path(node.right, target)

        if left:
            return [node] + left
        if right:
            return [node] + right


    def lowestCommonAncestor(self,
                             root: TreeNode,
                             p: TreeNode,
                             q: TreeNode) -> TreeNode:

        seen: Set[TreeNode] = set()

        combined_paths = self.find_path(root, p) + self.find_path(root, q)
        while combined_paths:
            node = combined_paths.pop()
            if node in seen:
                return node
            seen.add(node)


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.right), root)

    def test_second_example(self):

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.left.right), root.left)

    def test_third_example(self):

        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.left.right.right), root.left)

    def test_fourth_example(self):

        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.right), root)
