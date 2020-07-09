import unittest


class Solution:
    """
    This solution is based on using two pointers. The first pointer starts at the
    head of the string and the second pointer starts at the end of the string.
    If both pointers point to letters then the letters are swapped. If a pointer
    does not point to a letter then it is moved forwards or backwards. This process
    repeats until the first pointer meets the second pointer and then the constructed
    string is returned.
    """

    def reverseOnlyLetters(self, S: str) -> str:

        head = 0
        tail = len(S) - 1
        string = list(S)

        while head < tail:
            if string[head].isalpha() and string[tail].isalpha():
                string[head], string[tail] = string[tail], string[head]
                head += 1
                tail -= 1
                continue
            elif not string[head].isalpha():
                head += 1
            else:
                tail -= 1

        return "".join(string)


class TestSolution(unittest.TestCase):
    def test_second_example(self):

        self.assertEqual(
            Solution().reverseOnlyLetters("a-bC-dEf-ghIj"), "j-Ih-gfE-dCba"
        )

    def test_third_example(self):

        self.assertEqual(
            Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"),
            "Qedo1ct-eeLg=ntse-T!",
        )

