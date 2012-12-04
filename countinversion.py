def sort_and_count(a):
    """ counts the number of inversions
    in an array and returns the count and the
    sorted array in O(nlogn) time

    >>> sort_and_count([1, 3, 5, 2, 4, 6])
    ([1, 2, 3, 4, 5, 6], 3)
    """

    if len(a) == 1: return (a, 0)
    (b, x) = sort_and_count(a[:(len(a)/2)])
    (c, y) = sort_and_count(a[(len(a)/2):])
    (d, z) = merge_and_count_inv(b, c)
    return (d, x + y + z)

def merge_and_count_inv(b, c):
    d = []
    count = 0
    i, j = 0,0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            d.append(b[i])
            i += 1
        else: 
            d.append(c[j])
            j += 1
            # this works because all elements in b < c
            count += len(b[i:])
    if b[i:]: d += b[i:]
    if c[j:]: d += c[j:]
    return d, count

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
