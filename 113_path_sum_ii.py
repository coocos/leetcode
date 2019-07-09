import unittest
from typing import List

from common import TreeNode


class Solution:
    """
    This solution uses recursive depth-first traversal to visit all nodes
    of the tree. As the traversal is executed the sum is decremented
    by the value of each visited node. If a leaf is reached and the sum
    is zero then the path to this particular leaf meets the path sum
    criteria. If so, the leaf terminates the recursion by returning
    the value of itself in a nested list. As the recursive function returns
    all nodes will add their own values to this nested list if the
    nested list is not empty, thus forming all the paths which meet
    the path sum criteria.
    """
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []

        if not root.left and not root.right:
            return [[root.val]] if sum - root.val == 0 else []

        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)

        return [[root.val] + path for path in left + right if path]


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(5)

        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)

        expected = [
            [5, 4, 11, 2],
            [5, 8, 4, 5]
        ]
        self.assertListEqual(Solution().pathSum(root, 22), expected)
