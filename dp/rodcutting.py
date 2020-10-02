INT_MIN = -32767

def RodCutting(price):
    n=len(price)
    val = [0 for x in range(n+1)] 
    val[0]=0
    for i in range(1, n + 1): 
        mx = INT_MIN 
        for j in range(i): 
             mx=max(mx, price[j] + val[i-j-1]) 
        val[i] = mx 
    return val[n] 

arr = list(map(int,input().split()))
print(str(RodCutting(arr)))
