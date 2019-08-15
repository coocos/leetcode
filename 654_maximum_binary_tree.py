import unittest
from typing import List, Optional

from common import TreeNode


class Solution:
    """
    This recursive solution finds the largest value from the list,
    constructs a node from it and then recursively calls itself with
    sliced values from the left and right partition to construct the left
    subtree and right subtree.
    """
    def constructMaximumBinaryTree(self,
                                   nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        maximum = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[maximum]:
                maximum = i

        node = TreeNode(nums[maximum])
        node.left = self.constructMaximumBinaryTree(nums[:maximum])
        node.right = self.constructMaximumBinaryTree(nums[maximum + 1:])

        return node


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
        self.assertEqual(root.val, 6)
        self.assertEqual(root.left.val, 3)
        self.assertEqual(root.left.right.val, 2)
        self.assertEqual(root.left.right.right.val, 1)
        self.assertEqual(root.right.val, 5)
        self.assertEqual(root.right.left.val, 0)
