from random import randint
def qsort(a, start, end):
    """ quicksort in O(nlogn) and no extra
    memory. In place implementation
    >>> from random import sample
    >>> rand_list = [sample(range(100), 10) for j in range(10)]
    >>> sortedresult = [sorted(r) for r in rand_list]
    >>> for r in rand_list: qsort(r, 0, len(r)-1)
    >>> result = [sortedresult[i] == rand_list[i] for i in range(len(rand_list))]
    >>> print sum(result)
    10
    """
    if start < end:
        p = choosepivot(start, end)
        if p != start:
            a[p], a[start] = a[start], a[p]
        equal = partition(a, start, end)
        qsort(a, start, equal-1)
        qsort(a, equal+1, end)

def partition(a, l, r):
    """ partition array with pivot at a[0]
    in the array a[l...r] that returns the
    index of pivot element
    """
    pivot, i = a[l], l+1
    for j in range(l+1, r+1):
        if a[j] <= pivot:
            a[i],a[j] = a[j],a[i]
            i += 1
    # swap pivot to its correct place
    a[l], a[i-1] = a[i-1], a[l]
    return i-1

def choosepivot(s, e):
    return randint(s,e)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
