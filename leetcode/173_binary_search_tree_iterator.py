import unittest

from typing import List
from leetcode.common import TreeNode


class BSTIterator:
    """
    This solution uses a stack to implement the iterator.

    Upon iterator construction the root and all of its leftmost children
    are pushed to a stack. Once next() is called the stack is popped and the
    before the popped node is returned, all the leftmost children of its right
    child and the child itself are again pushed to the stack. Iterating the
    tree in such a manner will yield all of the node values in ascending order.
    hasNext() is implemented by simply returning the stack itself (or actually
    its boolean value to keep mypy happy).

    Note that the stack will contain at most H nodes, where H is the height of
    the tree and the complexity of next() will amortize to O(1) as it will call
    append() and pop() N times in total over N calls.
    """
    def __init__(self, root: TreeNode) -> None:

        self._stack: List[TreeNode] = []
        node = root
        while node:
            self._stack.append(node)
            node = node.left

    def next(self) -> int:

        node = self._stack.pop()

        child = node.right
        while child:
            self._stack.append(child)
            child = child.left

        return node.val

    def hasNext(self) -> bool:
        return bool(self._stack)


class TestIterator(unittest.TestCase):

    def test_first_example(self):

        root = TreeNode(7)
        root.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)

        iterator = BSTIterator(root)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 4)
        self.assertEqual(iterator.next(), 7)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 9)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 15)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 20)
        self.assertFalse(iterator.hasNext())
