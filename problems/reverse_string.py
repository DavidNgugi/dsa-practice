def reverse(string: str) -> str:
    """
    Time -> O(N)
    Space -> O(N)
    """

    s = [c for c in string]

    l, r = 0, len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    print("reverse:", "".join(s))
    return "".join(s)


def reverse2(string: str) -> str:
    """
    Time -> O(N)
    Space -> O(N)
    """
    output = ""

    for i in range(len(string) - 1, -1, -1):
        output += string[i]

    print("reverse2:", output)
    return output


def reverseRecursive(string: str) -> str:
    """
    Time -> O(N)
    Space -> O(N)
    """
    output = []

    def reverse(string, index, output):
        if index < 0:
            return

        output.append(string[index])

        reverse(string, index - 1, output)

    reverse(string, len(string) - 1, output)

    print("reverseRecursive:", output)
    return "".join(output)


if __name__ == "__main__":
    s = "abcdef"
    output = "fedcba"

    print(reverse(s) == output)
    print(reverse2(s) == output)
    print(reverseRecursive(s) == output)
