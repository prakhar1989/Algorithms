# A Dynamic Programming solution for subset 
# sum problem 
# Returns true if there is a subset of 
# with sum equal to the given sum 

def isSubsetSum(set, n, sum): 
	
	dp =([[False for i in range(sum + 1)] 
			for i in range(n + 1)]) 
	
	for i in range(n + 1): 
		dp[i][0] = True
		
	for i in range(1, sum + 1): 
		dp[0][i]= False
			
	for i in range(1, n + 1): 
		for j in range(1, sum + 1): 
			if j < set[i-1]: 
				dp[i][j] = dp[i-1][j] 
			if j >= set[i-1]: 
				dp[i][j] = (dp[i - 1][j] or
								dp[i - 1][j-set[i - 1]]) 
	return dp[n][sum] 
		
if __name__=='__main__': 
	set = [3, 34, 44, 1299, 5, 29] 
	sum = 9
	n = len(set) 
	if (isSubsetSum(set, n, sum) == True): 
		print("Subset found") 
	else: 
		print("No such subset") 
