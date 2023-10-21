# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    # have a stack to keep track of opening parantheses
    # stack ->

    n = len(s)

    if n == 1:
        return False

    stack = []

    pairs = {"(": ")", "{": "}", "[": "]"}

    for i in range(n):
        if s[i] in pairs:
            stack.append(str(s[i]))
        elif s[i] in pairs.values():
            if len(stack) == 0 or s[i] != pairs[stack.pop()]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    s = "()[]{}"
    print(isValid(s))
