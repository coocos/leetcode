import unittest


class Solution:
    """
    This solution iterates over the string and maps the movements
    to a (x, y) tuple. All the visited positions are maintained in
    a set and once a movement results in a position already present
    in the set, False is returned.
    """

    def isPathCrossing(self, path: str) -> bool:

        position = (0, 0)
        visited = set([position])

        for direction in path:
            if direction == "N":
                position = (position[0], position[1] + 1)
            elif direction == "W":
                position = (position[0] + 1, position[1])
            elif direction == "E":
                position = (position[0] - 1, position[1])
            else:
                position = (position[0], position[1] - 1)

            if position in visited:
                return True

            visited.add(position)

        return False


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertFalse(Solution().isPathCrossing("NES"))
