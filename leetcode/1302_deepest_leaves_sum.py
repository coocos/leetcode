import unittest
import collections
from typing import List
from .common import TreeNode


class Solution:
    """
    This iterative solution performs a breadth-first traversal of the
    tree. While traversing a sum is kept of the deepest leaves encountered
    so far. If a new, deeper leaf is found then the sum replaced with the value
    of the new, deepest leaf. Finally once the entire tree has been traversed the
    sum is returned.
    """

    def deepestLeavesSum(self, root: TreeNode) -> int:

        deepest = 0
        leaf_sum = 0
        nodes = collections.deque([(root, 0)])

        while nodes:
            node, depth = nodes.popleft()
            if not node.left and not node.right:
                if depth > deepest:
                    leaf_sum = node.val
                    deepest = depth
                elif depth == deepest:
                    leaf_sum += node.val
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

        return leaf_sum


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(7)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(6)
        root.right.right.right = TreeNode(8)

        self.assertEqual(Solution().deepestLeavesSum(root), 15)
