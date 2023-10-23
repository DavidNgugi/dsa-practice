import heapq

from sortedcontainers import SortedList
from typing import List

# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Constraints:
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

def findKthLargest(nums: List[int], k:int)->int:
    """
    Time -> O(log N)
    Space -> O(N)
    """

    heap = []
    for n in nums:
        heapq.heappush(heap, n)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

def findKthLargestWithSorting(nums: List[int], k:int)->int:
    """
    Time -> O(Nlog N)
    Space -> O(N)
    """

    nums = SortedList(nums)

    return nums[len(nums)-k]
    
if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    output = 5
    
    print(findKthLargest(nums, k))
    print(findKthLargestWithSorting(nums, k))
