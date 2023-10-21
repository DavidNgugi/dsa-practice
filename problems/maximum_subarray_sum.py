from typing import List

# https://leetcode.com/problems/maximum-subarray/description/

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104

def maxSubArray(nums: List[int]) -> int:
    """
    Kadane's algorithm
    Time -> O(N)
    Space -> O(1)
    """
    # use max variable to store maximum sum, curr to store current sum
    # go through the list, find maximum sum
    # return maximum sum

    n = len(nums)

    if n < 2:
        return nums[0]

    max_sum = curr = nums[0]

    for i in range(n-1):
        curr = max(curr+nums[i+1], nums[i+1])
        max_sum = max(max_sum, curr)
        
    return max_sum

def maxSubArrayDynamic( nums: List[int]) -> int:
    """
    Dynamic programming Approach
    Time -> O(N)
    Space -> O(1)
    """
    # use max variable to store maximum sum, list or hashmap to store sums
    # go through the list, store sums as we check for currSum
    # return maximum sum

    n = len(nums)

    if n < 2:
        return nums[0]

    sums = [0] * n # can use a hashmap but it's not really better
    sums[0] = nums[0]
    maxSum = sums[0]

    for i in range(1, n):
        sums[i] = max(sums[i-1] + nums[i], nums[i])
        # check for max sum or just do this 
        # maxSum = max(maxSum, sums[i]), problem is this will be updated every time
        if sums[i] > maxSum:
            maxSum = sums[i]
        
    return maxSum


if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output = 6

    print(maxSubArray(nums) == output)

