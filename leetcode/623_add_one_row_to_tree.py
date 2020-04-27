import unittest
import collections

from leetcode.common import TreeNode


class Solution:
    """
    This solution performs an iterative breadth-first traversal of the tree
    while keeping track of the depth of each node. When the algorithm
    encounters a node above the new row, it modifies the children of the node
    to be new nodes with values of v. The previous children of the node are set
    as the children of the new inserted nodes.
    """
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:

        # Handle root replacement separately
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root

        queue = collections.deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if depth == d - 1:
                temp_left = node.left
                node.left = TreeNode(v)
                node.left.left = temp_left
                temp_right = node.right
                node.right = TreeNode(v)
                node.right.right = temp_right
            # Nodes deeper than the target depth are irrelevant
            if depth >= d:
                break
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return root


class TestSolution(unittest.TestCase):

    def test_basic_example(self):

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(1)
        root.right.left = TreeNode(5)

        root = Solution().addOneRow(root, 1, 2)
        self.assertEqual(root.left.val, 1)
        self.assertEqual(root.right.val, 1)
        self.assertEqual(root.left.left.val, 2)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.right.val, 6)
        self.assertEqual(root.right.right.left.val, 5)
        self.assertIsNone(root.right.left)

    def test_replacing_root(self):

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root = Solution().addOneRow(root, 1, 1)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 4)
