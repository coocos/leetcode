import unittest
from typing import List

from common import TreeNode


class Solution:
    """
    This depth-first recursive solution maintains a list with a single value
    for each level of the tree. By traversing the tree in a pre-order
    manner and storing the value of the current node to the list at the
    index indicated by its level the list will eventually contain the
    rightmost node for each level.
    """
    def traverse(self,
                 node: TreeNode,
                 levels: List[int],
                 level: int = 0) -> None:

        if not node:
            return

        try:
            levels[level] = node.val
        except IndexError:
            levels.append(node.val)

        self.traverse(node.left, levels, level + 1)
        self.traverse(node.right, levels, level + 1)

    def rightSideView(self, root: TreeNode) -> List[int]:

        levels: List[int] = []
        self.traverse(root, levels)
        return levels


class TestSolution(unittest.TestCase):

    def test_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)

        self.assertListEqual(Solution().rightSideView(root), [1, 3, 4])

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)

        self.assertListEqual(Solution().rightSideView(root), [1, 2])
