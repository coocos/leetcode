import unittest
import collections
from typing import List, Deque, Tuple
from common import TreeNode


class Solution:
    """
    This iterative solution keeps a queue of unvisited nodes and their depth
    to implement the level order traversal.

    The algorithm starts by queueing the root and its level, i.e. 0, to a
    queue of unvisited nodes. Then a loop is started which removes the next
    node and its level from the queue. The value of the removed node is
    appended to a list containing all values at this level and the node's
    children are put to the queue along with their levels (which is the
    current node's level plus one). This loop is executed until the queue
    is empty, i.e. when every node in the tree has been visited.
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        unvisited: Deque[Tuple[TreeNode, int]] = collections.deque([(root, 0)])
        levels: List[List[int]] = []

        while unvisited:

            node, level = unvisited.popleft()

            try:
                levels[level].append(node.val)
            except IndexError:
                levels.append([node.val])

            if node.left:
                unvisited.append((node.left, level + 1))
            if node.right:
                unvisited.append((node.right, level + 1))

        return levels


class TestSolution(unittest.TestCase):

    def test_example(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected = [[3], [9, 20], [15, 7]]
        self.assertListEqual(Solution().levelOrder(root), expected)

    def test_empty_tree(self):
        self.assertListEqual(Solution().levelOrder(None), [])
