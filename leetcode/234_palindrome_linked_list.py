import unittest

from leetcode.common import ListNode


class Solution:
    """
    This solution simply goes through the linked list and
    constructs a plain list from it. Then it compares the
    constructed list against a reversed list. If the match
    then the linked list is a palindrome.

    Alternatively you could push all the linked list values
    to a stack, then pop the values from the stack while
    iterating the linked list and comparing the popped values
    to the linked list values but this is slightly slower.
    """
    def isPalindrome(self, head: ListNode) -> bool:

        nodes = []

        current = head
        while current:
            nodes.append(current.val)
            current = current.next

        return nodes == list(reversed(nodes))


class TestSolution(unittest.TestCase):

    def test_false_example(self):

        head = ListNode(1)
        head.next = ListNode(2)
        self.assertFalse(Solution().isPalindrome(head))

    def test_true_example(self):

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)
        self.assertTrue(Solution().isPalindrome(head))
