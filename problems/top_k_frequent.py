import heapq

from collections import Counter

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    # hashmap of occurences
    # 1. go through n items and count items with k+ items,
    # 2. divide and conquer and go through each half
    # 3. use a heap

    n = len(nums)

    if n == 1 and k == 1:
        return nums

    table = {}

    for i in range(n):
        if nums[i] in table:
            table[nums[i]] += 1
        else:
            table[nums[i]] = 1

    table_list = sorted(table.items(), key=lambda x: x[1], reverse=True)[:k]

    return [k for k, _ in table_list]


def topKFrequentHeap(nums, k):
    # create a max heap
    # pop top k items from heap
    n = len(nums)
    table = {}
    for i in range(n):
        if nums[i] in table:
            table[nums[i]] += 1
        else:
            table[nums[i]] = 1

    heap = list(table.items())

    #  heapify
    heapq.heapify(heap)

    # get frequent items
    output = heapq.nlargest(k, heap, key=lambda x: x[1])
    return [k[0] for k in output]


def topKFrequentQuickSelect(nums, k):
    # count each element
    counter = Counter(nums)
    # partitions and sorts items, get k most common elements to least
    most_frequent = counter.most_common(k)
    return [k[0] for k in most_frequent]


if __name__ == "__main__":
    # nums = [1, 1, 1, 2, 2, 3]
    nums = [4, 1, -1, 2, -1, 2, 3]
    k = 2
    # print(topKFrequent(nums, k))
    # print(topKFrequentHeap(nums, k))
    print(topKFrequentQuickSelect(nums, k))
