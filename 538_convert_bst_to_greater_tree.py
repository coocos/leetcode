import unittest
from typing import Generator

from common import TreeNode


class Solution:
    """
    This solution uses a recursive generator to yield nodes from the
    BST in descending value order. A counter is used to keep track of the
    sum of the nodes seen so far and as each node is yielded from the
    generator, its value is updated to match the counter.
    """
    def convertBST(self, root: TreeNode) -> TreeNode:

        def traverse(node: TreeNode) -> Generator[TreeNode, None, None]:

            if not node:
                return

            yield from traverse(node.right)
            yield node
            yield from traverse(node.left)

        greater = 0
        for node in traverse(root):
            greater += node.val
            node.val = greater
        return root


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(13)

        root = Solution().convertBST(root)

        self.assertEqual(root.val, 18)
        self.assertEqual(root.left.val, 20)
        self.assertEqual(root.right.val, 13)

    def test_second_example(self):

        root = TreeNode(2)
        root.left = TreeNode(0)
        root.right = TreeNode(3)
        root.left.left = TreeNode(-4)
        root.left.right = TreeNode(1)

        root = Solution().convertBST(root)

        self.assertEqual(root.val, 5)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.val, 6)
        self.assertEqual(root.left.right.val, 6)
        self.assertEqual(root.left.left.val, 2)

    def test_third_example(self):

        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(4)
        root.left.left = TreeNode(-2)
        root.right.left = TreeNode(3)

        root = Solution().convertBST(root)

        self.assertEqual(root.val, 8)
        self.assertEqual(root.left.val, 8)
        self.assertEqual(root.right.val, 4)
        self.assertEqual(root.left.left.val, 6)
        self.assertEqual(root.right.left.val, 7)

    def test_empty_tree(self):

        root = Solution().convertBST(None)
        self.assertIsNone(root, None)
