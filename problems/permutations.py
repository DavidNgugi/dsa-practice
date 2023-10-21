from itertools import permutations
from typing import List

# https://leetcode.com/problems/permutations/description/

# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]
 
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

def permuteInbuilt(nums: List[int]) -> List[List[int]]:
    """
    Time -> O(N!) // O(N!*N!)
    Space -> O(N!)
    """

    perms = permutations(nums)

    return [list(p) for p in perms]

def permuteRecursive(nums: List[int]) -> List[List[int]]:
    """
    Time -> O(N!) // O(N!*N!) -> Takes N! times to get to each node in N! nodes
    Space -> O(N!) -> Can only have N! permutations
    """       
    result = []

    if len(nums) == 0:
        return [[]]
    
    for i in range(len(nums)):
        n = nums[i]
        # Create a copy of nums without the current element
        remaining_nums = nums[:i] + nums[i + 1:]
        
        # Recursively generate permutations for the remaining elements
        perms = permuteRecursive(remaining_nums)
        
        for perm in perms:
            perm.append(n)
        
        result.extend(perms)
    
    return result

# https://leetcode.com/problems/permutations-ii/description/
# Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.
# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

def permuteUnique(nums):
    """
    Time -> O(N!) // O(N!*N!) -> Takes N! times to get to each node in N! nodes
    Space -> O(N!) -> Can only have N! permutations
    """
    result = []

    visited = {}
    
    if len(nums) == 0:
        return [[]]

    for i in range(len(nums)):
        if nums[i] in visited:
            continue

        n = nums[i]

        visited[n] = 1

        remaining = nums[:i] + nums[i+1:]
        
        perms = permuteUnique(remaining)

        for perm in perms:
            perm.append(n)

        result.extend(perms)

    return result

if __name__ == "__main__":
    nums = [1,2,3]
    output = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    print(permuteInbuilt(nums))
    print(permuteRecursive(nums))

    nums2 = [1,1,2]
    output2 = [[1,1,2],[1,2,1], [2,1,1]]
    print(permuteUnique(nums2))