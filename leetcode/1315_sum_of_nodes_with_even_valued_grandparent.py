import unittest
import collections

from .common import TreeNode
from typing import Deque, Tuple, Optional


class Solution:
    """
    This solution is based on doing an iterative breadth-first traversal
    of the tree. The queue that is used to visit each node in breadth-first
    order also contains each node's parent and grandparent. As the queue
    is unpacked the value of each node's grandparent is checked and if the
    value is even it's added to a running sum. Finally the sum is returned.
    """

    def sumEvenGrandparent(self, root: TreeNode) -> int:

        nodes: Deque[
            Tuple[TreeNode, Optional[TreeNode], Optional[TreeNode]]
        ] = collections.deque([(root, None, None)])
        node_sum = 0

        while nodes:
            node, parent, grandparent = nodes.popleft()
            if grandparent and grandparent.val % 2 == 0:
                node_sum += node.val
            if node.left:
                nodes.append((node.left, node, parent))
            if node.right:
                nodes.append((node.right, node, parent))

        return node_sum


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        root = TreeNode(6)

        root.left = TreeNode(7)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(7)
        root.left.left.left = TreeNode(9)
        root.left.right.left = TreeNode(1)
        root.left.right.right = TreeNode(4)

        root.right = TreeNode(8)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(5)

        self.assertEqual(Solution().sumEvenGrandparent(root), 18)
