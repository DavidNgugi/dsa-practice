# https://leetcode.com/problems/house-robber-ii/description/

# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security 
# system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of 
# money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
# Example 2:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 3:

# Input: nums = [1,2,3]
# Output: 3

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    Time -> O(n)
    Space -> O(n)
    """
    n = len(nums)

    if n < 3:
        return max(nums)
    
    # strategy 1, start from first house
    dp1 = [0] * (n)
    dp1[0], dp1[1] = nums[0], nums[0]
    # strategy 2, start from 2nd house
    dp2 = [0] * (n)
    dp2[0], dp2[1] = 0, nums[1]
    
    for i in range(2, n):
        dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])
    
    return max(dp1[n-2], dp2[n-1] )

if __name__ == '__main__':
    nums = [2,3,2]
    output = 3

    nums2 = [1,2,3,1]
    output2 = 4

    nums3 = [1,2,3]
    output3 = 3

    print(rob(nums) == output)
    print(rob(nums2) == output2)
    print(rob(nums3) == output3)