from random import randint
def partition(a, l, r):
    """ partitions the array a 
    with pivot as the first element"""
    pivot, i = a[l], l+1
    for j in range(l+1, r+1):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i-1], a[l] = a[l], a[i-1]
    return i-1

def random_selection(a, start, end, i):
    """ returns the ith order statistic 
    in the array a in linear time 
    >>> from random import sample
    >>> test_cases = [sample(range(20), 10) for i in range(10)]
    >>> orders = [randint(0, 9) for i in range(10)] 
    >>> results = [sorted(test_cases[i])[orders[i]] == random_selection(test_cases[i], 0, len(test_cases[i])-1, orders[i]) for i in range(10)]
    >>> print sum(results)
    10
    """
    if start < end:
        p = choosePivot(start, end)
        a[start], a[p] = a[p], a[start]
        j = partition(a, start, end)
        if j == i: return a[i]
        if j < i:
            return random_selection(a, j+1, end, i)
        else: # j > i
            return random_selection(a, start, j-1, i)
    else:
        return a[start]

def choosePivot(s, e):
    return randint(s,e)

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
