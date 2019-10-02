import unittest


class Solution:
    """
    This recursive solution is a bit convoluted but essentially it works
    along these lines:

    1. call the function first with the entire string to start the recursion
    2. if the string starts with an integer, multiply the integer with
       decodeString(string_between_next_pair_of_brackets) and append to it
       the string returned by decodeString(string_after_next_pair_of_brackets)
    3. if the string starts with an opening bracket, skip over it
    4. if the string starts with a closing bracket, terminate recursion
    5. if string is a letter, return letter + decodeString(rest_of_the_string)
    """
    def decodeString(self, string: str) -> str:

        def matching_bracket(string: str):
            """
            Returns index of the bracket which closes the bracket which
            starts the string, e.g. calling this with '[2[abc]]' would
            return the index of the last bracket: 7.
            """
            count = 0
            for i, s in enumerate(string):
                if s == '[':
                    count += 1
                elif s == ']':
                    count -= 1
                if not count:
                    return i

        if not string:
            return ''

        char = string[0]
        if char.isdigit():

            # Extract multiplier
            starting_bracket = string.find('[')
            multiplier = int(string[:starting_bracket])

            # Drop multiplier
            string = string[starting_bracket:]
            closing_bracket = matching_bracket(string)
            return (multiplier *
                    self.decodeString(string[:closing_bracket]) +
                    self.decodeString(string[closing_bracket + 1:]))
        elif char == '[':
            return self.decodeString(string[1:])
        elif char == ']':
            return ''
        else:
            return char + self.decodeString(string[1:])


class TestSolution(unittest.TestCase):

    def test_first_example(self):

        self.assertEqual(Solution().decodeString('3[a]2[bc]'), 'aaabcbc')

    def test_second_example(self):

        self.assertEqual(Solution().decodeString('3[a2[c]]'), 'accaccacc')

    def test_third_example(self):

        self.assertEqual(Solution().decodeString('2[abc]3[cd]ef'), 'abcabccdcdcdef')

    def test_fourth_example(self):

        self.assertEqual(Solution().decodeString('100[leetcode]'), 100 * 'leetcode')
