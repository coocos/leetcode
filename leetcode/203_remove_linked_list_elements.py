import unittest

from leetcode.common import ListNode


class Solution:
    """
    This recursive solution simply always checks if the next node should
    be removed. If so, then the next node is removed from the linked list
    and the recursion continues with the current node. If the next node
    does not need to be removed then the recursion continues with the next
    node. To deal with the problem of the head being a node to be removed
    a dummy node is inserted as the head of the linked list.
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        def remove(node: ListNode) -> None:

            if not node:
                return

            if node.next and node.next.val == val:
                node.next = node.next.next
                remove(node)
            else:
                remove(node.next)

        dummy_head = ListNode(None)
        dummy_head.next = head
        remove(dummy_head)

        return dummy_head.next


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)
        head.next.next.next.next.next = ListNode(5)
        head.next.next.next.next.next.next = ListNode(6)

        head = Solution().removeElements(head, 6)
        expected = [5, 4, 3, 2, 1]

        while head:
            self.assertEqual(head.val, expected.pop())
            head = head.next

    def test_removing_first_node(self):

        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)

        head = Solution().removeElements(head, 1)
        expected = [3, 2]

        while head:
            self.assertEqual(head.val, expected.pop())
            head = head.next
