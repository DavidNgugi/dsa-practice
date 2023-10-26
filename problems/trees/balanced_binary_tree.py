from typing import Optional

# https://leetcode.com/problems/balanced-binary-tree/description/

# Given a binary tree, determine if it is height-balanced.

# Note: A height-balanced binary tree is a binary tree in which the
# depth of the two subtrees of every node never differs by more than one.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: True

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: False

# Example 3:
# Input: root = []
# Output: True
 
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time -> O(N) i.e N is the number of nodes in the binary tree.
        Space -> O(N) i.e N is height of binary tree,
        This is because the recursive calls consume space on the call stack, 
        and in the worst case, the height of the tree is equal to the number of nodes in the tree, 
        resulting in O(N) space complexity.
        """
        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If either the left subtree or the right subtree is not height-balanced 
            if left == -1 or right == -1:
                return -1

            # If the absolute difference between the heights of the left and right subtrees is greater than 1
            if abs(left - right) > 1:
                return -1

            # calculates the height of the current subtree as 1 plus the maximum of the heights 
            # of the left and right subtrees
            return 1 + max(left, right)

        return True if dfs(root) != -1 else False

