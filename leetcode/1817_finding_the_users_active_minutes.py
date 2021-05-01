from typing import List
import collections
import unittest


class Solution:
    """
    This solution first iterates over the logs and creates a dictionary, where
    each key is a user and the value is a set containing the minutes the user
    performed actions at. Next, the dictionary is iterated over and the size
    of each set is used as an index to increment a number starting from zero
    in a list of size k. This way the list ends up containing the number of
    users who spent n active minutes.
    """

    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        users = collections.defaultdict(set)
        for user, minute in logs:
            users[user].add(minute)

        active_minutes = [0] * k
        for user_minutes in users.values():
            active_minutes[len(user_minutes) - 1] += 1

        return active_minutes


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
        k = 5
        expected = [0, 2, 0, 0, 0]
        self.assertListEqual(Solution().findingUsersActiveMinutes(logs, k), expected)

    def test_second_example(self):

        logs = [[1, 1], [2, 2], [2, 3]]
        k = 4
        expected = [1, 1, 0, 0]
        self.assertListEqual(Solution().findingUsersActiveMinutes(logs, k), expected)
