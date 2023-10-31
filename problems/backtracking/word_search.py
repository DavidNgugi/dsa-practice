from typing import List

# https://leetcode.com/problems/word-search/description/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
# or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: True

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: True

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: False

# Constraints:
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?


class Solution(object):
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time -> O(N*M*K) #  k -> word length
        Space -> O(1) # we are not storing anything else
        """

        if not board:
            return False

        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if self.dfs(board, row, col, 0, word):
                    return True
        return False

    def dfs(self, board, i, j, index, word):
        # what would make this false?
        # i < 0 or j < 0 when checking directions
        # i > number of rows
        # j > number of columns
        # index >= length of word
        # letters don't match in position
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or index >= len(word)
            or board[i][j] != word[index]
        ):
            return False

        # if all characters checked
        if len(word) - 1 == index:
            return True

        # check in all directions for remaining words

        # you can use a loop although less efficient

        # for dr,dc in ((1,0), (-1,0), (0,-1), (0,1)):
        #     # mark position as visited
        #     tmp = board[i][j]
        #     board[i][j] = '-1'
        #     if self.dfs(board, i + dr, j + dc, index+1, word):
        #         return True
        #     board[i][j] = tmp

        # or just check all cases, more efficient

        tmp = board[i][j]
        board[i][j] = "-1"

        res = (
            self.dfs(board, i + 1, j, index + 1, word)
            or self.dfs(board, i - 1, j, index + 1, word)
            or self.dfs(board, i, j - 1, index + 1, word)
            or self.dfs(board, i, j + 1, index + 1, word)
        )

        board[i][j] = tmp

        return res


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    output = True

    s = Solution()
    print(s.exist(board, word) == output)
