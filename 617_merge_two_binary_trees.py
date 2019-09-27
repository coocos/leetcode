import unittest
from typing import Optional

from common import TreeNode


class Solution:
    """
    This recursive depth-first solution simply traverses the tree and combines
    the nodes as it goes. The recursion can be terminated in three different
    cases:

    * when neither of the nodes exist
    * t1 does not exist (which means the rest of the merged branch is just t2)
    * t2 does not exist (which means the rest of the merged branch is just t1)

    It's possible to not terminate the recursion in the latter two cases but
    it will cost time as the entire branch will be traversed even though it
    will only contain nodes from one of the trees.
    """
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> Optional[TreeNode]:

        if not t1 and not t2:
            return None

        # t2 has no nodes in the branch so the rest of the branch is just t1
        if t1 and not t2:
            return t1
        # t1 has no nodes in the branch so the rest of the branch is just t1
        if t2 and not t1:
            return t2

        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        t1.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)

        return t1


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root1 = TreeNode(1)
        root1.left = TreeNode(3)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(5)

        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)
        root2.left.right = TreeNode(4)
        root2.right.right = TreeNode(7)

        merged_root = Solution().mergeTrees(root1, root2)
        self.assertEqual(merged_root.val, 3)
        self.assertEqual(merged_root.left.val, 4)
        self.assertEqual(merged_root.right.val, 5)
        self.assertEqual(merged_root.left.left.val, 5)
        self.assertEqual(merged_root.left.right.val, 4)
        self.assertEqual(merged_root.right.right.val, 7)
