# Python program to find maximum contiguous subarray

def maxSubArraySum(a,size): 
	
	max_so_far = 0
	max_ending_here = 0
	
	for i in range(0, size): 
		max_ending_here = max_ending_here + a[i] 
		if max_ending_here < 0: 
			max_ending_here = 0
		
		# Do not compare for all elements. Compare only 
		# when max_ending_here > 0 
		elif (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
			
	return max_so_far 


# Driver function to check the above function (with a sample test case)

a = [3, 3, -25, 20, -3, 16, 23, -12, -5, 22, -15, 4, -7] 
print "Maximum contiguous sum is", maxSubArraySum(a,len(a))
