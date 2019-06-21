import unittest
from typing import List


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def construct(*args) -> 'ListNode':
        """Constructs a linked list from passed values"""
        head = ListNode(args[0])
        current = head
        for arg in args[1:]:
            node = ListNode(arg)
            current.next = node
            current = node

        return head

    def __str__(self) -> str:
        """A pretty printable representation of the linked list"""
        values = []
        head = self
        while head:
            values.append(str(head.val))
            head = head.next
        return ' -> '.join(values)


class Solution:
    """
    This solution works in two parts.

    First both of the linked lists are reversed and summed. This is done by
    first pushing nodes / digits of each linked list to a stack. Then the
    stack is emptied by popping until it is empty and each popped value is
    multiplied by 10 to the power of the remaining stack size to essentially
    "add" zeros to the digits by making it a multiple of 10. All of the
    multiplied digits are then summed together to form the final sum.

    Once we have the sums for both linked lists, they can be summed together.
    Then the previous process is done in reverse by extracting the digits
    of the sum by repeatedly dividing the sum by 10 and storing the remainder
    digits as new nodes in a linked list. Finally the head of the linked
    list is returned.
    """
    def combine_digits(self, node: ListNode) -> int:

        stack: List[int] = []
        head = node

        # Reverse the list by iterating it and pushing the values on to a stack
        while head:
            stack.append(head.val)
            head = head.next

        # Combine the digits
        total = 0
        while stack:
            total += stack.pop() * 10 ** len(stack)

        return total

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        number_1 = self.combine_digits(l1)
        number_2 = self.combine_digits(l2)
        summed = number_1 + number_2

        # Handle the sum being zero separately
        if not summed:
            return ListNode(summed)

        head = None
        current = None

        # Keep dividing sum by 10 and creating new linked list nodes
        # of the remainder until the sum is zero
        while summed:
            node = ListNode(summed % 10)
            if current is None:
                current = node
                head = current
            else:
                current.next = node
                current = current.next
            summed = summed // 10

        return head


class TestSolution(unittest.TestCase):

    def test_basic_example(self):
        l1 = ListNode.construct(2, 4, 3)
        l2 = ListNode.construct(5, 6, 4)
        self.assertEqual(str(Solution().addTwoNumbers(l1, l2)), '7 -> 0 -> 8')

    def test_with_both_lists_containing_only_zero(self):
        l1 = ListNode.construct(0)
        l2 = ListNode.construct(0)
        self.assertEqual(str(Solution().addTwoNumbers(l1, l2)), '0')

    def test_with_second_list_containing_one(self):
        l1 = ListNode.construct(1)
        l2 = ListNode.construct(0)
        self.assertEqual(str(Solution().addTwoNumbers(l1, l2)), '1')
