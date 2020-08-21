import unittest
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    """
    This solution starts by constructing a sorted dictionary
    which keeps track of how many times each card appears in
    the hand, i.e. the count of each number. Then the dictionary
    is iterated over card by card while decrementing the count
    of the current card and adding the card to a group. If the group
    reaches the target set size then the process is restarted from
    the beginning with a new group. This is done until all cards
    in the dictionary have been consumed. If at any point any of
    the groups contain non-sequential cards or the size of a
    constructed group does not match the target set size then it's
    not possible to rearrange the cards into groups.

    Note that dictionaries are ordered by insertion only from
    Python 3.7 onwards. It's also possible to further optimize
    this problem by not actually constructing groups and instead
    just maintaining the current group size and the last card in
    the group.
    """

    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        cards: DefaultDict[int, int] = defaultdict(int)
        for card in sorted(hand):
            cards[card] += 1

        while cards:
            group: List[int] = []
            for card in list(cards.keys()):

                if cards[card] == 0:
                    del cards[card]
                    continue

                if group and group[-1] != card - 1:
                    return False

                group.append(card)
                cards[card] -= 1
                if len(group) == W:
                    break

            if group and len(group) != W:
                return False

        return True


class TestSolution(unittest.TestCase):
    def test_true_example(self):
        self.assertTrue(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))

    def test_false_example(self):
        self.assertFalse(Solution().isNStraightHand([1, 2, 3, 4, 5], 4))

    def test_trivial_example(self):
        self.assertFalse(Solution().isNStraightHand([5, 1], 2))

