# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
# two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the
# LCA definition.

# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2
 
# Constraints:
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.

class TreeNode:
    def __init__(self, x):
        self = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        We will rely upon the invariant of the BST to solve the exercise. 
        We know that the left subtree of each node contains nodes with smaller values and the right subtree
        contains nodes with greater values. We also know that if two nodes, x and y, are on different 
        subtrees of a node z (one in the left portion and one in the right portion), then x and y have z 
        as the lowest common ancestor.

        Time -> O(log N) since we half the nodes we are searching for each time
        Space -> O(1)
        """
        while(root!=None):
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return root
    
    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time -> O(log N) since we half the nodes we are searching for each time
        Space -> O(1)
        """
        while(root!=None):
            if root.val < min(p.val,q.val):
                root = root.right
            elif root.val > max(p.val,q.val):
                root = root.left
            else:
                return root
        return root