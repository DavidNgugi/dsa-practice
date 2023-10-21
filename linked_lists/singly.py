from base import BaseNode


class Node(BaseNode):
    def __init__(self, data=None):
        super().__init__(data)

    def __repr__(self) -> str:
        return f"Node({self.data})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> None:
        """print the linked list"""
        try:
            temp = self.head
            while temp:
                print(str(temp.data), end="->")
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
        """insert data at tail or at a given index"""
        try:
            if index is None:
                index = self.length()

            if index < 0 or index > self.length():
                raise ValueError("Invalid index")

            print(f"inserting {data} into index {index}")

            if index == 0:
                node = Node(data)
                node.next = self.head
                self.head = node
            else:
                temp = self.head
                while index > 0:
                    if index == 1:
                        node = Node(data)
                        node.next = temp.next
                        temp.next = node
                        break
                    temp = temp.next
                    if not temp:
                        break
                    index -= 1
        except Exception as e:
            print(e)

    def deleteByValue(self, data):
        """delete the first node with the given value"""
        trav = self.head
        trav2 = self.head.next
        while trav:
            if trav.next.data == data:
                trav.next = trav2.next
                break
            trav = trav.next
            trav2 = trav2.next
            if not trav2:
                break

    def deleteAtIndex(self, index):
        """delete the node at a given index"""
        if index == 0:
            self.head = self.head.next
        else:
            trav = self.head
            trav2 = self.head.next
            while index > 0:
                if index == 1:
                    trav.next = trav2.next
                    break
                trav = trav.next
                trav2 = trav2.next
                if not trav2:
                    break
                index -= 1

    def search(self, data):
        """search for the first node with the given value"""
        temp = self.head
        index = 0
        while temp:
            if temp.data == data:
                break
            temp = temp.next
            index += 1

        return (temp.data, index)

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
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        prev = None
        temp = head
        
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        
        print(prev)
        return prev
    
    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        # print(head)

        temp = self.reverseListRecursive(head.next)

        head.next.next = head
        head.next = None

        return temp


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.insert(1)
    singly_linked_list.insert(4)
    singly_linked_list.insert(3)
    singly_linked_list.insert(2)
    singly_linked_list.insert(7, 2)
    print(singly_linked_list)
    # print(f"Length: {singly_linked_list.length()}")

    # singly_linked_list.deleteAtIndex(4)
    # print(singly_linked_list)

    # print(singly_linked_list.search(4))

    singly_linked_list.sort()

    print(singly_linked_list)
