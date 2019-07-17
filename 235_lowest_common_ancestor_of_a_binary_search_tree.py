import unittest

from common import TreeNode


class Solution:
    """
    This recursive solution utilizes the basic property of a binary search
    tree to find the common ancestor. In a binary search tree the left
    subtree of each node contains only values smaller than that particular
    node and the right subtree contains values larger than that particular
    node. Therefore, starting at the root, you can search for the first node
    where the value is smaller than p but larger than q or vice versa. That
    node will be the lowest common ancestor.
    """
    def lowestCommonAncestor(self,
                             root: TreeNode,
                             p: TreeNode,
                             q: TreeNode) -> TreeNode:

        # Node is larger than both nodes so the common ancestor has to be
        # in the left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Node is smaller than both nodes so the common ancestor has to be
        # in the right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Nodes are in distinct subtrees so this is the first common ancestor
        return root


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.right), root)

    def test_second_example(self):

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right = TreeNode(8)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)

        self.assertEqual(Solution().lowestCommonAncestor(root, root.left, root.left.right), root.left)
