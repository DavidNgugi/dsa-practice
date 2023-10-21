class CircularQueue:
    def __init__(self, n):
        self.n = n
        self.store = [None] * n
        # HEAD track the first element of the queue
        # TAIL track the last elements of the queue
        self.head = self.tail = -1

    def isEmpty(self):
        return self.n == 0

    def enqueue(self, value):
        """
        check if the queue is full
        for the first element, set value of FRONT to 0
        circularly increase the REAR index by 1
        (i.e. if the rear reaches the end, next it would be at the start of the queue)
        add the new element in the position pointed to by REAR
        """
        pass

    def dequeue(self):
        """
        check if the queue is empty
        return the value pointed by FRONT
        circularly increase the FRONT index by 1
        for the last element, reset the values of FRONT and REAR to -1
        However, the check for full queue has a new additional case:

        Case 1: FRONT = 0 && REAR == SIZE - 1
        Case 2: FRONT = REAR + 1
        """
        pass

    def peek(self):
        pass

    def display(self):
        # display in FIFO
        print("\nDisplay:")
        print(self.store)


if __name__ == "__main__":
    pass
