from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, data: T = None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None


"""
Given the root of a binary tree and the value of a target node,
target, and an integer K, return a list of the values of all nodes
that have a distance of K from the target node
Example:

target = 5, K = 2

                3
             /      \
            5          1
         /    \      /   \
        6       2   0     8
               / \
              7   4

return: [1,7,4]
"""


# dfs approach
# can k < 1?
# if root is target and k=1, return all nodes?
# if all nodes are target?
# can target not be in tree?
# is there an order of retrieving nodes?
def find_k_distanced(root, target, k):
    nodes = []

    distance = 1

    def dfs(node, distance):
        if node:
            if node.data == target:
                # print(f"found target node {target}")
                distance = 0  # reset

            # print(distance)

            if distance == k:
                # print("found node in k distance")
                nodes.append(node.data)

            distance += 1
            dfs(node.right, distance)
            dfs(node.left, distance)

        return nodes

    nodes = dfs(root, distance)

    print(nodes)

    return nodes


if __name__ == "__main__":
    tree = Tree
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(1)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(2)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(8)

    find_k_distanced(tree.root, 5, 0)
