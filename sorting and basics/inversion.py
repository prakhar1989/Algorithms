count = 0
list = []
def mergeCount(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m

    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    global count
    global list
    i = 0
    j = 0
    k = l
    
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            count = count + (n1-i)
            '''for counter in range(n1-i):
                list.append(str(L[i+counter])+"  "+str(R[j]))'''
            arr[k] = R[j]
            j += 1
            
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def countInversion(arr,l,r):
    if l < r:

        m = (l+r)/2
        countInversion(arr, l, m)
        countInversion(arr, m+1, r)
        mergeCount(arr, l, m, r)

def start(size):
    arr = []
    global count
    count = 0
    for i in range(size):
        a = input()
        arr.append(a)
    #print ("Given array is")
    #print arr
    n = len(arr)
    countInversion(arr,0,n-1)
    #print list
    print count

n = input()
raw_input()
for i in range(n):
    size = input()
    start(size)
    if(i != n-1):
        raw_input()
