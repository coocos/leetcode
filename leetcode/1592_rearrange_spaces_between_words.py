import unittest


class Solution:
    """
    This solution starts by counting the amount of space characters in the
    text. The padding between each word can be computed with the following
    formula:

        padding = spaces // (len(words) - 1)

    Once the amount of padding is known, the solution starts to construct
    a temporary list by taking the next word and adding padding after it.
    This is repeated until all the words have been consumed. If the amount
    of used padding has not exhausted all the space characters then those
    remaining space characters are appended to the end of the list. Finally
    the list is turned into a string and returned.
    """

    def reorderSpaces(self, text: str) -> str:

        spaces = 0
        for char in text:
            if char == " ":
                spaces += 1

        if not spaces:
            return text

        reordered = []
        words = text.split()
        padding = spaces // (len(words) - 1) if len(words) > 1 else spaces
        for word in words:
            reordered.append(word)
            reordered.append(" " * min(padding, spaces))
            spaces -= padding
        return "".join(reordered) + " " * spaces


class TestSolution(unittest.TestCase):
    def test_rerodering_text_with_trailing_space(self):
        text = "  walks  udp package   into  bar a"
        expected = "walks  udp  package  into  bar  a "
        self.assertEqual(Solution().reorderSpaces(text), expected)

    def test_reordering_text_with_single_word(self):
        text = "  hello"
        expected = "hello  "
        self.assertEqual(Solution().reorderSpaces(text), expected)

    def test_reordering_single_character_words(self):
        text = "a b c "
        expected = text
        self.assertEqual(Solution().reorderSpaces(text), expected)

    def test_reordering_space_in_the_middle_of_words(self):
        text = "a b   c d"
        expected = "a b c d  "
        self.assertEqual(Solution().reorderSpaces(text), expected)
