import unittest
import collections
from typing import Generator

from common import TreeNode


class Solution:
    """
    This solution lazily compares the trees by zipping two generators which
    yield nodes from both trees in breadth-first order. Each yielded node is
    compared against the node yielded from the other tree and if they differ
    at any point then the trees are not the same.
    """
    def visit(self, root: TreeNode) -> Generator[TreeNode, None, None]:

        queue = collections.deque([root])

        while queue:

            node = queue.popleft()
            yield node.val if node else None

            if node is not None:
                queue.append(node.left)
                queue.append(node.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        for first, second in zip(self.visit(p), self.visit(q)):
            if first != second:
                return False

        return True


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root_p = TreeNode(1)
        root_p.right = TreeNode(3)
        root_p.left = TreeNode(2)

        root_q = TreeNode(1)
        root_q.right = TreeNode(3)
        root_q.left = TreeNode(2)

        self.assertTrue(Solution().isSameTree(root_p, root_q))

    def test_second_example(self):

        root_p = TreeNode(1)
        root_p.left = TreeNode(2)

        root_q = TreeNode(1)
        root_q.right = TreeNode(2)

        self.assertFalse(Solution().isSameTree(root_p, root_q))

    def test_third_example(self):

        root_p = TreeNode(1)
        root_p.right = TreeNode(1)
        root_p.left = TreeNode(2)

        root_q = TreeNode(1)
        root_q.right = TreeNode(2)
        root_q.left = TreeNode(1)

        self.assertFalse(Solution().isSameTree(root_p, root_q))
