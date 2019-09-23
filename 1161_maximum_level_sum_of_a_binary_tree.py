import unittest
import collections
from typing import Deque, List


from common import TreeNode


class Solution:
    """
    This solution does a level-order traversal of the tree,
    creates a list with sum of all the levels and returns the
    index of the level with the maximum sum.
    """
    def maxLevelSum(self, root: TreeNode) -> int:

        nodes: Deque[TreeNode] = collections.deque([root])
        next_level: Deque[TreeNode] = collections.deque()
        levels: List[int] = [0]

        while nodes:

            node = nodes.popleft()
            levels[-1] = levels[-1] + node.val

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if not nodes:
                nodes = next_level
                next_level = collections.deque()
                if nodes:
                    levels.append(0)

        return levels.index(max(levels)) + 1


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        self.assertEqual(Solution().maxLevelSum(root), 2)
