import unittest
import heapq
from typing import List, Optional, Tuple

from .common import ListNode


class Solution:
    """
    This solution is based on using a heap / priority queue. First the
    first node of each linked list as well as the index of the list are
    inserted into a priority queue. Then the algorithm starts by dequeuing
    the lowest value from the priority list. This becomes the head of
    the merged list. The node following this node is inserted back into
    the priority queue. Then the process is repeated: a node is popped from
    the priority queue, it is attached to the previously popped node and the
    node following it is inserted into the priority queue. This is done until
    the priority queue is empty. Then the first node ever popped from the priority
    queue is returned as it is the head of the merged list.
    """

    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:

        heap: List[Tuple[int, int]] = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i))

        if not heap:
            return None

        # Construct the head of the merged list
        value, index = heapq.heappop(heap)
        current = lists[index]
        head = current
        if lists[index].next:
            lists[index] = lists[index].next
            heapq.heappush(heap, (current.next.val, index))

        # Construct the rest of the merged list
        while heap:

            value, index = heapq.heappop(heap)

            if lists[index]:

                current.next = lists[index]
                current = current.next

                lists[index] = lists[index].next
                if lists[index]:
                    heapq.heappush(heap, (lists[index].val, index))

        return head


class TestSolution(unittest.TestCase):
    def test_merging_three_lists(self):

        lists = [
            ListNode.construct(1, 4, 5),
            ListNode.construct(1, 3, 4),
            ListNode.construct(2, 6),
        ]
        merged = Solution().mergeKLists(lists)
        self.assertEqual(str(merged), "1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6")

    def test_merging_single_element_list(self):

        lists = [ListNode(1)]
        merged = Solution().mergeKLists(lists)
        self.assertIs(merged, lists[0])

    def test_merging_empty_lists(self):

        self.assertIsNone(Solution().mergeKLists([]))
        self.assertIsNone(Solution().mergeKLists([None]))
