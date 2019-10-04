import unittest
import string

from common import TreeNode


class Solution:
    """
    This recursive depth-first solution constructs all the strings from
    leaves to the root by constructing a string for each path as it
    traverses the tree. Once a leaf is reached then the constructed
    string is returned. Each recursive call returns the smaller
    of the two strings returned from the two subtrees.
    """
    def smallestFromLeaf(self, root: TreeNode, string_so_far: str = '') -> str:

        if not root:
            return ''

        if not root.left and not root.right:
            return string.ascii_lowercase[root.val] + string_so_far

        string_now = string.ascii_lowercase[root.val] + string_so_far
        left = self.smallestFromLeaf(root.left, string_now)
        right = self.smallestFromLeaf(root.right, string_now)

        return min(left, right) if (left and right) else left or right


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(4)
        self.assertEqual(Solution().smallestFromLeaf(root), 'dba')

    def test_second_example(self):

        root = TreeNode(25)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(2)
        self.assertEqual(Solution().smallestFromLeaf(root), 'adz')
