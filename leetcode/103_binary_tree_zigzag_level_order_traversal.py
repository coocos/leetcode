import unittest
import collections
from typing import List, Deque

from leetcode.common import TreeNode


class Solution:
    """
    This solution uses iterative breadth-first traversal to visit
    all nodes of the tree. As each level is visited the nodes are
    pushed to a double-ended queue and when all nodes of the current
    level have been visited they are pushed to a list of lists by
    iterating the double-ended queue in a zigzag order according to
    the current level depth.
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        queue: Deque[TreeNode] = collections.deque([root])
        level: Deque[TreeNode] = collections.deque([])
        levels: List[List[int]] = []

        while queue:

            node = queue.pop()
            level.append(node)

            if not queue and node:

                for node in level:
                    if node.left:
                        queue.appendleft(node.left)
                    if node.right:
                        queue.appendleft(node.right)

                direction = -1 if len(levels) % 2 else 1
                levels.append([node.val for node in level][::direction])
                level = collections.deque([])

        return levels


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        expected = [
            [3],
            [20, 9],
            [15, 7]
        ]
        self.assertListEqual(Solution().zigzagLevelOrder(root), expected)

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)

        expected = [
            [1],
            [3, 2],
            [4, 5]
        ]
        self.assertListEqual(Solution().zigzagLevelOrder(root), expected)

    def test_empty_tree(self):

        root = None
        self.assertListEqual(Solution().zigzagLevelOrder(root), [])
