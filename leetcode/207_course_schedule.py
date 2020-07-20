import unittest
import collections
from typing import List


class Solution:
    """
    This solution performs a topological sort using Kahn's algorithm.

    First a graph is constructed in the form of a dictionary which contains the
    courses, their requirements and the courses that they themselves enable. Then
    a queue is constructed which contains the courses with no initial requirements.
    As such courses are dequeued from the queue, each course is removed from the graph
    and it is removed from the requirements of all the courses it enables. If a course
    ends up having no requirements after this process then it itself is added to the
    queue. This process repeats until the graph has been completely emptied in which
    case the course schedule is possible. If the graph is non-empty then the course
    schedule is impossible.
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = {
            course: {"id": course, "requirements": set(), "enables": set()}
            for course in range(numCourses)
        }
        for course, *requirements in prerequisites:
            for requirement in requirements:
                courses[course]["requirements"].add(requirement)
                courses[requirement]["enables"].add(course)

        possible_courses = collections.deque(
            [course for course in courses.values() if not course["requirements"]]
        )
        while possible_courses:
            course = possible_courses.popleft()

            for next_course in course["enables"]:
                courses[next_course]["requirements"].remove(course["id"])
                if not courses[next_course]["requirements"]:
                    possible_courses.append(courses[next_course])

            del courses[course["id"]]

        return not courses


class TestSolution(unittest.TestCase):
    def test_true_example(self):

        self.assertTrue(Solution().canFinish(2, [[1, 0]]))

    def test_false_example(self):

        self.assertFalse(Solution().canFinish(2, [[1, 0], [0, 1]]))

    def test_failing_example(self):

        self.assertTrue(Solution().canFinish(3, [[1, 0], [2, 1]]))
