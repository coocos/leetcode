import unittest
import collections
from typing import List, Set


class Solution:
    """
    This solution approaches the transformations like a graph by
    performing a breadth-first search using a queue. The search
    starts from the initial word and performs all possible allowed
    transformations to that word and expands the search to those
    transformed words while maintaining the amount of transformations
    performed so far. If the search reaches the end word then the amount
    of transformations performed to reach that point is returned.
    """

    def ladderLength(self, begin: str, end: str, words: List[str]) -> int:

        valid_words = set(words)
        seen = set()
        if end not in valid_words:
            return 0

        transformations: List[Set[str]] = [set() for _ in begin]
        for word in valid_words:
            for i, letter in enumerate(word):
                transformations[i].add(letter)

        ladder = collections.deque([(begin, 1)])
        while ladder:
            word, length = ladder.popleft()

            if word in seen:
                continue
            if word == end:
                return length

            seen.add(word)

            for i in range(len(word)):
                for letter in transformations[i]:
                    next_word = word[:i] + letter + word[i + 1 :]
                    if next_word != word and next_word in valid_words:
                        ladder.append((next_word, length + 1))
        return 0


class TestSolution(unittest.TestCase):
    def test_five_step_transformation(self):
        begin = "hit"
        end = "cog"
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(Solution().ladderLength(begin, end, words), 5)

    def test_example_with_no_possible_solution(self):
        begin = "hit"
        end = "cog"
        words = ["hot", "dot", "tog", "cog"]
        self.assertEqual(Solution().ladderLength(begin, end, words), 0)

