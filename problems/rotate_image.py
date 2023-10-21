# https://leetcode.com/problems/rotate-image/description/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # Reasoning #1: 
    # if matrix is 1 column, return matrix
    # loop through both -> O(MxN)/O(N^2), O(1)
    # a[row][col]
    # a[i][j] -> a[i][j+n-1]
    # a[2][0] -> a[0][0]
    # a[0][0] -> a[0][2]
    
    # make upside-down
    matrix.reverse()
    
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 1 and cols == 1:
        return matrix

    for i in range(rows):
        for j in range(i):
            # swap at current
            matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix

def rotate2(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    Time -> O(M*N)
    Space -> O(1)
    Get transpose and reverse
    """
    matrix[:] = zip(*matrix[::-1])

    return matrix

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [[7,4,1],[8,5,2],[9,6,3]]

    # comment one out since matrix has been changed by previous
    print(rotate(matrix))
    # print(rotate2(matrix))