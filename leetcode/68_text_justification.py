import unittest
from typing import List


class Solution:
    """
    This greedy iterative solution simply consumes words from the list
    until enough words have been consumed to form a single line with
    a single whitespace character between each word. Then this single line is
    justified added to the final list of justified lines. This process is repeated
    until all the words have been consumed.

    The helper function justify_line is a bit awkward but essentially it first
    constructs a list which consists of each word in the line as well as the
    single space characters between each word. Then this list is looped over and
    each space character is increased one by one until the total length of the
    line meets the specified maximum line width. Iterating over the line in
    this manner ensures that the spaces are distributed as evenly as possible
    starting from the left.
    """

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str], last_line=False) -> str:
            """Justifies a single line"""
            needed_padding = maxWidth - len(" ".join(line))

            # Single word lines have whitespace only on the right
            if len(line) == 1:
                return line[0] + " " * needed_padding

            # Last line has extra whitespace only on the right
            if last_line or len(line) == 1:
                return " ".join(line) + " " * needed_padding

            justified_line = [line[0]]
            for word in line[1:]:
                justified_line.append(" ")
                justified_line.append(word)

            # Increment each space character length by one until the line is full
            while needed_padding:
                for i in range(len(justified_line)):
                    if justified_line[i].startswith(" "):
                        justified_line[i] += " "
                        needed_padding -= 1
                    if not needed_padding:
                        break

            return "".join(justified_line)

        lines = []
        line: List[str] = []

        for word in words:
            if len(" ".join(line + [word])) <= maxWidth:
                line.append(word)
            else:
                lines.append(justify_line(line))
                line = [word]

        if line:
            lines.append(justify_line(line, last_line=True))

        return lines


class TestSolution(unittest.TestCase):
    def test_first_example(self):

        words = ["This", "is", "an", "example", "of", "text", "justification."]
        expected = ["This    is    an", "example  of text", "justification.  "]
        self.assertListEqual(Solution().fullJustify(words, 16), expected)

    def test_second_example(self):

        words = ["What", "must", "be", "acknowledgment", "shall", "be"]
        expected = ["What   must   be", "acknowledgment  ", "shall be        "]
        self.assertListEqual(Solution().fullJustify(words, 16), expected)

    def test_third_example(self):

        words = [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ]
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ]
        self.assertListEqual(Solution().fullJustify(words, 20), expected)
