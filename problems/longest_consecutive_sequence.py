from typing import List

# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 
# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

def longestConsecutive(nums: List[int]) -> int:
    """
    Time -> O(N)
    Space -> O(N)
    """
    if not nums:
        return 0
    
    if len(nums) == 1:
        return 1

    seen = set(nums)
    longest = 1

    for num in seen:
        if num - 1 in seen:
            continue
        count = 1
        # count consecutive values
        while num + count in seen:
            count += 1
        longest = max(longest, count)
        
    return longest

def longestConsecutive2(nums: List[int]) -> int:
    """
    Time -> O(N)
    Space -> O(N)
    """
    if not nums:
        return 0
    
    if len(nums) == 1:
        return 1

    seen = set(nums)
    longest = 0

    for num in nums:
        curr_longest, count = 1, 1
        while num - count in seen:
            seen.remove(num-count)
            count += 1
            curr_longest += 1
        count = 1
        while num + count in seen:
            seen.remove(num+count)
            count += 1
            curr_longest += 1
        longest = max(longest, curr_longest)
        
    
    return longest 

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    output = 4
    nums2 = [0,3,7,2,5,8,4,6,0,1]
    output2 = 9

    print(longestConsecutive(nums) == output)
    print(longestConsecutive(nums2) == output2)

    print(longestConsecutive2(nums) == output)
    print(longestConsecutive2(nums2) == output2)