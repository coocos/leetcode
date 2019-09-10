import unittest
from typing import List

from common import TreeNode


class Solution:
    """
    Two solutions are provided for this problem. The first is a standard
    recursive solution and the second is a slightly more complicated
    iterative solution using a stack. The iterative solution
    works by first by pushing the root to the top of the stack. Then
    the stack is popped and the right and left child of the popped node
    are pushed to the stack in that order. This process repeats until
    the stack has been exhausted and thus all the nodes of the tree have
    been visited.
    """
    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        unvisited_nodes = [root]
        visited_nodes = []

        while unvisited_nodes:

            node = unvisited_nodes.pop()

            visited_nodes.append(node.val)
            if node.right:
                unvisited_nodes.append(node.right)
            if node.left:
                unvisited_nodes.append(node.left)

        return visited_nodes

    def preorderTraversalRecursive(self, node: TreeNode) -> List[int]:

        if not node:
            return []

        nodes = [node.val]
        if node.left:
            nodes = nodes + self.preorderTraversalRecursive(node.left)
        if node.right:
            nodes = nodes + self.preorderTraversalRecursive(node.right)
        return nodes


class TestSolution(unittest.TestCase):

    def test_recursive_solution(self):

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertListEqual(Solution().preorderTraversalRecursive(root), [1, 2, 3])

    def test_first_example_with_iterative_solution(self):

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertListEqual(Solution().preorderTraversalIterative(root), [1, 2, 3])

    def test_second_example_with_iterative_solution(self):

        root = TreeNode(1)
        root.left = TreeNode(4)
        root.right = TreeNode(3)
        root.left.left = TreeNode(2)
        self.assertListEqual(Solution().preorderTraversalIterative(root), [1, 4, 2, 3])
