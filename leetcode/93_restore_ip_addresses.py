import unittest
from typing import List


class Solution:
    """
    This slightly convoluted depth-first recursive solution keeps slicing off 1, 2 and
    3 digits from the front of the string until the string has been exhausted and the
    sliced digits form a valid IP address.
    """

    def restoreIpAddresses(self, s: str, numbers: List[str] = None) -> List[str]:

        if numbers is None:
            numbers = []

        if numbers:
            # Numbers over 255 indicate an invalid address
            if int(numbers[-1]) > 255:
                return []
            # Numbers with leading zeroes indicate an invalid address
            elif numbers[-1].startswith("0") and len(numbers[-1]) > 1:
                return []

        if len(numbers) == 4:
            return [] if s else [".".join(numbers)]
        elif not s:
            return []

        addresses = []
        for address in self.restoreIpAddresses(s[1:], numbers + [s[:1]]):
            addresses.append(address)
        if len(s) > 1:
            for address in self.restoreIpAddresses(s[2:], numbers + [s[:2]]):
                addresses.append(address)
        if len(s) > 2:
            for address in self.restoreIpAddresses(s[3:], numbers + [s[:3]]):
                addresses.append(address)
        return addresses


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        self.assertCountEqual(
            Solution().restoreIpAddresses("25525511135"),
            ["255.255.11.135", "255.255.111.35"],
        )

    def test_zero_input(self):

        self.assertCountEqual(Solution().restoreIpAddresses("0000"), ["0.0.0.0"])

    def test_failing_example(self):

        self.assertCountEqual(
            Solution().restoreIpAddresses("010010"), ["0.10.0.10", "0.100.1.0"]
        )

