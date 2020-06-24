import unittest
import collections
from typing import List


class Solution:
    """
    A simple iterative solution which builds a dictionary of cities
    as keys and their destinations as values. Afterwards the dictionary
    is iterated over again and the city with no destinations is returned
    making this O(N).
    """

    def destCity(self, paths: List[List[str]]) -> str:

        cities = collections.defaultdict(list)

        for source, destination in paths:
            cities[source].append(destination)
            if destination not in cities:
                cities[destination] = []

        for city, destinations in cities.items():
            if not destinations:
                return city

        raise Exception("No destination city found")


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        self.assertEqual(Solution().destCity(paths), "Sao Paulo")

    def test_second_example(self):

        paths = [["B", "C"], ["D", "B"], ["C", "A"]]
        self.assertEqual(Solution().destCity(paths), "A")

    def test_third_example(self):

        paths = [["A", "Z"]]
        self.assertEqual(Solution().destCity(paths), "Z")
