# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    Time -> O(n)
    Space -> O(n)
    """

    n = len(s)
    m = len(t)

    if n != m:
        return False

    n_map = {}
    for i in range(n):
        if s[i] in n_map:
            n_map[s[i]] += 1
        else:
            n_map[s[i]] = 1

    for i in range(m):
        if t[i] not in n_map:
            return False
        else:
            n_map[t[i]] -= 1

    for i in range(m):
        if n_map[s[i]] != 0:
            return False

    return True


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    print(isAnagram(s,t))
