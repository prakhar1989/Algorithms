def mergesort(arr):
    """ perform mergesort on a list of numbers 

    >>> mergesort([5, 4, 1, 6, 2, 3, 9, 7])
    [1, 2, 3, 4, 5, 6, 7, 9]

    >>> mergesort([3, 2, 4, 2, 1])
    [1, 2, 2, 3, 4]
    """
    n = len(arr)
    if n <= 1: return arr
    a1 = mergesort(arr[:n/2])
    a2 = mergesort(arr[n/2:])
    return merge(a1, a2)

def merge(arr_a, arr_b):
    arr_c = []
    i, j = (0, 0)
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] <= arr_b[j]:
            arr_c.append(arr_a[i])
            i += 1
        else:
            arr_c.append(arr_b[j])
            j += 1
    if arr_a[i:]: arr_c.extend(arr_a[i:])
    if arr_b[j:]: arr_c.extend(arr_b[j:])
    return arr_c

def quicksort(a):
    """ quicksort implementation in python
    NOTE: This algo uses O(n) extra space
    to compute quicksort.

    >>> quicksort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    n = len(a)
    if n<=1:
        return a
    else:
        from random import randrange
        pivot = a.pop(randrange(n))
        lesser = quicksort([x for x in a if x < pivot])
        greater = quicksort([x for x in a if x >= pivot])
        return lesser + [pivot] + greater


def selectionsort(a):
    """ selectionsort implementation

    >>> selectionsort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    for i in range(len(a)):
        min = i
        for j in range(i,len(a)):
            if a[j] < a[min]: 
                min = j
        a[i],a[min] = a[min], a[i]
    return a

def bubblesort(a):
    """ bubble sort implementation
    
    >>> bubblesort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


def insertionsort(a):
    """ insertion sort implementation
    >>> insertionsort([6, 4, 8, 2, 1, 9, 10])
    [1, 2, 4, 6, 8, 9, 10]
    """
    for i in range(len(a)):
        item = a[i]
        j = i
        while j > 0 and a[j-1] > item:
            a[j] = a[j-1]
            j -= 1
        a[j] = item
    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
