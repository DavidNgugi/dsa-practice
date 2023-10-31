# https://leetcode.com/problems/trapping-rain-water/description/
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Two pointers technique
    # left = 0, right = n-1 pointers, leftmax and rightmax variables = 0
    # loop through while l<r
    # unit calculation -> maxHeight(l/r) - current height(l/r)
    # if h[l] <= h[r], check leftmax height, calc units, l++
    # else check rightmax height, calc units, r--
    # units = 0
    # Time -> O(n) (have to go through entire list)
    # Space -> O(1) (have to store only units variable)

    l = 0
    leftMax = 0
    rightMax = 0
    r = len(height) - 1
    units = 0

    while l <= r:
        if height[l] <= height[r]:
            leftMax = max(height[l], leftMax)
            units += leftMax - height[l]
            l += 1
        else:
            rightMax = max(height[r], rightMax)
            units += rightMax - height[r]
            r -= 1

    return units


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    output = 6

    print(trap(height) == output)
