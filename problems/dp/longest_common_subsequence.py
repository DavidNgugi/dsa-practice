# https://leetcode.com/problems/longest-common-subsequence/description/

# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none)
#  deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.


def longestCommonSubsequence(text1: str, text2: str) -> int:
    """
    We use 2D dynamic programming
    Iterative tabulation method
    Time -> O(M*N)
    Space -> O(M*N)
    """
    n1 = len(text1)
    n2 = len(text2)

    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[n1][n2]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    output: 3

    print(longestCommonSubsequence(text1, text2) == output)