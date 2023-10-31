from collections import deque
from typing import List

# https://leetcode.com/problems/max-area-of-island/description/

# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) Y
# ou may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:

# Input: grid = [
#   [0,0,1,0,0,0,0,1,0,0,0,0,0],
#   [0,0,0,0,0,0,0,1,1,1,0,0,0],
#   [0,1,1,0,1,0,0,0,0,0,0,0,0],
#   [0,1,0,0,1,1,0,0,1,0,1,0,0],
#   [0,1,0,0,1,1,0,0,1,1,1,0,0],
#   [0,0,0,0,0,0,0,0,0,0,1,0,0],
#   [0,0,0,0,0,0,0,1,1,1,0,0,0],
#   [0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    Similar to number of islands, this time we just find islands and increment area variable
    Time -> O(M*N)
    Space -> O(1)
    """
    # iterate thorugh grid
    # if we find a one, check all directions

    rows = len(grid)
    cols = len(grid[0])

    maxArea = 0

    def is_island(grid, i, j):
        return (
            True
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1
            else False
        )

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and (row, col):
                area = 1
                q = deque([(row, col)])
                # mark as visited
                grid[row][col] = -1
                while q:
                    i, j = q.popleft()
                    for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        r, c = i + dr, j + dc
                        if is_island(grid, r, c) and (r, c):
                            q.append((r, c))
                            grid[r][c] = -1
                            area += 1
                    maxArea = max(maxArea, area)

    print("maxArea=", maxArea)
    return maxArea


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    output = 6

    print(maxAreaOfIsland(grid) == output)
