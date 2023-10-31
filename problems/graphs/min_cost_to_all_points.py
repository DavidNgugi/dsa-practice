from heapq import heappop, heappush
from typing import List

# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

# You are given an array points representing integer coordinates of some points on a 2D-plane,
# where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
# |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly
# one simple path between any two points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:
# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

# Constraints:
# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.


def minCostConnectPoints(points: List[List[int]]) -> int:
    """
    Prim's Algorithm
    Time -> O(NlogN) or O(ElogV)
    Space -> O(E+V) or O(n^2) or O(E+V) ??
    """

    n = len(points)

    if n == 1:
        return 0

    # keeps track of diistances for each point
    table = {i: float("Inf") for i in range(n)}
    table[0] = 0

    # min heap keeps track of distances/weight and point
    heap = [(0, 0)]

    visited = set()

    totalCost = 0

    while heap:
        curr_cost, p1 = heappop(heap)

        if p1 in visited or table[p1] < curr_cost:
            continue

        visited.add(p1)
        totalCost += curr_cost

        # visit every point and set distance for each point and update our heap
        for p2 in range(n):
            if p2 not in visited:
                # get manhattan distance
                dist = abs(points[p1][0] - points[p2][0]) + abs(
                    points[p1][1] - points[p2][1]
                )

                # get min distance and store in hashmap and heap
                if dist < table[p2]:
                    table[p2] = dist
                    heappush(heap, (dist, p2))

    return totalCost


if __name__ == "__main__":
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    output = 20

    points2 = [[3, 12], [-2, 5], [-4, 1]]
    output2 = 18

    print(minCostConnectPoints(points) == output)
    print(minCostConnectPoints(points2) == output2)
