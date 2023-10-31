# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:


# Input: s = "cbbd"
# Output: "bb"
def longestPalindrome(s: str) -> str:
    """
    Time -> O(N^N)
    Space -> O(N)
    """

    # get substrings, check if palindromic,
    # if it is, check if in set, if not add to set
    # get longest substring in set

    n = len(s)

    if n == 1:
        return s

    substrings = []

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = s[i:j]
            if sub:
                is_palindromic = is_palindrome(sub)
                if is_palindromic and sub not in substrings:
                    substrings.append(sub)

    # print(substrings)
    if len(substrings) > 0:
        ans = max(substrings, key=len)
        return ans
    return None


def is_palindrome(s):
    n = len(s)
    if n == 1:
        return True
    left = 0
    right = n - 1
    response = False
    for i in range(n):
        if left < right:
            if s[left] == s[right]:
                response = True
                left += 1
                right -= 1
            else:
                response = False
                break

    return response


def longestPaliindromeEfficient(s: str) -> str:
    """
    Time -> O(N^N)
    Space -> O(1)
    """
    n = len(s)

    if n == 1:
        return s

    ans = ""

    for i in range(n):
        ans = max(ans, getPalindrome(s, i, i), getPalindrome(s, i, i + 1), key=len)
    return ans


def getPalindrome(s, left, right):
    # uses expand from center technique
    n = len(s)
    if n == 1:
        return s
    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1 : right]


if __name__ == "__main__":
    # s = "babad"
    # output = "bab"

    s = "cbbd"
    output = "bb"

    print(longestPalindrome(s))
    print(longestPaliindromeEfficient(s))
