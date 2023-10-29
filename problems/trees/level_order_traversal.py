from collections import defaultdict, deque
from typing import List, Optional

# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
   

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Iterative approach, use queue
        Time -> O(N)
        Space -> O(N)
        """
         
        if not root: 
           return []
        
        output = defaultdict(list)

        q = deque([root])

        level = 1

        while q:
            output[level] = []
            q_size = len(q)

            for _ in range(q_size):
                node = q.popleft()
                output[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return output.values()


    def levelOrderRecursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        DFS approach -> Get nodes in-order (left to right level by level)
        Time -> O(N)
        Space -> O(N)
        """

        if not root: 
           return []
        
        output = defaultdict(list)

        def inorder(node, level):
            if not node:
                return
            nonlocal output
            inorder(node.left, level+1)
            output[level].append(node.val)
            inorder(node.right, level+1)

            
        inorder(root, 1)

        return [v for _,v in sorted(output.items())]
    