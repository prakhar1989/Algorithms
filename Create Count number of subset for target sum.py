#Question:-Count the number of subset which can give the given target value by asssigning + or - in between elements
def bottom_up(arr,n,value):
    dp=[[0 for x in range(value+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(value+1):
            if i==0:
                dp[i][j]=0
            elif j==0:
                dp[i][j]=1
            elif( arr[i-1]<=j):
                dp[i][j]=dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[i][j]            
                
    

n=int(input())
arr=[int(x) for x in input().split()][:n]
value=int(input())
value=(sum(arr)+value)//2
d=bottom_up(arr,n,value)
print(d
