# https://leetcode.com/problems/permutation-in-string/description/

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 
# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
def checkInclusion(s1:str, s2:str)->bool:
    """
    Technique 1 -> Sliding Window, no window size, start from beginning, use hashmap of frequencies
    find window with characters in same frequency
    Time -> O(N)
    Space -> O(N)
    Technique 2 -> Sliding Window, no window size, start from beginning, use count of total of 
    sum of unicode codes of each character in s1
    check sum of unicode codes of characters in window
    if they match, return true, else false
    """
    ord
    # Clarification 1 -> is s2 length > s1 length?
    # 

    n1 = len(s1)
    n2 = len(s2)

    # not taking chances hehe
    if n2 < n1:
        return False

    # can replace with Counter
    freq1 = {}
    
    for i in range(n1):
        if s1[i] in freq1:
            freq1[s1[i]] += 1
        else:
            freq1[s1[i]] = 1

    # print("freq1", freq1)

    result = False

    def isEqual(freq1, freq2):
        for k,v in freq1.items():
            if k not in freq2 or (k in freq2 and v != freq2[k]):
                return False 
        return True
    
    # slide through matching frequencies
    left, right, freqInWindow = 0, 0, {}
    while right < n2:
        if s2[right] in freqInWindow:
            freqInWindow[s2[right]] += 1
        else:
            freqInWindow[s2[right]] = 1

        # check if permutation in string when window size equal to s1 length
        if right-left+1 == n1:
            # print("freqInWindow", freqInWindow)
            # check if frequencies match
            if isEqual(freq1,freqInWindow):
                return True
        if right-left+1 < n1:
            # advance
            right += 1
        else:
            if s2[left] in freqInWindow:
                freqInWindow[s2[left]] -= 1
                left += 1
                right += 1

    return result
    
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    output = True

    print(checkInclusion(s1, s2) == output)