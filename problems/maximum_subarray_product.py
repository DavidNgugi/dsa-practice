from typing import List

# https://leetcode.com/problems/maximum-product-subarray/description/

# Given an integer array nums, find a subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def maxProduct(nums: List[int]) -> int:
    """
    Kadane's algorithm
    Time -> O(N)
    Space -> O(1)
    """

    n = len(nums)

    if n < 2:
        return nums[0]

    maxProd = nums[0]

    currProdLeft = currProdRight = 1
    for i in range(n):
        currProdLeft *= nums[i]
        currProdRight *= nums[n - 1 - i]
        maxProd = max(maxProd, currProdLeft, currProdRight)
        if currProdLeft == 0:
            currProdLeft = 1

        if currProdRight == 0:
            currProdRight = 1

    return maxProd


def maxProductDynamic(nums: List[int]) -> int:
    """
    Dynamic Programming
    Keep track of minimum and maximum products,
    Get maximum product from maximum
    Time -> O(N)
    Space -> O(1)
    """

    if len(nums) < 2:
        return nums[0]

    maxProd = max(nums)

    currMin = currMax = 1

    for n in nums:
        if n == 0:
            currMin = currMax = 1
            continue
        tmp = currMin * n
        currMin = min(currMin * n, currMax * n, n)
        currMax = max(currMax * n, tmp, n)
        maxProd = max(maxProd, currMax)

    return maxProd


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    output = 6

    print(maxProduct(nums) == output)
