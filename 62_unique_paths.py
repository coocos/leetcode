import unittest


class Solution:
    """
    This solution uses dynamic programmming to compute
    the amount of unique paths to each position on the
    grid. The gist is to understand that all positions
    in the top row are reachable by only one path since
    the robot can only move right and not up. Similarly
    all the positions in the first column are reachable
    only by one path since the robot can only move down
    and not left. If you sketch out the situation you
    quickly realize that each position is only reachable
    from the positions to its left and above it. Therefore
    each position is reachable by the amount of paths which
    reach the surrounding positions to its left and above.
    """
    def uniquePaths(self, m: int, n: int) -> int:

        paths = [[0 for x in range(m)] for y in range(n)]

        # Top row is reachable only by one path
        for i in range(m):
            paths[0][i] = 1
        # First column is reachable only by one path
        for j in range(n):
            paths[j][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                # Each position is reachable by the amount of paths
                # to its left and above it
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[n - 1][m - 1]


class TestSolution(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(Solution().uniquePaths(3, 2), 3)

    def test_second_example(self):
        self.assertEqual(Solution().uniquePaths(7, 3), 28)
