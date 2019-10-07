def quickSort(ar):

    # Base case
    if len(ar) <= 1:
        return ar

    # Let us choose middle element a pivot
    else:
        mid = len(ar)//2
        pivot = ar[mid]

        # key element is used to break the array
        # into 2 halves according to their values
        smaller,greater = [],[]

        # Put greater elements in greater list,
        # smaller elements in smaller list. Also,
        # compare positions to decide where to put.
        for indx, val in enumerate(ar):
            if indx != mid:
                if val < pivot:
                    smaller.append(val)
                elif val > pivot:
                    greater.append(val)

                # If value is same, then considering
                # position to decide the list.
                else:
                    if indx < mid:
                        smaller.append(val)
                    else:
                        greater.append(val)
        return quickSort(smaller)+[pivot]+quickSort(greater)

# Driver code to test above
ar = [10, 7, 8, 9, 1, 5]
sortedAr = quickSort(ar)
print(sortedAr) 
