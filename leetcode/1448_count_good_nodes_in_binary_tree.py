import unittest
import sys
from .common import TreeNode


class Solution:
    """
    This rather terse solution is based on doing a recursive depth-first search.
    The idea is to maintain the largest value seen so far during each path and
    pass it along as all the paths to the leaves are traversed. Each recursive call
    will return 1 or 0 based on whether the current node is larger or equal to
    the largest value seen so far and will add to that 1 or 0 the values returned
    by the recursive calls to the left and right subtrees.
    """

    def goodNodes(self, root: TreeNode, largest: int = -sys.maxsize) -> int:

        value = 1 if root.val >= largest else 0
        largest = max(largest, root.val)
        left = self.goodNodes(root.left, largest) if root.left else 0
        right = self.goodNodes(root.right, largest) if root.right else 0
        return value + left + right


class TestSolution(unittest.TestCase):
    def test_first_example(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.left.left = TreeNode(3)
        root.right = TreeNode(4)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)
        self.assertEqual(Solution().goodNodes(root), 4)

    def test_second_example(self):
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(Solution().goodNodes(root), 3)

    def test_single_node_example(self):
        root = TreeNode(1)
        self.assertEqual(Solution().goodNodes(root), 1)
