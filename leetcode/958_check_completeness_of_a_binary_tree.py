import unittest
import collections

from .common import TreeNode


class Solution:
    """
    This solution performs a breadth-first traversal over the tree. A flag
    is maintained which is set if at any point in the traversal an empty
    node is encountered. If at any point after setting the flag a valid node is
    found then the tree is not complete.
    """

    def isCompleteTree(self, root: TreeNode) -> bool:

        nodes = collections.deque([root])
        empty_node_seen = False

        while nodes:
            node = nodes.popleft()
            if node:
                if empty_node_seen:
                    return False
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                empty_node_seen = True

        return True


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.left = TreeNode(6)

        self.assertTrue(Solution().isCompleteTree(root))

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(7)

        self.assertFalse(Solution().isCompleteTree(root))

    def test_third_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.left = TreeNode(7)
        root.left.left.left = TreeNode(8)

        self.assertFalse(Solution().isCompleteTree(root))

    def test_fourth_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(6)
        root.right = TreeNode(3)

        self.assertTrue(Solution().isCompleteTree(root))
