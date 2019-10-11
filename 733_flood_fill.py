import unittest
from typing import List


class Solution:
    """
    This solution uses a recursive depth-first approach to implement
    the flood fill. The recursion begins by setting the pixel at the
    initially given coordinates to the new color. Then the same function
    is called recursively for each of the neighboring pixels. The recursion
    is terminated when a pixel does not match the target color.

    Note that in order to avoid a stack overflow the algorithm first
    needs to check that the new color is not the same as the old
    color. Otherwise the depth-first traversal will end up visiting
    the same pixels over and over again.
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def fill(x: int, y: int, width: int, height: int, color: int) -> None:

            if image[y][x] != color:
                return

            image[y][x] = newColor

            if x > 0:
                fill(x - 1, y, width, height, color)
            if y > 0:
                fill(x, y - 1, width, height, color)
            if x < width:
                fill(x + 1, y, width, height, color)
            if y < height:
                fill(x, y + 1, width, height, color)

        width = len(image[0]) - 1
        height = len(image) - 1
        old_color = image[sr][sc]
        if old_color != newColor:
            fill(sc, sr, width, height, old_color)

        return image


class TestSolution(unittest.TestCase):

    def test_basic_flood_filL(self):
        image = [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
        filled = [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]
        ]
        self.assertListEqual(Solution().floodFill(image, 1, 1, 2), filled)

    def test_flood_filling_same_color(self):
        image = [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
        self.assertListEqual(Solution().floodFill(image, 1, 1, 1), image)
