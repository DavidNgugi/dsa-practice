from typing import List

# https://leetcode.com/problems/search-a-2d-matrix/description/

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: True

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: False

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    
    result = False

    for i in range(len(matrix)):
        if findTargetInRow(matrix[i], target):
            result = True
            break                
                
    return result

def findTargetInRow(row: List[int], target: int) -> bool:
    low, high = 0, len(row)-1

    result = False

    while low <= high:
        if row[low] == target:
            result = True
            break
        else:
            low += 1

        if row[high] == target:
            result = True
            break
        else:
            high -= 1
        
        mid = (low + high) // 2

        if row[mid] == target:
            result = True
            break
    return result

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    output = True

    print(searchMatrix(matrix, target) == output)