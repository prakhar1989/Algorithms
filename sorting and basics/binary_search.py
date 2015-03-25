from sorting import mergesort


def search(arr, item):
    """Performs binary search on an array
    with the given item and returns True or
    False.

>>> search([5, 4, 1, 6, 2, 3, 9, 7], 2)
    True

>>> search([5, 4, 1, 6, 2, 3, 9, 7], 8)
    False
    """

    arr = mergesort(arr)

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == item:
            found = True
        else:
            if item < arr[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


print search([5, 4, 1, 6, 2, 3, 9, 7], 2)
print search([5, 4, 1, 6, 2, 3, 9, 7], 8)
