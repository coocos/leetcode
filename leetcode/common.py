import collections
from typing import List, Deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)

    def levels(self) -> List[List[int]]:
        """
        Returns a list of lists containing the values of all nodes
        in the tree in level order
        """
        levels: List[List[int]] = [[]]
        current_level: Deque[TreeNode] = collections.deque([self])
        next_level: Deque[TreeNode] = collections.deque([])

        while current_level:
            node = current_level.popleft()
            levels[-1].append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if not current_level:
                if next_level:
                    current_level = next_level
                    next_level = collections.deque([])
                    levels.append([])

        return levels


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def construct(*args) -> "ListNode":
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
        return " -> ".join(values)
