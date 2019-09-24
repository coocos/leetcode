import unittest

from common import TreeNode


class Solution:
    """
    This recursive depth-first solution compares the two passed
    nodes against each other. If they are equal then the function
    calls itself recursively with its children taking into account
    that the children may be flipped, i.e. the right child of the
    first node may equal the left child of the second node.
    """
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        if not root1 and not root2:
            return True
        if not root1:
            return False
        if not root2:
            return False
        if root1.val != root2.val:
            return False

        children_not_flipped = (self.flipEquiv(root1.left, root2.left) and
                                self.flipEquiv(root1.right, root2.right))
        children_flipped = (self.flipEquiv(root1.left, root2.right) and
                            self.flipEquiv(root1.right, root2.left))
        return children_flipped or children_not_flipped


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root1.right.left = TreeNode(6)
        root1.left.left = TreeNode(4)
        root1.left.right = TreeNode(5)
        root1.left.right.left = TreeNode(7)
        root1.left.right.right = TreeNode(8)

        root2 = TreeNode(1)
        root2.left = TreeNode(3)
        root2.right = TreeNode(2)
        root2.left.right = TreeNode(6)
        root2.right.left = TreeNode(4)
        root2.right.right = TreeNode(5)
        root2.right.right.left = TreeNode(8)
        root2.right.right.right = TreeNode(7)

        self.assertTrue(Solution().flipEquiv(root1, root2))

    def test_second_example(self):

        root1 = None
        root2 = TreeNode(1)

        self.assertFalse(Solution().flipEquiv(root1, root2))

    def test_third_example(self):

        root1 = TreeNode(0)
        root1.right = TreeNode(1)
        root2 = None

        self.assertFalse(Solution().flipEquiv(root1, root2))

    def test_fourth_example(self):

        root1 = TreeNode(0)
        root1.left = TreeNode(3)
        root1.right = TreeNode(1)
        root1.right.right = TreeNode(2)

        root2 = TreeNode(0)
        root2.left = TreeNode(3)
        root2.right = TreeNode(1)
        root2.left.left = TreeNode(2)

        self.assertFalse(Solution().flipEquiv(root1, root2))
