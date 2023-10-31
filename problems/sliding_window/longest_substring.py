# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string s, find the length of the longest
# substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.
def lengthOfLongestSubstringNoRepeat(s: str) -> int:
    """
    Time -> O(N)\n
    Space -> O(N) -> Set stores all characters
    """
    # len(s) is < 2, then len(s) -> 0 or 1
    # Time -> O(N)
    # Space -> O(N) -> Set stores all characters
    # sliding window technique (right, left pointers)
    # set to keep track of unique characters in window
    # maxLen variable to keep track of maximum length of substring from window
    # window = right-left+1
    # if encounter duplicate, move left pointer and remove all chaaracters in at left pos

    n = len(s)

    if n < 2:
        return n

    maxLen, left, seen = int(0), int(0), set()

    for right in range(n):
        # remove previous duplicates in window
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxLen = max(maxLen, right - left + 1)

    # print(seen)
    return maxLen


def lengthOfLongestSubstring2(s: str) -> int:
    """
    Time -> O(N)\n
    Space -> O(N) -> Set stores all characters
    """
    # len(s) is < 2, then len(s) -> 0 or 1

    # sliding window technique (right, left pointers)
    # Hashmap to keep track of character occurences in window
    # maxLen variable to keep track of maximum length of substring from window
    # window = right-left+1
    # if encounter duplicate, move left pointer and remove all chaaracters in at left pos

    n = len(s)

    if n < 2:
        return n

    maxLen = 0
    seen = {}

    left = 0

    for right in range(n):
        # remove previous duplicates in window
        while s[right] in seen and seen[s[right]] < 2:
            del seen[s[left]]
            left += 1
        seen[str(s[right])] = 1
        maxLen = max(maxLen, right - left + 1)

    return maxLen


if __name__ == "__main__":
    s = "abcabcbb"
    output = 3

    print(lengthOfLongestSubstringNoRepeat(s) == output)
