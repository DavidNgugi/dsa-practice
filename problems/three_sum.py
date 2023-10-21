from typing import List

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Time -> O(N^2)
    Space -> O(N)
    """
    # sort array -> O(log n)
    # loop through with two pointers -> O(n^2)

    nums.sort()
    n = len(nums)
    output = []

    for i in range(n):
        # check duplicate
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        front = i + 1
        rear = n - 1
        while front < rear:
            total = nums[i] + nums[front] + nums[rear]
            if total < 0:
                front += 1
            elif total > 0:
                rear -= 1
            else:
                output.append((nums[i], nums[front], nums[rear]))
                # Another conditional for not calculating duplicates
                while front < rear and nums[front] == nums[front + 1]:
                    front += 1
                # Avoiding duplicates check
                while front < rear and nums[rear] == nums[rear - 1]:
                    rear -= 1
                front += 1
                rear -= 1

    return output


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    # nums = [-2, 0, 1, 1, 2]
    # expected = [[-2, 0, 2], [-2, 1, 1]]
    print(threeSum(nums))
