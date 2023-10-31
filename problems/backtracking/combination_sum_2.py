from typing import List

# https://leetcode.com/problems/combination-sum-ii/description/

# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]

# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Time -> O(NlogN)
    Space -> O(N)
    """
    if len(candidates) < 2:
        return [candidates] if candidates[0] == target else []

    combinations = []

    # assume not sorted
    candidates.sort()

    def dfs(nums, target, combination, combinations):
        if target < 0:
            return

        if target == 0:
            combinations.append(combination)
            return

        for i in range(len(nums)):
            # skip larger values than target
            if nums[i] > target:
                continue
            # skip if previous value is duplicate
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # skip repeated value thus i+1
            dfs(nums[i + 1 :], target - nums[i], combination + [nums[i]], combinations)

    dfs(candidates, target, [], combinations)
    return combinations


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    output = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    print(combinationSum2(candidates, target))
