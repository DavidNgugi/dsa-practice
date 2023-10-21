def remove_duplicate(s):
    """
    Given string s consisting of lowercase english letters,
    a duplicate removal consists of choosing two adjacent and equal letters and removing them
    we repeatedly make duplicate removals on s until we no longer can
    return final string
    example Input s = 'abbaca'
    output = 'ca'
    Time - O(n)
    Space - O(n)
    """

    # [], [a],[a, b],

    if not s:
        return s

    n = len(s)

    stack = []

    for i in range(n):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return "".join(stack)


def remove_duplicate_kwise(s, k):
    """
    What if instead of adjacent pairs (2), you want to remove k-wise duplicates?
    Example s = 'deeedbbcccbdaa', k=3
    Output = 'aa'
    """

    # eee -> ddbbcccbdaa
    # ccc -> ddbbbdaa
    # bbb -> dddaa
    # ddd -> aa

    # k=1 -> no duplicates
    # count of occurrences, stored in dict
    # iif stack empty, we add element to stack and set it's count to 1
    # if top element is current element and occurrence is 2, we can't add then, we pop all other occurrences
    # else we append and give new element a count of 1
    # stack = [], [d], [d,e], [d,e,e], [d,e,e,e], [d], [d,d], [d,d,b], [d,d,b,b], [d,d,b,b,c], [d,d,b,b,c,c], [d,d,b,b,c,c,c]
    # [d,d,b,b], [d,d,b,b,b], [d,d], [d,d,d], [], [a], [a,a]

    if not s or k == 1:
        return s

    n = len(s)

    stack = []

    occur_map = {}

    for i in range(n):
        if len(stack) > 0:
            # check conditions to delete or add
            # if top element is our character
            if stack[-1] == s[i]:
                if occur_map[stack[-1]] == k - 1:
                    for _ in range(k - 1):
                        stack.pop()
                else:
                    stack.append(s[i])
                    occur_map[s[i]] += 1
            else:
                stack.append(s[i])
                occur_map[s[i]] = 1
        else:
            # default add to stack if empty
            stack.append(s[i])
            occur_map[s[i]] = 1

    return "".join(stack)

    # Time - O(n)
    # Space - O(n)


if __name__ == "__main__":
    s_1 = "abbaca"
    expected_1 = "ca"
    output_1 = remove_duplicate(s_1)

    print((output_1, expected_1 == output_1))

    s_2 = "deeedbbcccbdaa"
    output_2 = remove_duplicate_kwise(s_2, 3)
    expected_2 = "aa"

    print((output_2, expected_2 == output_2))
