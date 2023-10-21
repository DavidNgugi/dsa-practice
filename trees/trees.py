from pprint import pprint
from typing import TypeVar, List

# from queues.queues import Queue
from collections import deque

T = TypeVar("T")


class Node:
    def __init__(self, data: T = None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def inOrderRecursive(self, root_node: Node):
        """
        - First, visit all the nodes in the left subtree
        - Then the root node
        - Visit all the nodes in the right subtree
        """
        if not root_node:
            return
        if root_node:
            self.inOrderRecursive(root_node.left)
            self.display(root_node)
            self.inOrderRecursive(root_node.right)

    def inOrderIterative(self, root_node: Node):
        """
        - First, go through tree as long as stack is not empty
        - pop last node from stack
        - If not visited, add right node to stack
        - add node to stack and mark as visited
        - add left node to stack
        """

        if not root_node:
            return

        stack = [(root_node, False)]
        output: List[Node] = []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    output.append(node)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        [self.display(node) for node in output]

    def preOrderRecursive(self, root_node):
        """
        - Visit root node
        - Visit all the nodes in the left subtree
        - Visit all the nodes in the right subtree
        """
        if not root_node:
            return
        if root_node:
            self.display(root_node)
            self.preOrderRecursive(root_node.left)
            self.preOrderRecursive(root_node.right)

    def preOrderIterative(self, root_node: Node):
        """
        - First, go through tree as long as stack is not empty
        - pop last node from stack
        - If not visited, add right node to stack
        - add left node to stack
        - add node to stack and mark as visited
        """

        if not root_node:
            return

        stack = [(root_node, False)]
        output: List[Node] = []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    output.append(node)
                else:
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))

        [self.display(node) for node in output]

    def postOrderRecursive(self, root_node):
        """
        - Visit all the nodes in the left subtree
        - Visit all the nodes in the right subtree
        - Visit the root node
        """
        if not root_node:
            return
        if root_node:
            self.postOrderRecursive(root_node.left)
            self.postOrderRecursive(root_node.right)
            self.display(root_node)

    def postOrderIterative(self, root_node: Node):
        """
        - First, go through tree as long as stack is not empty
        - pop last node from stack
        - If not visited, add node to stack and mark as visited
        - add right node to stack
        - add left node to stack
        """

        if not root_node:
            return

        stack = [(root_node, False)]
        output: List[Node] = []

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    output.append(node)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        [self.display(node) for node in output]

    def display(self, root_node):
        print(str(root_node.data), end="->")


def bfs(start):
    """Go down the tree by level/layer"""
    if not start:
        return
    queue = deque([start])
    # start from root
    # queue.enqueue(start)
    visited = set()

    while queue:
        node = queue.popleft()
        print(node.data)

        # go through child nodes
        if node.left and node.left not in visited:
            queue.append(node.left)
            visited.add(node.left)
            bfs(node.right)
        elif node.right and node.right not in visited:
            queue.append(node.right)
            visited.add(node.right)
            bfs(node.left)


def dfs(node):
    """Go down the tree until max depth"""
    if not node:
        return

    visited = set()
    dfs_inner(node, visited)


def dfs_inner(node, visited):
    # inorder traversal - left first
    if node and node.data not in visited:
        visited.add(node.data)
        print(node.data)
        return dfs_inner(node.left, visited) or dfs_inner(node.right, visited)

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """

    if not root:
        return
    
    left = invertTree(root.left)
    right = invertTree(root.right)

    root.left = right
    root.right = left
            
    return root

if __name__ == "__main__":
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(12)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(6)
    tree.root.right = Node(9)

    print("Inorder recursive:")
    tree.inOrderRecursive(tree.root)
    print("\nInorder Iterative:")
    tree.inOrderIterative(tree.root)
    print("\nPreorder Recursive:")
    tree.preOrderRecursive(tree.root)
    print("\nPreorder Iterative:")
    tree.preOrderIterative(tree.root)
    print("\nPostorder Recursive:")
    tree.postOrderRecursive(tree.root)
    print("\nPostorder Iterative:")
    tree.postOrderIterative(tree.root)

    # print("\nbfs:")
    # bfs(tree.root)
    # print("\ndfs:")
    # dfs(tree.root)

    # invertTree(tree.root)
