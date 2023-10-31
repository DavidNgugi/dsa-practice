from functools import cache

# https://leetcode.com/problems/powx-n/description/

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:
# -100.0 < x < 100.0
# -231 <= n <= 231-1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104


def myPow(x: float, n: int) -> float:
    """
    Binary Exponentiation Technique
    Reasoning: To compute base^exponent, we can calculate base^(exponent/2) and then square it.
    Time -> O(log N)
    Space -> O(1)
    """
    if x == 0:
        return 0

    if n == 0:
        return 1

    def calc(x, n):
        curr = 1
        while n != 0:
            if n % 2 == 0:
                x = x * x
                # reduce search space by half
                n //= 2
            curr *= x
            n -= 1
        return curr

    if n > 0:
        return calc(x, abs(n))
    elif n < 0:
        return 1 / calc(x, abs(n))


# cache to avoid time exceeding
@cache
def myPowRecursive(x: float, n: int) -> float:
    """
    Binary Exponentiation Technique (Recursive)
    Reasoning: To compute base^exponent, we can calculate base^(exponent/2) and then square it.
    Time -> O(log N)
    Space -> O(N)
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1 / x
    return (
        myPowRecursive(x, n // 2) * myPowRecursive(x, n // 2) * myPowRecursive(x, n % 2)
    )


if __name__ == "__main__":
    x = 2.00000
    n = 10
    output = 1024.00000

    print(myPow(x, n) == output)
    print(myPowRecursive(x, n) == output)
