def heapify(a,i, heapSize):
    """
    Implementation of heapify for a max heap
    :param a: A heap as a list
    :param i: Integer position of the current node
    :param heapSize: the size of the heap
    :return: None. Operations are done on the heap.
    """
    l = 2*i
    r = 2*i+1
    if (l < heapSize) and (a[l] > a[i]):
        largest = l
    else:
        largest = i

    if (r < heapSize) and (a[r] > a[largest]):
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, largest, heapSize)

def buildHeap(a):
    """
    Builds a Max heap from a random list of integers
    :param a: List to become the heap
    :return: None. Operations done on the heap.
    """
    i = len(a)//2
    heapSize = len(a)
    while i>=0:
        heapify(a,i,heapSize)
        i-=1

def heapsort(a):
    """
    Implementation of the heap sort algorithm on a max heap.
    :param a: Random list of integers to be sorted
    :return: None. Operations are done on the list.
    """
    a = buildHeap(a)
    heapSize = len(a)-1
    while heapSize >= 2:
        a[0], a[heapSize] = a[heapSize], a[0]
        heapSize-=1
        heapify(a,0,heapSize)
if __name__ == "__main__":
    #test case here.
    a = [10,3,4,6,7,9,1,2,5]
    print(a)
    buildHeap(a)
    print(a)
    heapsort(a)
    print(a)
