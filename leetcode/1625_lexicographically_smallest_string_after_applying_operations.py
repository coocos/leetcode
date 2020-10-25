import unittest
import collections


class Solution:
    """
    This solution performs a brute force breadth-first search starting
    from the given string. A depth-first search would probably work just
    as well.
    
    The iterative search pops a string from a queue, generates the rotated
    and added versions of the string and appends them to the queue, unless
    these strings have already been previously visited. Whenever a string
    is visited, it is compared against the smallest string so far and if it
    is smaller, then the smallest string so far is updated to be the current
    string. Once the queue is exhausted, the smallest string found during the
    search is returned.
    """

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        smallest = s
        queue = collections.deque([s])
        seen = {s}

        while queue:

            string = queue.popleft()
            smallest = min(string, smallest)

            rotated = string[b:] + string[:b]
            if rotated not in seen:
                queue.append(rotated)
                seen.add(rotated)

            added = ""
            for i, c in enumerate(string):
                if i % 2 != 0:
                    added += str((int(c) + a) % 10)
                else:
                    added += c
            if added not in seen:
                queue.append(added)
                seen.add(added)

        return smallest


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertEqual(Solution().findLexSmallestString("5525", 9, 2), "2050")

