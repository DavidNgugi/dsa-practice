import gc
from base import BaseNode


class Node(BaseNode):
    def __init__(self, data=None):
        super().__init__(data)
        self.prev = None

    def __repr__(self) -> str:
        return f"Node({self.data})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> None:
        """print the linked list"""
        try:
            temp = self.head
            while temp:
                print(f"{str(temp.data)}", end="<-->")
                temp = temp.next
        except Exception as e:
            print(e)
        return ""

    def length(self):
        """return the length of the linked list"""
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def insert(self, data, index=None):
        """insert data to tail or at a given index"""
        try:
            if index is None:
                index = self.length()

            if index < 0 or index > self.length():
                raise ValueError("Invalid index")

            print(f"inserting {data} into index {index}")

            if index == 0:
                node = Node(data)
                if not self.head:
                    # add head
                    node.next = self.head
                    self.head = node
                else:
                    # make head
                    node.next = self.head
                    self.head.prev = node
                    self.head = node
            else:
                current = self.head
                while index > 0:
                    if index == 1:
                        node = Node(data)
                        node.prev = current
                        node.next = current.next
                        current.next = node
                        break
                    current = current.next
                    if not current:
                        break
                    index -= 1
        except Exception as e:
            print(e)

    def deleteByValue(self, data):
        """delete the first node with the given value"""
        print(f"Removing node with value {data} from linked list")
        if not self.head:
            return
        current = self.head
        if current.data == data:
            self.head = current.next
            return
        while current:
            if current.next.data == data:
                temp = current.next
                current.next = temp.next
                if current.next:
                    current.prev = current.next.prev
                break
            current = current.next
            if not current:
                break

        gc.collect()

    def deleteAtIndex(self, index):
        """delete the node at a given index"""
        print(f"Removing node at {index} from linked list")
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            comparison = index > 0 if index < self.length() else index > self.length / 2
            while comparison:
                reached = (
                    index == 1 if index < self.length() else index == self.length - 1
                )
                if reached:
                    temp = current.next
                    if current.next:
                        current.next = temp.next
                        if current.next:
                            current.prev = current.next.prev
                    break
                current = current.next
                if not current:
                    break
                index -= 1

        gc.collect()

    def search(self, data):
        """search for the first node with the given value"""
        temp = self.head
        index = 0
        while temp:
            if temp.data == data:
                break
            temp = temp.next
            index += 1

        return (temp.data, index) if temp else f"{data} not found in linked list"

    def sort(self, sort_order="ASC"):
        """Sort data in sort_order. Defaults to "ASC"."""
        current = self.head
        nextNode = Node()

        if not current:
            return
        else:
            while current:
                nextNode = current.next
                while nextNode:
                    print(f"checking {current.data} and {nextNode.data}")
                    if (
                        current.data > nextNode.data
                        if sort_order == "ASC"
                        else current.data < nextNode.data
                    ):
                        print(f"Swapping {current.data} > {nextNode.data}")
                        temp = current.data
                        current.data = nextNode.data
                        nextNode.data = temp
                    nextNode = nextNode.next
                current = current.next


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.insert(1)
    doubly_linked_list.insert(4)
    doubly_linked_list.insert(3)
    doubly_linked_list.insert(2)
    doubly_linked_list.insert(7, 2)
    doubly_linked_list.insert(6, 0)

    print(doubly_linked_list)

    doubly_linked_list.deleteAtIndex(4)
    # doubly_linked_list.deleteByValue(1)

    # print(doubly_linked_list.search(3))

    doubly_linked_list.sort()

    # print(f"Length: {doubly_linked_list.length()}")
    print(doubly_linked_list)
