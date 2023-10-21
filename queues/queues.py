class QueueException(Exception):
    def __init__(self, message):
        self.message = message


class Queue:
    def __init__(self):
        self.store = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, value):
        if value:
            self.store.append(value)
            self.size += 1
            return
        raise QueueException("No value provided")

    def dequeue(self):
        # FIFO
        if not self.isEmpty():
            self.size -= 1
            popped = self.store.pop(0)
            print(f"Dequeue: {popped}")
            return popped
        raise QueueException("Queue empty")

    def peek(self):
        if not self.isEmpty():
            print(f"\nPeek: {self.store[0]}")
            return self.store[0]
        raise QueueException("Queue empty")

    def display(self):
        # display in FIFO
        print("\nDisplay:")
        print(self.store)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.peek()
    queue.display()

    queue.dequeue()
    queue.peek()
    queue.display()
