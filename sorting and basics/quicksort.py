import random
import time
import sys

def partition(input_list,low,high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1],input_list[high] = input_list[high],input_list[i+1]
    return (i+1)

# Though there are built in function for sort in numpy
#We will use Quick Sort algorithm which is considered as FASTEST SORTING ALGORITHM.
def quickSort(input_list, low, high):
    if low < high:
        partition_index = partition(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)

#Function for Random number generation.
def random_no_generator():
    randomlist = []
    for i in range(0,10):
        n = random.randint(1,500)
        time.sleep(0.5)
        print(n ,sep='',end=" ",flush=True)
        randomlist.append(n)
    return randomlist

#Calculating complete execution time.
#""" FOR BEST EXECUTION TIME REMOVE *time.sleep()* FROM PROGRAM """"
start_time = time.time()

#Random Numbers
print('Random Numbers : ',end=' ')
numbers = random_no_generator()

#Sort Random numbers
quickSort(numbers, 0, len(numbers)-1)
print("\nSorted array : \t",end=' ')
time.sleep(0.5)
for i in range(0,10):
    time.sleep(0.3)
    print(numbers[i] ,end=" ",flush=True)

#Execution time    
end_time = time.time()
print('\n+] Program execution done in : ',end_time-start_time)
