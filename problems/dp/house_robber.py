# https://leetcode.com/problems/house-robber/description/

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Find recursive relation
# 1. Recursive (top-down)
# 2. Recursive + memo (top-down)
# 3. Iterative + memo (bottom-up)
# 4. Iterative + N variables (bottom-up)


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    DP tabulation
    Time -> O(n)
    Space -> O(n)
    """

    n = len(nums)

    if n < 3:
        return max(nums)

    dp = [0] * (n + 1)

    dp[0], dp[1] = 0, nums[0]

    for i in range(1, n):
        dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

    return dp[n]


def robRecursive(nums):
    """
    :type nums: List[int]
    :rtype: int
    Time -> O(n)
    Space -> O(n)
    """

    n = len(nums)

    if n < 3:
        return max(nums)

    memo = {}

    def robHouse(i, memo):
        if i in memo:
            return memo[i]

        if i < 0:
            return 0

        if i < n:
            memo[i] = max(robHouse(i - 1, memo), robHouse(i - 2, memo) + nums[i])

        return memo[i]

    return robHouse(n - 1, memo)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    output = 4
    nums2 = [2, 7, 9, 3, 1]
    output2 = 12

    print(rob(nums) == output)
    print(rob(nums2) == output2)

    print(robRecursive(nums) == output)
    print(robRecursive(nums2) == output2)
