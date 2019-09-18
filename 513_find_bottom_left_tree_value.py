import unittest

from typing import List
from common import TreeNode


class Solution:
    """
    This recursive depth-first solution traverses the tree and adds
    the leftmost node on each level to a list. Once the tree has been
    traversed the value of the last element in the list is returned.
    """
    def leftmostNodes(self,
                      node: TreeNode,
                      nodes: List[TreeNode],
                      depth: int) -> None:

        if not node:
            return

        if len(nodes) <= depth:
            nodes.append(node)

        self.leftmostNodes(node.left, nodes, depth + 1)
        self.leftmostNodes(node.right, nodes, depth + 1)

    def findBottomLeftValue(self, root: TreeNode) -> int:

        nodes: List[TreeNode] = []
        self.leftmostNodes(root, nodes, 0)
        return nodes[-1].val


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)

        self.assertEqual(Solution().findBottomLeftValue(root), 1)

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left.left = TreeNode(7)

        self.assertEqual(Solution().findBottomLeftValue(root), 7)
