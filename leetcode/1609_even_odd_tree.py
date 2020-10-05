import unittest
import collections
from typing import Dict

from .common import TreeNode


class Solution:
    """
    This solution performs a breadth-first traversal over
    the tree using a queue. Since also the depth of each
    node is stored in the queue, checking the even-odd
    property of each node is trivial. Checking whether the
    nodes in each level are in increasing or decreasing order
    is a bit trickier and is done by storing the latest visited
    node in each level in a dictionary and by comparing the
    current node against the latest visited node from the same
    level via the dictionary.
    """

    def isEvenOddTree(self, root: TreeNode) -> bool:

        queue = collections.deque([(root, 0)])
        last_value_in_level: Dict[int, TreeNode] = {}
        while queue:
            node, depth = queue.popleft()
            if depth % 2 == 0:
                if node.val % 2 == 0:
                    return False
                if (
                    depth in last_value_in_level
                    and last_value_in_level[depth].val >= node.val
                ):
                    return False
            else:
                if node.val % 2 != 0:
                    return False
                if (
                    depth in last_value_in_level
                    and last_value_in_level[depth].val <= node.val
                ):
                    return False
            last_value_in_level[depth] = node

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return True


class TestSolution(unittest.TestCase):
    def test_even_odd_tree(self):

        root = TreeNode(1)
        root.left = TreeNode(10)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(12)
        root.left.left.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.left.left = TreeNode(6)
        root.right.right = TreeNode(9)
        root.right.right.right = TreeNode(2)
        self.assertTrue(Solution().isEvenOddTree(root))

    def test_tree_with_non_increasing_even_level(self):

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(7)
        self.assertFalse(Solution().isEvenOddTree(root))
