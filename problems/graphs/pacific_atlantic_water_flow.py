from collections import deque
from typing import List

# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right
# and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights
# where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly
# north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

# Example 2:
# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

# Constraints:
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Time -> O(V)
    Space -> O(V)
    """
    rows = len(heights)
    cols = len(heights[0])

    in_pacific = in_atlantic = set()
    p, q = deque(), deque()

    def is_sloping(heights, i, j, r, c):
        if (
            0 <= i < len(heights)
            and 0 <= j < len(heights[0])
            and 0 <= r < len(heights)
            and 0 <= c < len(heights[0])
        ):
            return heights[r][c] >= heights[i][j]
        return False

    def bfs(q):
        seen = set()
        while q:
            i, j = q.popleft()

            if (i, j) not in seen:
                seen.add((i, j))

            # check neighboring cells
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                r, c = i + dr, j + dc
                if is_sloping(heights, i, j, r, c) and (r, c):
                    if (r, c) not in seen:
                        seen.add((r, c))
                        q.append((r, c))

        return seen

    # fill coordiinates for pacific and atlantic cells
    for i in range(rows):
        p.append((i, 0))
        q.append((i, cols - 1))

    for j in range(cols):
        p.append((0, j))
        q.append((rows - 1, j))

    in_pacific = bfs(p)
    in_atlantic = bfs(q)

    return list(in_pacific.intersection(in_atlantic))


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]

    print(pacificAtlantic(heights))
