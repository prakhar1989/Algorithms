from minheap import minheap
class maxheap(minheap):
    """
    Heap class - made of keys and items
    methods: build_heap, heappush, heappop
    """

    MAX_HEAP = True

    def __str__(self):
        return "Max-heap with %s items" % (len(self.heap))

    def heapify(self, i):
        l = self.leftchild(i)
        r = self.rightchild(i)
        largest = i
        if l < self.max_elements() and self.heap[l] > self.heap[largest]:
            largest = l
        if r < self.max_elements() and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)

    def heappush(self, x):
        """ Adds a new item x in the heap"""
        i = len(self.heap)
        self.heap.append(x)
        parent = self.parent(i)
        while parent != -1 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.parent(i)
