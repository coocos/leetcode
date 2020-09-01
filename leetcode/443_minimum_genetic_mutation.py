import collections
import unittest
from typing import List


class Solution:
    """
    This solution treats the mutations like a graph and uses a queue to perform
    a breadth-first search on the graph. The search starts from the original string,
    mutates it according to all the valid rules and expands the search to those
    mutations while keeping track of the distance (amount of mutations) from the
    original string. This same process is repeated until one of the mutations turns
    out to be the target string or all the possible mutations in the mutation graph
    are visited. Since this is a breadth-first search and not a depth-first search,
    the first mutation to match the target string is the minimum mutation.
    """

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        mutations = collections.deque([(start, "", 0)])
        while mutations:
            mutation, previous_mutation, generation = mutations.popleft()
            if mutation == end:
                return generation

            for i in range(len(mutation)):
                for m in "CGTA":
                    if m != mutation[i]:
                        new_mutation = mutation[:i] + m + mutation[i + 1 :]
                        if new_mutation in bank and new_mutation != previous_mutation:
                            mutations.append((new_mutation, mutation, generation + 1))
        return -1


class TestSolution(unittest.TestCase):
    def test_example(self):
        start = "AAAAACCC"
        end = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
        self.assertEqual(Solution().minMutation(start, end, bank), 3)

    def test_second_example(self):

        start = "AACCGGTT"
        end = "AACCGCTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        self.assertEqual(Solution().minMutation(start, end, bank), 2)
