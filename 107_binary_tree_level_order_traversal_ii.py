import unittest
from typing import List

from common import TreeNode


class Solution:
    """
    This depth-first recursive solution simply constructs the levels by
    keeping track of what level the recursion is on and adding the nodes
    to the list for that level. This list of lists is simply reversed before
    returning it.
    """
    def traverse(self,
                 node: TreeNode,
                 levels: List[List[int]],
                 level: int = 0) -> None:

        if not node:
            return

        try:
            levels[level].append(node.val)
        except IndexError:
            levels.append([])
            levels[level].append(node.val)

        self.traverse(node.left, levels, level + 1)
        self.traverse(node.right, levels, level + 1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        levels: List[List[int]] = []
        self.traverse(root, levels)
        levels.reverse()
        return levels


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertListEqual(Solution().levelOrderBottom(root), [
            [15, 7],
            [9, 20],
            [3]
        ])
