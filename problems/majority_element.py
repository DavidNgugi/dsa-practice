from collections import Counter
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]


# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109


# Follow up: Could you solve the problem in linear time and in O(1) space?
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Hashmap solution
    Time -> O(n)
    Space -> O(n)
    """
    n = len(nums)

    if n == 1:
        return nums

    count = n / 3

    return [k for k, v in Counter(nums).items() if v > count]


def majorityElementBoyer(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    Boyer-Moore Majority algorithm solution
    Time -> O(n)
    Space -> O(1)
    """

    # We can have at most 2 top candidates/elements, we give all others a score of 0
    candidate_1, candidate_2 = 0, 0
    counter_1, counter_2 = 0, 0

    # first pass to identify candidates and set their counts
    for num in nums:
        if counter_1 == 0 and candidate_2 != num:
            candidate_1 = num
            counter_1 = 1
        elif counter_2 == 0 and candidate_1 != num:
            candidate_2 = num
            counter_2 = 1
        elif candidate_1 == num:
            counter_1 += 1
        elif candidate_2 == num:
            counter_2 += 1
        else:
            counter_1 -= 1
            counter_2 -= 1

    # check if they meet count/threshhold
    count = len(nums) / 3
    results = []

    # second pass to set the correct counts
    counter_1, counter_2 = 0, 0
    for num in nums:
        if candidate_1 == num:
            counter_1 += 1
        elif candidate_2 == num:
            counter_2 += 1

    print(candidate_1, candidate_2)
    print(counter_1, counter_2)
    if counter_1 > count:
        results.append(candidate_1)
    if counter_2 > count and candidate_2 != candidate_1:
        results.append(candidate_2)

    return results


if __name__ == "__main__":
    # nums = [3,2,3]
    # nums = [1,2]
    # nums = [2,2]
    # nums = [3,3,4]
    nums = [2, 2, 1, 3]
    print(majorityElementBoyer(nums))
