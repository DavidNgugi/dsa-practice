from collections import deque

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
# return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    Time - O(m * n)
    Space - O(mn)
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    def is_island(grid, i, j):
        return (
            True
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"
            else False
        )

    # bfs, check neighbours
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1" and (row, col):
                islands += 1
                queue = deque([(row, col)])
                while queue:
                    i, j = queue.popleft()
                    grid[i][j] = "-1"
                    # check neighbours (left, right, down, top)
                    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        r, c = i + dr, j + dc
                        if is_island(grid, r, c) and (r, c):
                            queue.append((r, c))
                            grid[r][c] = "-1"

    return islands


def numIslandsDFSRecursive(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    # dfs, check neighbours
    def search(grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "-1"  # ensure we don't check visited node
            search(grid, i - 1, j)
            search(grid, i + 1, j)
            search(grid, i, j + 1)
            search(grid, i, j - 1)
            return 1
        return 0

    for row in range(rows):
        for col in range(cols):
            islands += search(grid, row, col)

    return islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    expected = 1
    # print(numIslands(grid) == 1)
    print(numIslandsDFSRecursive(grid) == 1)
