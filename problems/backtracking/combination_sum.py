from typing import List

# https://leetcode.com/problems/combination-sum/description/

# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 
# combinations for the given input.

# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:
# Input: candidates = [2], target = 1
# Output: []
 
# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Time -> O(NlogN)
    Space -> O(N)
    """
    
    n = len(candidates)

    if n == 1:
        return [candidates[0]] if candidates[0] == target else []
    
    combinations = []

    #  DFS/backtracking approach
    def evaluate(nums, target, combinations, combination):
        # not possible so ignore
        if target < 0:
            return

        #  we've completed combination check
        if target == 0:
            combinations.append(combination)
            return

        for i in range(len(nums)):
            evaluate(nums[i:], target-nums[i] , combinations, combination+[nums[i]])

    evaluate(candidates, target, combinations, [])

    return combinations

if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    output = [[2,2,3],[7]]

    print(combinationSum(candidates, target))