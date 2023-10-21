from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, data: T = None):
        self.val = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSymmetric(root):
    """
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
    :type root: TreeNode
    :rtype: bool
    """
    # to be symmetric
    # must have same value in all nodes of the same level
    # must have both left and right leafs

    # dfs approach, check values at each subtree
    # any contradictions, set it to False and return
    # Time = O(n) where n is number of nodes
    # Space O(h) where h is height of deepest tree

    # empty tree is symmetric or reached end without finding an issue
    if not root:
        return True

    def dfs(left, right):
        # if both sides are empty, then it's symmetric
        if not left and not right:
            return True

        # if either nodes are empty or values mattch, not symmetric
        if not left or not right or left.val != right.val:
            return False

        # check left subtree and right subtree
        return (
            left.val == right.val
            and dfs(left.left, right.right)
            and dfs(left.right, right.left)
        )

    return dfs(root.left, root.right)


if __name__ == "__main__":
    # root = [1, 2, 2, 3, 4, 4, 3]
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(3)
    is_symmetric = isSymmetric(tree.root)
    print(is_symmetric)
