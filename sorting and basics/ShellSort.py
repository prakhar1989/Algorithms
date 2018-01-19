def shellSort(myArray):
    sublistCount = len(myArray)//2
    while sublistCount >0:
        for start in range(sublistCount):
            gapInsert(myArray,start,sublistCount)
	sublistCount = sublistCount //2

def gapInsert(myArray,start,gap):
    for x in range(start+gap,len(myArray),gap):
        current = myArray[x]
        pos = x
    while pos >=gap and myArray[pos-gap]> current:
        myArray[pos] = myArray[pos-gap]
        pos = pos-gap
    myArray[pos] = current


Array = [0,1000,900]
shellSort(Array)
print(Array)
