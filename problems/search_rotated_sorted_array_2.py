from typing import List

# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target,
# return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false


# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104
def search(nums: List[int], target: int) -> int:
    """
    Time -> O(N)
    Space -> O(1)
    """

    n = len(nums)

    if n < 2:
        return nums[0] == target

    low, high = 0, n - 1

    result = False

    while low <= high:
        if nums[low] == target:
            result = True
            break
        else:
            low += 1

        if nums[high] == target:
            result = True
            break
        else:
            high -= 1

        mid = (high + low) // 2

        if nums[mid] == target:
            result = True
            break

    return result


if __name__ == "__main__":
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    output = True

    print(search(nums, target) == output)
