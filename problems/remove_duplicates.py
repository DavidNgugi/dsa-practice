# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
# the smallest in lexicographical order
#  among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.
def removeDuplicateLetters(s: str) -> str:
    """
    Time -> O(N)
    Space -> O(N)
    """
    # Solution 1
    # use a set and visit all chars ensuring we haven't visited it
    # sort based on position in index of number of occurrence

    # Solution 2
    # Build map of occurences
    # Stack to keep track of latest elements accordiing to lexicographic order

    n = len(s)

    last_occ, stack, visited = {}, [], set()

    for i in range(n):
        last_occ[s[i]] = i

    for i in range(n):
        if s[i] not in visited:
            while stack and stack[-1] > s[i] and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(s[i])
            visited.add(s[i])

    return "".join(stack)


if __name__ == "__main__":
    pass
