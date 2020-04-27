import unittest


from leetcode.common import TreeNode


class Solution:
    """
    This recursive depth-first solution traverses the
    tree and upon reaching a leaf returns whether the
    leaf should be pruned or not. If it should be pruned
    it is pruned by the parent node and the parent node
    returns whether it itself should be pruned by checking
    if either of its subtrees need to be preserved or
    it itself should be preserved.
    """
    def prune(self, node: TreeNode) -> bool:

        if node.left is None and node.right is None:
            return node.val == 1

        preserve_right = False
        if node.right:
            preserve_right = self.prune(node.right)
            if not preserve_right:
                node.right = None

        preserve_left = False
        if node.left:
            preserve_left = self.prune(node.left)
            if not preserve_left:
                node.left = None

        return preserve_left or preserve_right or bool(node.val)

    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.prune(root)
        return root


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(1)
        root.right = TreeNode(0)
        root.right.right = TreeNode(1)
        root.right.left = TreeNode(0)

        Solution().pruneTree(root)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.right.val, 0)
        self.assertEqual(root.right.right.val, 1)
        self.assertIsNone(root.right.left)

    def test_second_example(self):

        root = TreeNode(1)
        root.right = TreeNode(0)
        root.right.right = TreeNode(1)
        root.right.left = TreeNode(0)

        root.left = TreeNode(1)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(1)
        root.left.left.left = TreeNode(0)

        Solution().pruneTree(root)
        self.assertIsNone(root.left.left.left)
        self.assertIsNone(root.right.left)
