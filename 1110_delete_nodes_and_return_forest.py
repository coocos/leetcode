import unittest
from typing import List, Set

from common import TreeNode


class Solution:
    """
    This recursive depth-first solution traverses the tree and uses a flag
    to keep track of whether a node is a new root or not. When each
    node is visited the algorithm checks whether the flag is true or
    not and if it is, then the node is added to the list of new roots.
    When the algorithm calls itself recursively for the children of the
    current node, it will compute the flag based on whether the
    current node needs to be deleted or not. Additionally the algorithm
    disconnects the links between deleted nodes and their parent nodes.
    """
    def delete_nodes(self,
                     node: TreeNode,
                     to_delete: Set[int],
                     forest: List[TreeNode],
                     new_root: bool = False) -> List[TreeNode]:

        if not node:
            return forest

        if new_root and node.val not in to_delete:
            forest.append(node)

        self.delete_nodes(node.left, to_delete, forest, node.val in to_delete)
        self.delete_nodes(node.right, to_delete, forest, node.val in to_delete)

        # Remove the links if the children are marked for deletion
        if node.left and node.left.val in to_delete:
            node.left = None
        if node.right and node.right.val in to_delete:
            node.right = None

        return forest

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        return self.delete_nodes(root, set(to_delete), [], True)


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)

        expected = [
            root,
            root.right.left,
            root.right.right
        ]
        self.assertListEqual(Solution().delNodes(root, [3, 5]), expected)

    def test_second_example(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(3)

        expected = [
            root,
            root.left.left
        ]
        self.assertListEqual(Solution().delNodes(root, [2, 3]), expected)
