from __future__ import annotations
import unittest
import collections
from typing import Optional


Range = collections.namedtuple("Range", ["start", "end"])


class BinarySearchTreeNode:
    def __init__(self, start: int, end: int) -> None:
        self.range = Range(start, end)
        self.left: Optional[BinarySearchTreeNode] = None
        self.right: Optional[BinarySearchTreeNode] = None

    def insert(self, node: BinarySearchTreeNode) -> bool:

        if node.range.end <= self.range.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.insert(node)
        elif self.range.end <= node.range.start:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.insert(node)
        else:
            return False


class MyCalendar:
    """
    This solution uses a binary-search tree where each node represents
    an event and its time range. When an event is booked, the event is
    turned into a tree node and inserted into the tree starting from
    the root. The insertion process recurses to the left subtree if
    the event ends before (or immediately before) the current node starts
    or to the right subtree if the event starts after (or immediately after)
    the current node ends. If neither of those conditions are true then
    the event cannot be booked as it overlaps another event.
    """

    def __init__(self):
        self.root: Optional[BinarySearchTreeNode] = None

    def book(self, start: int, end: int) -> bool:

        if not self.root:
            self.root = BinarySearchTreeNode(start, end)
            return True

        return self.root.insert(BinarySearchTreeNode(start, end))


class TestSolution(unittest.TestCase):
    def test_simple_booking(self):
        calendar = MyCalendar()
        self.assertTrue(calendar.book(10, 20))
        self.assertFalse(calendar.book(15, 25))
        self.assertTrue(calendar.book(20, 30))

    def test_complex_booking(self):

        calendar = MyCalendar()
        events = [
            [47, 50, True],
            [33, 41, True],
            [39, 45, False],
            [33, 42, False],
            [25, 32, True],
            [26, 35, False],
            [19, 25, True],
            [3, 8, True],
            [8, 13, True],
            [18, 27, False],
        ]
        for start, end, expected in events:
            self.assertEqual(calendar.book(start, end), expected)
