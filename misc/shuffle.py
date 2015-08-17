"""
Fisher-Yates shuffle algorithm implemented in Python.

Reference :
https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
http://www.geeksforgeeks.org/shuffle-a-given-array/

Algorithm:
For all N indices of list, swap the element at a given index i with the element at a random index j where 0 <= j <= i.
"""

from random import randint

def shuffle(arr):
	"""
	Shuffle a list.
	"""
	for i in range(0,len(arr)):
		r = randint(0,i)
		arr[i],arr[r] = arr[r],arr[i]

if __name__ == '__main__':
	arr = [1,2,3,4,5,6]
	shuffle(arr)
	print(arr)
