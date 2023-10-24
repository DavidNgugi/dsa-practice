
# https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def isPalindrome(s: str) -> bool:
    """
    Time -> O(N)
    Space -> O(1)
    """
    s = ''.join([c for c in s.lower().strip() if c.isalnum() or c.isnumeric()])

    n = len(s)

    if n < 2:
        return True

    left, right = 0, n-1

    response = False
    for _ in range(n):
        if left < right:
            if s[left] == s[right]:
                response = True
                left += 1
                right -= 1
            else:
                response = False
                break

    return response

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    output = True

    print(isPalindrome(s) == output)
