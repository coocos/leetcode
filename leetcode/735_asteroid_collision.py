from __future__ import annotations
import unittest
from typing import List, Optional


class Node:
    """Linked list node"""

    def __init__(self, value) -> None:
        self.value = value
        self.next: Optional[Node] = None
        self.previous: Optional[Node] = None

    @classmethod
    def from_list(cls, values: List) -> Node:
        """Constructs linked list from a list"""
        head = cls(values[0])
        current = head
        for value in values[1:]:
            current.next = cls(value)
            current.next.previous = current
            current = current.next
        return head

    def to_list(self) -> List:
        """Turns linked list into a list"""
        values = []
        current = self
        while current:
            values.append(current.value)
            current = current.previous
        return values


class Solution:
    """
    This rather convoluted solution constructs a doubly linked list from the asteroids.
    A pointer is moved over the linked list and when a collision is detected, the linked
    list is altered to delete either both asteroids or one of the asteroids according
    to the size of each asteroid. Then the pointer is adjusted accordingly. For example,
    if both asteroids are destroyed then the pointer is moved one asteroid backwards
    and the two asteroids are deleted from the linked list. This process repeats until
    the pointer reaches the end of the linked list.
    """

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        current = Node.from_list(asteroids)

        while current.next:

            if current.value > 0 and current.next.value < 0:
                # Next asteroid gets demolished
                if current.value > abs(current.next.value):
                    current.next = current.next.next
                    if current.next:
                        current.next.previous = current
                # Current asteroid gets demolished
                elif current.value < abs(current.next.value):
                    if current.previous:
                        current = current.previous
                        current.next = current.next.next
                        current.next.previous = current
                    else:
                        current = current.next
                        current.previous = None
                # Both asteroids get demolished
                else:
                    if current.previous:
                        current = current.previous
                        current.next = current.next.next.next
                        if current.next:
                            current.next.previous = current
                    else:
                        current = current.next.next
                        if current:
                            current.previous = None
            else:
                current = current.next

            if not current:
                break

        return list(reversed(current.to_list())) if current else []


class TestSolution(unittest.TestCase):
    def test_example_with_two_collisions(self):

        asteroids = [10, 2, -5]
        self.assertListEqual(Solution().asteroidCollision(asteroids), [10])

    def test_example_with_one_collision(self):

        asteroids = [5, 10, -5]
        self.assertListEqual(Solution().asteroidCollision(asteroids), [5, 10])

    def test_example_with_all_asteroids_colliding(self):

        asteroids = [8, -8]
        self.assertListEqual(Solution().asteroidCollision(asteroids), [])

    def test_example_with_no_asteroids_colliding(self):

        asteroids = [-2, -1, 1, 2]
        self.assertListEqual(Solution().asteroidCollision(asteroids), asteroids)

    def test_example_with_the_last_asteroid_destroying_others(self):

        asteroids = [2, 1, -8]
        self.assertListEqual(Solution().asteroidCollision(asteroids), [-8])
