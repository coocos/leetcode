import unittest
import collections
from typing import List, DefaultDict

from leetcode.common import TreeNode


class Solution:
    """
    This recursive solution traverses the tree, computing all the
    tree sums and adding them into a dictionary where each key is a
    tree sum and the value how many times the sum appears in the
    tree. Then the dictionary is iterated over and the most common
    sums are returned as a list.
    """
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        def find_sums(node: TreeNode, sums) -> int:
            """Returns all the tree sums as a list"""

            if not node:
                return 0

            tree_sum = (node.val +
                        find_sums(node.left, sums) +
                        find_sums(node.right, sums))
            sums[tree_sum] += 1
            return tree_sum

        sums: DefaultDict[int, int] = collections.defaultdict(int)
        find_sums(root, sums)
        if sums:
            most_frequent_sum_count = max(sums.values())
            return [tree_sum for tree_sum, sum_count in sums.items() if sum_count == most_frequent_sum_count]

        return []


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(-3)

        self.assertListEqual(Solution().findFrequentTreeSum(root), [2, -3, 4])

    def test_second_example(self):

        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(-5)

        self.assertListEqual(Solution().findFrequentTreeSum(root), [2])
