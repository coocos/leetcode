import unittest

from leetcode.common import ListNode


class Solution:
    """
    This solution starts by looking at both of the lists and setting
    the head of the new linked list to be the smaller node of the
    the two lists and moving the pointer of the list forward. Then the
    process is repeated but the smaller nodes are always attached to the
    tail of the new linked list. Once one of the lists has been exhausted
    the algorithm links the remaining list to the tail of the new list,
    thus merging the two lists completely.
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # If one the lists is empty then just return the other list
        if not l1 or not l2:
            return l1 if l1 else l2

        head = None
        tail = None

        # Set the head to be the smallest node
        if l1.val < l2.val:
            head = l1
            tail = l1
            l1 = l1.next
        else:
            head = l2
            tail = l2
            l2 = l2.next

        # Consume nodes from both lists and link the smaller node
        # to the tail of the new linked list
        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
            else:
                tail.next = l2
                tail = tail.next
                l2 = l2.next

        # Link the left over list to the tail
        tail.next = l1 if l1 else l2

        return head


class TestSolution(unittest.TestCase):

    def test_basic_example(self):
        l1 = ListNode.construct(1, 2, 4)
        l2 = ListNode.construct(1, 3, 4)
        expected = '1 -> 1 -> 2 -> 3 -> 4 -> 4'
        self.assertEqual(str(Solution().mergeTwoLists(l1, l2)), expected)

    def test_empty_list(self):
        self.assertIsNone(Solution().mergeTwoLists(None, None))
