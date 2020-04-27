import unittest
import collections

from typing import List, Deque
from leetcode.common import TreeNode


class Solution:
    """
    This iterative algorithm performs a breadth-first traversal,
    gathers all the nodes from all levels of the tree into a
    list of lists and then averages the levels.
    """
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        queue: Deque[TreeNode] = collections.deque([root])
        children: Deque[TreeNode] = collections.deque([])
        levels: List[List[float]] = [[]]

        while queue:

            node = queue.popleft()
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            levels[-1].append(node.val)

            if not queue:
                queue = children
                children = collections.deque([])

                if queue:
                    levels.append([])

        return [sum(level) / len(level) for level in levels]


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual(Solution().averageOfLevels(root), [3, 14.5, 11])
