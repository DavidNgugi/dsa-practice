from base import BaseNode


class Node(BaseNode):
    def __init__(self, data=None):
        super().__init__(data)

    def __repr__(self) -> str:
        return f"Node({self.data})"


class CircularLinkedList:
    def __init__(self):
        self.head = None
