from typing import TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, data: T = None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
