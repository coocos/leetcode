import unittest
from typing import List


class Solution:
    """
    This solution simply iterates over the operations, pushes
    each folder to a stack and pops the stack if the operation is ../
    and the stack contains folders. Nothing is done if the operation
    is ./. The minimum amount of operations needed to return to
    the main folder is the size of the stack after applying all operations
    from the log.
    """

    def minOperations(self, logs: List[str]) -> int:

        stack: List[str] = []

        for operation in logs:
            if operation == "./":
                pass
            elif operation == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(operation)

        return len(stack)


class TestSolution(unittest.TestCase):
    def test_example(self):

        logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
        self.assertEqual(Solution().minOperations(logs), 3)
