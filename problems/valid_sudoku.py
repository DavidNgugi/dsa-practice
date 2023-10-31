from typing import List

# https://leetcode.com/problems/valid-sudoku/description/

# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:

# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


def isValidSudoku(board: List[List[str]]) -> bool:
    """
    Time -> O(M*N)
    Space -> O(N) -> N is worst case 9*9 values
    """

    # validate row, 1-9, no repeat
    # validate col, 1-9, no repeat
    # each 3x3 matrix (9) must contain 1-9, no repeat

    # hashmap -> frequencies, prevent dupliation
    # set -> seen?, if seen before (repeat), return False
    # ignore empty

    seenInRow = [set() for x in range(9)]
    seenInCol = [set() for x in range(9)]
    squares = [[set() for x in range(3)] for y in range(3)]

    print("squares", squares)

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            print(
                "looking at (row,col)",
                (i, j),
                "value",
                board[i][j],
                "square",
                squares[i // 3][j // 3],
            )
            if (
                board[i][j] in seenInRow[i]
                or board[i][j] in seenInCol[j]
                or
                # value already in square
                board[i][j] in squares[i // 3][j // 3]
            ):
                print("found repeat")
                return False
            seenInRow[i].add(board[i][j])
            seenInCol[j].add(board[i][j])
            squares[i // 3][j // 3].add(board[i][j])
    return True
