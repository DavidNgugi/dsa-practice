# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # sliding window
    # left(l)=0, right(r)=n-1 pointers
    # loop across, l < r
    # get max that can fill space -> min(h[l], h[r])
    # min(1,7) * (r-l) -> current area
    # store maximum area
    # advance inwards depending on height of left and right
    # Time -> O(n)
    # Space -> O(1)

    l = 0
    r = len(height) - 1

    max_area = 0

    while l < r:
        current_area = min(height[l], height[r]) * (r - l)
        max_area = max(current_area, max_area)
        if height[l] == height[r]:
            l += 1
            r -= 1
        elif height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = 49

    print(maxArea(height) == output)
