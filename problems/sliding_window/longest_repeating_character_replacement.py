from collections import Counter

# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# You are given a string s and an integer k. You can choose any character of the string and change it to 
# any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the 
# above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.
 
# Constraints:
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

def characterReplacement(s: str, k: int) -> int:
    """
    Time -> O(N)
    Space -> O(26) = O(1)
    """
    n = len(s)

    if k == len(s):
        return len(s)

    maxLength, left, freq = 0, 0, Counter()

    for right in range(n):
        # Store the frequency of each character
        freq[s[right]] += 1
        width = right-left+1 # matches to cell count
        # calc replacement cost
        if width - max(freq.values()) > k:
            freq[s[left]] -=1
            # shrink window
            left += 1
        else:
            maxLength = max(maxLength, width)
        
    return maxLength

def characterReplacement2(s: str, k: int) -> int:
    """
    Reduce memory by only keeping track of the largest substring length
    Time -> O(N)
    Space -> O(26) = O(1)
    """
    maxlen, largestCount, arr = 0, 0, Counter()

    for idx in range(len(s)):
        # Store the frequency of each character
        arr[s[idx]] += 1
        largestCount = max(largestCount, arr[s[idx]])
        if maxlen - largestCount >= k:
            arr[s[idx - maxlen]] -= 1
        else:
            maxlen += 1
    return maxlen

if __name__ == "__main__":
    s = "ABAB"
    k = 2
    output = 4

    s2 = "AABABBA"
    k2 = 1
    output2 = 4

    print(characterReplacement(s, k) == output)
    print(characterReplacement(s2, k2) == output2)

    print(characterReplacement2(s, k) == output)
    print(characterReplacement2(s2, k2) == output2)