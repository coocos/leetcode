import unittest

from leetcode.common import ListNode


class Solution:
    """
    This solution first iterates over the linked list once
    to find out its length. Then it iterates over the list
    partially a second time but stops at the middle and returns
    the node it is stopped at.
    """
    def middleNode(self, head: ListNode) -> ListNode:

        # Find out length of the list
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        # Go to the middle of the list
        current = head
        for _ in range(length // 2):
            current = current.next

        return current


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        head = ListNode.construct(1, 2, 3, 4, 5)
        node = Solution().middleNode(head)
        self.assertEqual(node.val, 3)

    def test_second_example(self):

        head = ListNode.construct(1, 2, 3, 4, 5, 6)
        node = Solution().middleNode(head)
        self.assertEqual(node.val, 4)

    def test_third_example(self):

        head = ListNode.construct(1, 2, 3)
        node = Solution().middleNode(head)
        self.assertEqual(node.val, 2)
