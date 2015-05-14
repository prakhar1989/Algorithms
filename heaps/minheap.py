import math
class minheap(object):
    """
    Heap class - made of keys and items
    methods: build_heap, heappush, heappop
    """

    MIN_HEAP = True

    def __init__(self, nums=None):
        self.heap = []
        if nums:
            self.build_heap(nums)

    def __str__(self):
        return "Min-heap with %s items" % (len(self.heap))

    def max_elements(self):
        return len(self.heap)

    def height(self):
        return math.ceil(math.log(len(self.heap)) / math.log(2))

    def is_leaf(self, i):
        """ returns True if i is a leaf node """
        return i > int(math.ceil((len(self.heap) - 2) / 2.0))

    def parent(self, i):
        if i == 0:
            return -1
        elif i % 2 != 0: # odd
            return (i - 1) / 2
        return (i - 2) / 2

    def leftchild(self, i):
        return 2 * i + 1

    def rightchild(self, i):
        return 2 * i + 2

    def heapify(self, i):
        l = self.leftchild(i)
        r = self.rightchild(i)
        smallest = i
        if l < self.max_elements() and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < self.max_elements() and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_heap(self, elem):
        """ transforms a list of elements into a heap
        in linear time """
        self.heap = elem[:]
        last_leaf = self.parent(len(self.heap))
        for i in range(last_leaf, -1, -1):
            self.heapify(i)

    def heappush(self, x):
        """ Adds a new item x in the heap"""
        i = len(self.heap)
        self.heap.append(x)
        parent = self.parent(i)
        while parent != -1 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.parent(i)

    def heappop(self):
        """ extracts the root of the heap, min or max
        depending on the kind of heap"""
        if self.max_elements():
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            pop = self.heap.pop()
            self.heapify(0)
            return pop
        raise Exception("Heap is empty")
