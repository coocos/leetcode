import unittest
import collections
from typing import List


class Solution:
    """
    This solution first constructs a dictionary which maps
    the replacement keys to values for constant time look ups.
    Then the string is iterated over and whenever a bracket pair
    is captured, the captured value is looked up from the dictionary
    and replaced with the dictionary value.
    """

    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        aliases = collections.defaultdict(lambda: "?")
        for key, value in knowledge:
            aliases[key] = value

        final_string = []
        bracket_value = []
        within_brackets = False

        for letter in s:
            if letter == "(":
                within_brackets = True
                bracket_value = []
            elif letter == ")":
                replacement = aliases["".join(bracket_value)]
                final_string += list(replacement)
                within_brackets = False
            else:
                if within_brackets:
                    bracket_value.append(letter)
                else:
                    final_string.append(letter)

        return "".join(final_string)


class TestSolution(unittest.TestCase):
    def test_example_with_all_keys_defined(self):
        s = "(name)is(age)yearsold"
        knowledge = [["name", "bob"], ["age", "two"]]

        self.assertEqual(Solution().evaluate(s, knowledge), "bobistwoyearsold")

    def test_example_with_missing_key(self):
        s = "hi(name)"
        knowledge = [["a", "b"]]
        self.assertEqual(Solution().evaluate(s, knowledge), "hi?")

