import unittest


class Solution:
    """
    This solution treats the permutations like a graph and uses
    dynamic programming to build the count of possible permutations
    from the bottom up starting with single letter permutations.

    For a more thorough explanation to this problem see the solution
    to #935 - knight dialer as it is essentially the exact same problem.
    The only difference here is that the letters have been mapped to numbers
    and the graph itself is different.
    """

    def countVowelPermutation(self, n: int) -> int:

        graph = {
            0: (1,),
            1: (0, 2),
            2: (0, 1, 3, 4),
            3: (2, 4),
            4: (0,),
        }

        previous_permutations = [1] * 5
        for _ in range(n - 1):
            next_permutations = [0] * 5
            for node in range(5):
                for neighbour in graph[node]:
                    next_permutations[neighbour] += previous_permutations[node]
            previous_permutations = next_permutations

        return sum(previous_permutations) % (10 ** 9 + 7)


class TestSolution(unittest.TestCase):
    def test_five_letter_string(self):

        self.assertEqual(Solution().countVowelPermutation(5), 68)
