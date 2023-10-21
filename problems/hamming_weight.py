# https://leetcode.com/problems/number-of-1-bits/description/
# Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: n = 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:

# Input: n = 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

# Constraints:

# The input must be a binary string of length 32.
def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    
    # while count < n:
    #     n &= n - 1
    #     count += 1
    while n > 0:
        # check last bit is 1 using AND operation
        count += n & 1
        # shift right by 1 bit
        n >>= 1
    
    print(count)
    return count

if __name__ == "__main__":
    n = int('11111111111111111111111111111101', 2)
    output = 31

    print(hammingWeight(n) == output)