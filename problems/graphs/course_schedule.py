from typing import List

# https://leetcode.com/problems/course-schedule/description/

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take
# course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.

# Example 2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
# So it is impossible.

# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    DFS Approach
    Time -> O(N+P) where N is every node and P are every node's prerequisites
    Space -> O(NP)
    """
    # cycle detection -> False

    def buildAdjacencyList(n, edgesList):
        adjList = [[] for _ in range(n)]
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    visited = set()

    def hasCycle(v, stack):
        if v in visited:
            # we are at this vertex and it's been seen before
            if v in stack:
                return True
            return False

        visited.add(v)
        stack.append(v)

        for i in adjList[v]:
            if hasCycle(i, stack):
                return True

        stack.pop()
        return False

    adjList = buildAdjacencyList(numCourses, prerequisites)

    print(adjList)

    for i in range(numCourses):
        # check if completed
        if hasCycle(i, []):
            return False

    return True


def canFinish2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    DFS Approach
    Time -> O(N+P) where N is every node and P are every node's prerequisites
    Spacce -> O(NP)
    """
    # cycle detection -> False

    #  build adj. List of courses
    adjList = {i: [] for i in range(numCourses)}

    for course, pre in prerequisites:
        adjList[course].append(pre)

    visited = set()

    def hasCycle(course):
        # we are at this vertex and it's been seen before
        if course in visited:
            return False

        if adjList[course] == []:
            return True

        visited.add(course)

        for pre in adjList[course]:
            if not hasCycle(pre):
                return False

        # we can take this course, so safe to remove
        visited.remove(course)
        adjList[course] = []

        return True

    for course in range(numCourses):
        # check if completed
        if not hasCycle(course):
            return False

    return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    output = True

    print(canFinish(numCourses, prerequisites) == output)
    print(canFinish2(numCourses, prerequisites) == output)
