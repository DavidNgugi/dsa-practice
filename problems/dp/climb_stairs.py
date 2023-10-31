# https://leetcode.com/problems/climbing-stairs/description/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# Constraints:

# 1 <= n <= 45

# Best way to think of this:
# To reach stair n, you have to stand on either stair n-1 or n-2
def climbStairs(n):
    """
    :type n: int
    :rtype: int

    Fibonacci memoization
    Time -> O(n)
    Space -> O(n)
    """
    memo = {}

    def climb(n, memo):
        if n == 0 or n == 1:
            return 1

        if n not in memo:
            memo[n] = climb(n - 1, memo) + climb(n - 2, memo)

        return memo[n]

    return climb(n, memo)


def climbStairs2(n):
    """
    :type n: int
    :rtype: int

    Fibonacci tabulation
    Bottom-up approach
    Time -> O(n)
    Space -> O(n)
    """

    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    # we can now count from 2nd stair
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    n = 6
    print(climbStairs(n))
    print(climbStairs2(n))
