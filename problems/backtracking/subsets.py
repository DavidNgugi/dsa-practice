from typing import List

# https://leetcode.com/problems/subsets/description/

# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
 
# Constraints:
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Iterative Solution
    Time -> O(N*K)
    Space -> O(N*K)
    """
    n = len(nums)

    if n == 1:
        return [[],nums]

    nums.sort()
    subsets = [[]]
    
    for i in range(n):
        subsets += [sub+[nums[i]] for sub in subsets]

    return subsets

def subsetsDFS(nums: List[int]) -> List[List[int]]:
    """
    DFS Solution
    Time -> O(N*K)
    Space -> O(N*K)
    """

    n = len(nums)

    if n == 1:
        return [[],nums]

    nums.sort()

    subsets = []

    def dfs(nums, subset, subsets, seen):
        if len(nums) < 0:
            return

        if len(subset) > 0:
            key = "".join([str(s) for s in subset])

            if key in seen:
                return
            
            seen.add(key)
        subsets.append(subset)
        
        for i in range(len(nums)):
            dfs(nums[i+1:], subset+[nums[i]], subsets, seen)

    dfs(nums, [], subsets, set())

    return subsets

def subsetsBitManipulation(nums: List[int]) -> List[List[int]]:
    """
    Bit Manipulation 
    Time -> O(N*K)
    Space -> O(N*K)
    """
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res


if __name__ == "__main__":
    nums = [1,2,3]
    output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    print(subsets(nums))
    print("\n",subsetsDFS(nums))
    print("\n",subsetsBitManipulation(nums))