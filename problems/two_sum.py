def twoSumByTwoPointers(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # two pointers, front and rear
    # front = 0 -> to mid
    # <-rear = n-1 to mid
    # mid = (n+1)/2
    # add numbers and check if target, if it is, return indices, otherwise advance until base case nums[front] + nums[rear] = target

    n = len(nums)

    front, rear = 0, n - 1

    # sorts asc by default
    nums.sort()

    while front <= rear:
        s = nums[front] + nums[rear]
        if s == target:
            return [front + 1, rear + 1]
        elif s > target:
            rear -= 1
        else:
            front += 1
    return []


def twoSumHashTable(nums, target):
    # use hash table to keep track of indexes, use complement to find if already in table
    # O(n)
    n = len(nums)

    if n == 1:
        return []

    table = {}

    for i in range(n):
        c = target - nums[i]
        if c in table:
            return [i, table[c]]
        else:
            table[nums[i]] = i


def twoSumBinarySearch(nums, target):
    n = len(nums)

    if n == 1:
        return []

    # go through array in half the time O(nlog n)
    # we search from left of target is less than the front
    # search from middle if target is larger than middle

    for i in range(n):
        front, rear = i + 1, n - 1
        comp = target - nums[i]
        while front <= rear:
            mid = front + (rear - front) / 2
            if nums[mid] == comp:
                return [i + 1, mid + 1]
            elif nums[mid] < comp:
                front = mid + 1
            elif nums[mid] > comp:
                rear = mid - 1
