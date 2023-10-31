from linked_lists.base import BaseNode


class Node(BaseNode):
    def __init__(self, data=None):
        super().__init__(data)

    def __repr__(self) -> str:
        return f"Node({self.data})"


# https://leetcode.com/problems/reverse-linked-list/description/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]


# Example 3:
# Input: head = []
# Output: []
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    Time -> O(N)
    Space -> O(1)
    """

    if not head:
        return None

    prev = None
    temp = head

    while temp:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next

    print(prev)
    return prev


def reverseListRecursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    if not head or not head.next:
        return head

    # print(head)

    temp = reverseListRecursive(head.next)

    head.next.next = head
    head.next = None

    return temp


# https://leetcode.com/problems/reverse-linked-list-ii/description/
# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]


# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]
def reverseBetween(head, left, right):
    """
    :type head: ListNode
    :type left: int
    :type right: int
    :rtype: Node
    Time -> O(N)
    Space -> O(1)
    """

    if not head or not head.next:
        return head

    dummy = Node(0)
    dummy.next = head

    prev = dummy
    curr = dummy.next

    for i in range(left - 1):
        curr = curr.next
        prev = prev.next

    print("prev", prev)
    print("curr", curr)

    # reverse nodes in between
    for i in range(right - left):
        if curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

    return dummy.next


if __name__ == "__main__":
    pass
