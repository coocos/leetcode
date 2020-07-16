import unittest
from typing import List

from .common import TreeNode


class Solution:
    """
    This solution first traverses both binary search trees in order and
    returns their values in two ordered lists. Then the two ordered
    lists are merged value by value and this final combined list is returned.

    Note that it's possible to yield values from the trees via generators without
    constructing the two lists but it seems to be slightly slower - possibly because
    of the slight overhead created by the generators.
    """

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def tree_values(node: TreeNode, values: List[int] = None) -> List[int]:
            if values is None:
                values = []
            if not node:
                return values

            if node.left:
                tree_values(node.left, values)
            values.append(node.val)
            if node.right:
                tree_values(node.right, values)
            return values

        def merge_lists(first: List[int], second: List[int]) -> List[int]:
            merged = []
            i, j = 0, 0
            while i < len(first) and j < len(second):
                if first[i] <= second[j]:
                    merged.append(first[i])
                    i += 1
                else:
                    merged.append(second[j])
                    j += 1
            while i < len(first):
                merged.append(first[i])
                i += 1
            while j < len(second):
                merged.append(second[j])
                j += 1
            return merged

        return merge_lists(tree_values(root1), tree_values(root2))


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        first = TreeNode(2)
        first.left = TreeNode(1)
        first.right = TreeNode(4)

        second = TreeNode(1)
        second.left = TreeNode(0)
        second.right = TreeNode(3)
        second.right.right = TreeNode(4)
        second.right.right.right = TreeNode(5)

        self.assertListEqual(
            Solution().getAllElements(first, second), [0, 1, 1, 2, 3, 4, 4, 5]
        )

    def test_empty_example(self):

        first = TreeNode(2)
        first.left = TreeNode(1)
        first.right = TreeNode(4)

        self.assertListEqual(Solution().getAllElements(first, None), [1, 2, 4])
