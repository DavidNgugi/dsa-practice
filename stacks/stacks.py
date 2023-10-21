class StackException(Exception):
    def __init__(self, message):
        self.message = message


class Stack:
    def __init__(self):
        self.store = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        if value:
            self.store.append(value)
            self.size += 1
            return
        raise StackException("No value provided")

    def pop(self):
        if not self.isEmpty():
            self.size -= 1
            popped = self.store.pop()
            print(f"Pop: {popped}")
            return popped
        raise StackException("Stack empty")

    def peek(self):
        # get top item
        if not self.isEmpty():
            print(f"\nPeek: {self.store[-1]}")
            return self.store[-1]
        raise StackException("Stack empty")

    def display(self):
        # LIFO
        # prevent changing existing store for consequent operations on stack
        lifo_store = self.store
        lifo_store.reverse()
        print("\nDisplay:")
        print(lifo_store)

    def search(self, value):
        pass

    def delete(self, value):
        pass


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.peek()
    stack.display()

    stack.pop()
    stack.peek()
    stack.display()
