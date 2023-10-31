# https://leetcode.com/problems/linked-list-cycle/

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer
# is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Follow up: Can you solve it using O(1) (i.e. constant) memory?


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: ListNode) -> bool:
    """
    **Tortoise and Hare algorithm**

    The idea is that we create two pointers, a slow one and a fast one.
    The slow pointer traverses the linked list 1 node at a time,
    while the fast pointer traverses the linked list 2 nodes at a time.
    If at some point the two pointers meet on the same node, then that means a cycle exists.

    Time -> O(N)
    Space -> O(1)
    """

    if not head or (head and not head.next):
        return False

    fast = head

    while fast and fast.next:
        head = head.next
        fast = fast.next.next

        # checks if exact same in memory (position and value)
        if head is fast:
            return True

    return False
