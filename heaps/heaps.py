class Heap:
    """Tree where parent node value is larger than child"""

    def __init__(self, input_arr=[]):
        self.arr = input_arr
        self.size = len(input_arr)

    def build_max(self):
        for i in range(self.size // 2, -1, -1):
            self.heapify(self.size, i)

        self.sort_max()

    def build_min(self):
        for i in range(self.size // 2, 0, -1):
            self.min_heapify(self.size, i)

    def sort_max(self):
        for i in range(self.size - 1, 0, -1):
            self.swap(i, 0)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.arr[i] < self.arr[l]:
            largest = l
        elif r < n and self.arr[largest] < self.arr[r]:
            largest = r

        # if root not largest, swap and heapify
        if largest != i:
            self.swap(i, largest)
            self.heapify(n, largest)

    def swap(self, curr, new):
        self.arr[curr], self.arr[new] = self.arr[new], self.arr[curr]

    def min_heapify(self, n, i):
        # check if non-leaf
        if not i * 2 > n:
            l = 2 * i
            r = 2 * i + 1

            if (
                l < n
                and r < n
                and (self.arr[i] > self.arr[l] or self.arr[i] > self.arr[r])
            ):
                # swap left, heapify left child
                if self.arr[i] < self.arr[l]:
                    self.swap(i, l)
                    self.min_heapify(n, l)
                else:
                    # swap right, heapify right child
                    self.swap(i, r)
                    self.min_heapify(n, r)

    def max(self):
        # found in last
        return self.arr[-1]

    def min(self):
        return self.arr[0]

    def display(self):
        for i in range(self.size):
            print(self.arr[i], end="\n")


if __name__ == "__main__":
    input_arr = [1, 12, 9, 5, 6, 10]
    heap = Heap(input_arr)
    # heap.build_max()
    heap.build_min()
    heap.display()
    print(f"\n {heap.min()}")
    # print(f"\n {heap.max()}")
