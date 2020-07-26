import unittest
from .common import ListNode


class Solution:
    """
    This solution iterates over the linked list and uses
    bitwise operations to compose the binary number.
    """

    def getDecimalValue(self, head: ListNode) -> int:

        value = head.val

        while head.next:

            value = value << 1 | head.next.val
            head = head.next

        return value


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        head = ListNode(1)
        head.next = ListNode(0)
        head.next.next = ListNode(1)
        self.assertEqual(Solution().getDecimalValue(head), 5)

