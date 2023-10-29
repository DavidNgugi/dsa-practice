from typing import List

# https://leetcode.com/problems/spiral-matrix/description/?source=submission-noac

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    Time -> O(M*N)
    Space -> O(1) - can be considered O(N) if taking into account the result list
    """
    # define boundaries of matrix we're looking at
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    result = []

    # check if within boundaries
    while left < right and top < bottom:
        # move right
        for i in range(left, right):
            result.append(matrix[top][i])
        
        # move to next row
        top += 1

        # move down
        for i in range(top, bottom):
            result.append(matrix[i][right-1]) # -1 because it's out of bounds

        # reduce window
        right -= 1

        # edge case when pointers meet, we are done
        if not (top < bottom and left < right):
            break

        # move left
        for i in range(right-1, left-1, -1):
            result.append(matrix[bottom-1][i])

        # reduce window
        bottom -= 1

        # move up
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        
        # reduce window
        left += 1
        
    return result

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [1,2,3,6,9,8,7,4,5]

    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    output2 = [1,2,3,4,8,12,11,10,9,5,6,7]

    print(spiralOrder(matrix) == output)
    print(spiralOrder(matrix2) == output2)
                    
